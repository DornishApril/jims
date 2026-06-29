@echo off
REM ============================================================================
REM  KANBAN AGENT SWARM CREATOR
REM  Creates one kanban task per PDF in paper_folder
REM  All agents share the same extraction prompt from prompt.txt
REM ============================================================================

SET WORK_DIR=C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction
SET PAPER_DIR=%WORK_DIR%\paper_folder
SET OUTPUT_DIR=%WORK_DIR%\results
SET PROMPT_FILE=%WORK_DIR%\prompt.txt
SET PROFILE=default

echo ============================================
echo   KANBAN SWARM CREATOR
echo   Working Dir: %WORK_DIR%
echo   Paper Dir:   %PAPER_DIR%
echo   Output Dir:  %OUTPUT_DIR%
echo   Profile:     %PROFILE%
echo ============================================
echo.

REM ---------------------------------------------------------------------------
REM Step 0: Create output directory if it doesn't exist
REM ---------------------------------------------------------------------------
if not exist "%OUTPUT_DIR%" (
    echo [INFO] Creating results directory...
    mkdir "%OUTPUT_DIR%"
    echo [OK] Results directory created: %OUTPUT_DIR%
) else (
    echo [OK] Results directory already exists: %OUTPUT_DIR%
)
echo.

REM ---------------------------------------------------------------------------
REM Step 1: Verify prompt.txt exists
REM ---------------------------------------------------------------------------
if not exist "%PROMPT_FILE%" (
    echo [ERROR] prompt.txt not found at: %PROMPT_FILE%
    echo Aborting.
    exit /b 1
)
echo [OK] Prompt file found: %PROMPT_FILE%
echo.

REM ---------------------------------------------------------------------------
REM Step 2: Count PDF files
REM ---------------------------------------------------------------------------
SET COUNT=0
for %%F in ("%PAPER_DIR%\*.pdf") do SET /a COUNT+=1
echo [INFO] Found %COUNT% PDF files in paper_folder.
echo.

REM ---------------------------------------------------------------------------
REM Step 3: Create kanban tasks — one per PDF
REM ---------------------------------------------------------------------------
echo [INFO] Creating %COUNT% kanban tasks...
echo.

