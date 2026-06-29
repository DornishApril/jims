@echo off
setlocal enabledelayedexpansion
REM ============================================================================
REM  KANBAN AGENT SWARM CREATOR v2
REM  Creates one kanban task per PDF in paper_folder
REM  Each agent writes to its OWN per-paper JSON file (no xlsx collision)
REM  Waits for all tasks to complete, then auto-merges into results.xlsx
REM ============================================================================

SET WORK_DIR=C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction
SET PAPER_DIR=%WORK_DIR%\paper_folder
SET OUTPUT_DIR=%WORK_DIR%\results
SET PER_PAPER_DIR=%OUTPUT_DIR%\per_paper
SET PROMPT_FILE=%WORK_DIR%\prompt.txt
SET PROFILE=default

echo ============================================
echo   KANBAN SWARM CREATOR v2
echo   Working Dir: %WORK_DIR%
echo   Paper Dir:   %PAPER_DIR%
echo   Output Dir:  %OUTPUT_DIR%
echo   Per-Paper:   %PER_PAPER_DIR%
echo   Profile:     %PROFILE%
echo ============================================
echo.

REM ---------------------------------------------------------------------------
REM Step 0: Create output directories
REM ---------------------------------------------------------------------------
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
    echo [OK] Results directory created.
) else (
    echo [OK] Results directory exists.
)

if not exist "%PER_PAPER_DIR%" (
    mkdir "%PER_PAPER_DIR%"
    echo [OK] Per-paper directory created.
) else (
    echo [OK] Per-paper directory exists.
)
echo.

REM ---------------------------------------------------------------------------
REM Step 1: Verify prompt.txt exists
REM ---------------------------------------------------------------------------
if not exist "%PROMPT_FILE%" (
    echo [ERROR] prompt.txt not found.
    exit /b 1
)
echo [OK] Prompt file found.
echo.

REM ---------------------------------------------------------------------------
REM Step 2: Create tasks per PDF
REM ---------------------------------------------------------------------------
SET COUNT=0

for %%F in ("%PAPER_DIR%\*.pdf") do (
    SET /a COUNT+=1
    SET "AGENT_OUTPUT=%PER_PAPER_DIR%\%%~nF.json"
    
    echo [CREATE] Task !COUNT!: %%~nxF
    
    hermes kanban create "Param Extraction: %%~nxF" --assignee %PROFILE% --body "Research Data Extraction agent. ONE paper only. ASSIGNED PAPER: %%~nxF. PAPER PATH: %PAPER_DIR%\%%~nxF. OUTPUT: Write a single JSON object to !AGENT_OUTPUT!. Use exact column names from prompt as keys. Missing values = null. Extract ONLY explicitly reported values, no inference. Read full extraction rules from %PROMPT_FILE%. WORKSPACE: %WORK_DIR%. Work ONLY here. Do NOT touch other papers. Do NOT write to results.xlsx. When done call kanban_complete with summary."
)

echo.
echo [OK] %COUNT% tasks created.
echo.

REM ---------------------------------------------------------------------------
REM Step 3: Start gateway
REM ---------------------------------------------------------------------------
echo [INFO] Starting gateway...
hermes gateway run --accept-hooks
echo.

REM ---------------------------------------------------------------------------
REM Step 4: Wait for all tasks to complete
REM ---------------------------------------------------------------------------
echo [INFO] Waiting for all agents to finish...
echo [INFO] (This may take several minutes. Press Ctrl+C to cancel monitoring.)
echo.

:WAIT_LOOP
REM Count running + ready tasks (tasks not yet done)
SET REMAINING=0
for /f "tokens=2 delims= " %%A in ('hermes kanban list 2^>nul ^| findstr /i "running ready blocked"') do (
    SET /a REMAINING+=1
)

REM Check if any tasks are still active
hermes kanban list 2>nul | findstr /i "running ready blocked" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [%DATE% %TIME%] Tasks still running. Checking again in 30 seconds...
    timeout /t 30 /nobreak >nul
    goto WAIT_LOOP
)

echo.
echo [OK] All agents have finished.
echo.

REM ---------------------------------------------------------------------------
REM Step 5: Merge per-paper JSONs into results.xlsx
REM ---------------------------------------------------------------------------
echo [INFO] Merging per-paper results into results.xlsx...
cd /d "%OUTPUT_DIR%"
python merge_results.py

echo.
echo ============================================
echo   SWARM COMPLETE
echo   Final output: %OUTPUT_DIR%\results.xlsx
echo   Per-paper JSONs: %PER_PAPER_DIR%
echo ============================================

pause
