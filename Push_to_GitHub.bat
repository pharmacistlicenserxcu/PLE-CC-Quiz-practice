@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ================================================================
echo   🚀 PLE-CC Quiz Practice - Full Deploy (Compile + Push)
echo   Target: pharmacistlicenserxcu/PLE-CC-Quiz-practice
echo ================================================================
echo.

REM ─── STEP 1: Compile ───────────────────────────────────────────
echo [1/2] Compiling offline database from Google Sheets...
echo.
python compile_offline_db.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Compilation failed! Push aborted.
    echo         Fix the error above and try again.
    echo.
    pause
    exit /b 1
)
echo.

REM ─── STEP 2: Git add, commit, push ────────────────────────────
echo [2/2] Pushing to GitHub...
echo.

if not exist ".git" (
    echo [INFO] Initializing Git repository...
    git init
    git branch -M main
    git remote add origin git@github.com:pharmacistlicenserxcu/PLE-CC-Quiz-practice.git
)

git status -s > tmp_status.txt 2>nul
set size=0
for %%A in (tmp_status.txt) do set size=%%~zA
del tmp_status.txt 2>nul

if "%size%"=="0" (
    echo [OK] No changes to commit. Pushing existing commits...
    git push -u origin main
    goto FINISH
)

echo [INFO] Changed files:
git status --short
echo.

set MYDATE=%date:~0,10%
set MYTIME=%time:~0,5%
set COMMIT_MSG=update: sync quiz database %MYDATE% %MYTIME%

echo [INFO] Commit: %COMMIT_MSG%
echo.
git add -A
git commit -m "%COMMIT_MSG%"
git push -u origin main

:FINISH
echo.
if %ERRORLEVEL%==0 (
    echo ================================================================
    echo   [SUCCESS] Deploy complete!
    echo   Live at: https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/
    echo ================================================================
) else (
    echo [ERROR] Push failed. Check internet or git permissions.
)
echo.
pause