REM Task 1: 1-s2.0-S2352484723001609-main.pdf
hermes kanban create "Param Extraction: 1-s2.0-S2352484723001609-main.pdf" --assignee %PROFILE% --body "Your assigned paper: 1-s2.0-S2352484723001609-main.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\1-s2.0-S2352484723001609-main.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 2: Techno-Economic_Analysis_of_Hybrid_Hydrogen_Fuel-Cell_PV_Wind_Turbine_Battery_Diesel_Energy_System_for_Rural_Coastal_Community_in_Western_Australia.pdf
hermes kanban create "Param Extraction: Techno-Economic_Analysis_of_Hybrid_Hydrogen_Fuel-Cell_PV_Wind_Turbine_Battery_Diesel_Energy_System_for_Rural_Coastal_Community_in_Western_Australia.pdf" --assignee %PROFILE% --body "Your assigned paper: Techno-Economic_Analysis_of_Hybrid_Hydrogen_Fuel-Cell_PV_Wind_Turbine_Battery_Diesel_Energy_System_for_Rural_Coastal_Community_in_Western_Australia.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Techno-Economic_Analysis_of_Hybrid_Hydrogen_Fuel-Cell_PV_Wind_Turbine_Battery_Diesel_Energy_System_for_Rural_Coastal_Community_in_Western_Australia.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 3: Article 3607.pdf
hermes kanban create "Param Extraction: Article 3607.pdf" --assignee %PROFILE% --body "Your assigned paper: Article 3607.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Article 3607.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 4: Article 36.pdf
hermes kanban create "Param Extraction: Article 36.pdf" --assignee %PROFILE% --body "Your assigned paper: Article 36.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Article 36.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 5: Article 37.pdf
hermes kanban create "Param Extraction: Article 37.pdf" --assignee %PROFILE% --body "Your assigned paper: Article 37.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Article 37.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 6: Article 38.pdf
hermes kanban create "Param Extraction: Article 38.pdf" --assignee %PROFILE% --body "Your assigned paper: Article 38.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Article 38.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 7: Article 39.pdf
hermes kanban create "Param Extraction: Article 39.pdf" --assignee %PROFILE% --body "Your assigned paper: Article 39.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Article 39.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 8: 1-s2.0-S0959652622033388-main.pdf
hermes kanban create "Param Extraction: 1-s2.0-S0959652622033388-main.pdf" --assignee %PROFILE% --body "Your assigned paper: 1-s2.0-S0959652622033388-main.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\1-s2.0-S0959652622033388-main.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 9: Article Text-19435-1-10-20260522.pdf
hermes kanban create "Param Extraction: Article Text-19435-1-10-20260522.pdf" --assignee %PROFILE% --body "Your assigned paper: Article Text-19435-1-10-20260522.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\Article Text-19435-1-10-20260522.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 10: mathematics-10-03708-v2.pdf
hermes kanban create "Param Extraction: mathematics-10-03708-v2.pdf" --assignee %PROFILE% --body "Your assigned paper: mathematics-10-03708-v2.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\mathematics-10-03708-v2.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 11: 60169-194014-4-PB.pdf
hermes kanban create "Param Extraction: 60169-194014-4-PB.pdf" --assignee %PROFILE% --body "Your assigned paper: 60169-194014-4-PB.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\60169-194014-4-PB.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 12: ok58218-189848-2-PB.pdf
hermes kanban create "Param Extraction: ok58218-189848-2-PB.pdf" --assignee %PROFILE% --body "Your assigned paper: ok58218-189848-2-PB.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\ok58218-189848-2-PB.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 13: ayop2018.pdf
hermes kanban create "Param Extraction: ayop2018.pdf" --assignee %PROFILE% --body "Your assigned paper: ayop2018.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\ayop2018.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 14: han2017.pdf
hermes kanban create "Param Extraction: han2017.pdf" --assignee %PROFILE% --body "Your assigned paper: han2017.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\han2017.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 15: s41598-024-55631-3.pdf
hermes kanban create "Param Extraction: s41598-024-55631-3.pdf" --assignee %PROFILE% --body "Your assigned paper: s41598-024-55631-3.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\s41598-024-55631-3.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 16: 1-s2.0-S1110016820305457-main.pdf
hermes kanban create "Param Extraction: 1-s2.0-S1110016820305457-main.pdf" --assignee %PROFILE% --body "Your assigned paper: 1-s2.0-S1110016820305457-main.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\1-s2.0-S1110016820305457-main.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 17: file.pdf
hermes kanban create "Param Extraction: file.pdf" --assignee %PROFILE% --body "Your assigned paper: file.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\file.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 18: (1) Design simulation of hydrogen based hybrid green power system using sea water for Cox s Bazar.pdf
hermes kanban create "Param Extraction: (1) Design simulation of hydrogen based hybrid green power system using sea water for Cox s Bazar.pdf" --assignee %PROFILE% --body "Your assigned paper: (1) Design simulation of hydrogen based hybrid green power system using sea water for Cox s Bazar.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\(1) Design simulation of hydrogen based hybrid green power system using sea water for Cox s Bazar.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 19: (10) Techno-economic and multicriteria analysis of grid-connected energy systems for hydrogen production_ A case study from Bangladesh.pdf
hermes kanban create "Param Extraction: (10) Techno-economic and multicriteria analysis of grid-connected energy systems for hydrogen production_ A case study from Bangladesh.pdf" --assignee %PROFILE% --body "Your assigned paper: (10) Techno-economic and multicriteria analysis of grid-connected energy systems for hydrogen production_ A case study from Bangladesh.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\(10) Techno-economic and multicriteria analysis of grid-connected energy systems for hydrogen production_ A case study from Bangladesh.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 20: (6) Optimizing an integrated hybrid energy system with hydrogen-based storage to develop an off-grid green community for sustainable development in Bangladesh.pdf
hermes kanban create "Param Extraction: (6) Optimizing an integrated hybrid energy system with hydrogen-based storage to develop an off-grid green community for sustainable development in Bangladesh.pdf" --assignee %PROFILE% --body "Your assigned paper: (6) Optimizing an integrated hybrid energy system with hydrogen-based storage to develop an off-grid green community for sustainable development in Bangladesh.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\(6) Optimizing an integrated hybrid energy system with hydrogen-based storage to develop an off-grid green community for sustainable development in Bangladesh.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 21: (13) Solar, Wind, Hydrogen, and Bioenergy-Based Hybrid System for Off-Grid Remote Locations_ Techno-Economic and Environmental Analysis.pdf
hermes kanban create "Param Extraction: (13) Solar, Wind, Hydrogen, and Bioenergy-Based Hybrid System for Off-Grid Remote Locations_ Techno-Economic and Environmental Analysis.pdf" --assignee %PROFILE% --body "Your assigned paper: (13) Solar, Wind, Hydrogen, and Bioenergy-Based Hybrid System for Off-Grid Remote Locations_ Techno-Economic and Environmental Analysis.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\(13) Solar, Wind, Hydrogen, and Bioenergy-Based Hybrid System for Off-Grid Remote Locations_ Techno-Economic and Environmental Analysis.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 22: (15) The Best Techno-economic Aspects of the Feasibility Study Concerning the Proposed PV- Wind-hydro Hybrid System in Nilphamari, Bangladesh.pdf
hermes kanban create "Param Extraction: (15) The Best Techno-economic Aspects of the Feasibility Study Concerning the Proposed PV- Wind-hydro Hybrid System in Nilphamari, Bangladesh.pdf" --assignee %PROFILE% --body "Your assigned paper: (15) The Best Techno-economic Aspects of the Feasibility Study Concerning the Proposed PV- Wind-hydro Hybrid System in Nilphamari, Bangladesh.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\(15) The Best Techno-economic Aspects of the Feasibility Study Concerning the Proposed PV- Wind-hydro Hybrid System in Nilphamari, Bangladesh.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

