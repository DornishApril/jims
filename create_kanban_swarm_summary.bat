@echo off
setlocal enabledelayedexpansion
REM ============================================================================
REM  KANBAN AGENT SWARM CREATOR — PAPER SUMMARIZATION v3
REM  Creates one kanban task per PDF in paper_folder
REM  Each agent writes a detailed .md summary to results/summaries/
REM  Waits for all tasks to complete
REM ============================================================================

SET WORK_DIR=C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction
SET PAPER_DIR=%WORK_DIR%\paper_folder
SET OUTPUT_DIR=%WORK_DIR%\results
SET SUMMARIES_DIR=%OUTPUT_DIR%\summaries
SET PROMPT_FILE=%WORK_DIR%\prompt2.txt
SET PROFILE=default

echo ============================================
echo   PAPER SUMMARIZATION SWARM v3
echo   Working Dir:  %WORK_DIR%
echo   Paper Dir:    %PAPER_DIR%
echo   Output Dir:   %SUMMARIES_DIR%
echo   Profile:      %PROFILE%
echo ============================================
echo.

REM ---------------------------------------------------------------------------
REM Step 0: Create output directories
REM ---------------------------------------------------------------------------
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"
if not exist "%SUMMARIES_DIR%" mkdir "%SUMMARIES_DIR%"
echo [OK] Directories ready.
echo.

REM ---------------------------------------------------------------------------
REM Step 1: Verify prompt2.txt exists
REM ---------------------------------------------------------------------------
if not exist "%PROMPT_FILE%" (
    echo [ERROR] prompt2.txt not found at: %PROMPT_FILE%
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
    SET "PAPER_BASENAME=%%~nF"
    SET "AGENT_OUTPUT=%SUMMARIES_DIR%\%%~nF.md"
    
    echo [CREATE] Task !COUNT!: %%~nxF
    
    hermes kanban create "Paper Summary: %%~nxF" --assignee %PROFILE% --body "Read the full instructions from %PROMPT_FILE% and follow them EXACTLY. YOUR ASSIGNED PAPER: %%~nxF. PAPER PATH: %PAPER_DIR%\%%~nxF. OUTPUT FILE: !AGENT_OUTPUT!. Write a single comprehensive Markdown file. Do a minimum of 2-3 full passes through the paper before writing. Follow the EXACT section structure specified in the prompt. When done call kanban_complete with summary."
)

echo.
echo [OK] %COUNT% tasks created.
echo.

REM ---------------------------------------------------------------------------
REM Step 3: Start gateway (background)
REM ---------------------------------------------------------------------------
echo [INFO] Starting gateway in background...
start "Hermes Gateway" /B cmd /c "hermes gateway run --accept-hooks"
timeout /t 5 /nobreak >nul
echo [OK] Gateway started.
echo.

REM ---------------------------------------------------------------------------
REM Step 4: Wait for all tasks to complete
REM ---------------------------------------------------------------------------
echo [INFO] Waiting for all agents to finish...
echo [INFO] (This may take 10-20 minutes per paper. Press Ctrl+C to cancel.)
echo.

:WAIT_LOOP
hermes kanban list 2>nul | findstr /i "running ready blocked" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [%DATE% %TIME%] Tasks still active, checking again in 30s...
    timeout /t 30 /nobreak >nul
    goto WAIT_LOOP
)

echo.
echo [OK] All agents have finished.
echo.

REM ---------------------------------------------------------------------------
REM Step 5: Report results
REM ---------------------------------------------------------------------------
echo.
echo ============================================
echo   SUMMARIZATION COMPLETE
echo   Output: %SUMMARIES_DIR%
echo ============================================
echo.
echo Files created:
dir /b "%SUMMARIES_DIR%\*.md" 2>nul
echo.
echo To read a summary, open any .md file in that folder.
echo ============================================

pause