REM Task 23: (8) Hydrogen Energy Storage Based Green Power Plant in Seashore of Bangladesh Design and Optimal Cost Analysis.pdf
hermes kanban create "Param Extraction: (8) Hydrogen Energy Storage Based Green Power Plant in Seashore of Bangladesh Design and Optimal Cost Analysis.pdf" --assignee %PROFILE% --body "Your assigned paper: (8) Hydrogen Energy Storage Based Green Power Plant in Seashore of Bangladesh Design and Optimal Cost Analysis.pdf. Read the prompt from C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\prompt.txt and follow it exactly. Your working directory is C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. The paper is at C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\paper_folder\(8) Hydrogen Energy Storage Based Green Power Plant in Seashore of Bangladesh Design and Optimal Cost Analysis.pdf. Write extracted results to C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction\results\results.xlsx. APPEND mode — do not overwrite existing data. Only work inside C:\Users\Admin\OneDrive\Desktop\jims\parameters_extraction. When done, call kanban_complete with summary."

echo.
echo ============================================
echo   TASKS CREATED: %COUNT%
echo ============================================
echo.

REM ---------------------------------------------------------------------------
REM Step 4: Verify tasks were created
REM ---------------------------------------------------------------------------
echo [INFO] Verifying tasks...
hermes kanban list --status ready
echo.

REM ---------------------------------------------------------------------------
REM Step 5: Start gateway to dispatch all tasks
REM ---------------------------------------------------------------------------
echo [INFO] Starting gateway to dispatch tasks...
hermes gateway start
echo.

echo ============================================
echo   SWARM DEPLOYED!
echo   Gateway is now dispatching %COUNT% agents.
echo   Monitor with: hermes kanban list
echo   Gateway status: hermes gateway status
echo ============================================

pause
