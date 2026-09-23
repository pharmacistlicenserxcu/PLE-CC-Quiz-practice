@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ========================================================
echo   📝 PLE-CC Quiz Practice - Push to GitHub Pages
echo   Target Repo: pharmacistlicenserxcu/PLE-CC-Quiz-practice
echo ========================================================
echo.

echo [1/3] Compiling offline database from Google Sheets...
python compile_offline_db.py
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Python compilation encountered an issue, continuing with existing files...
)
echo.

echo [2/3] Checking for Git repository status...
if not exist ".git" (
    echo [INFO] Initializing Git repository...
    git init
    git branch -M main
    git remote add origin https://github.com/pharmacistlicenserxcu/PLE-CC-Quiz-practice.git
)

git status -s > tmp_status.txt 2>nul
set size=0
for %%A in (tmp_status.txt) do set size=%%~zA
del tmp_status.txt 2>nul

if "%size%"=="0" (
    echo [OK] No changes detected. All files are already committed!
    echo.
    echo Pushing any pending commits to GitHub...
    git push -u origin main
    goto FINISH
)

echo [INFO] Changed files:
echo.
git status --short
echo.

set MYDATE=%date:~0,10%
set MYTIME=%time:~0,5%
set COMMIT_MSG=update: sync quiz database %MYDATE% %MYTIME%

echo [INFO] Commit Message: %COMMIT_MSG%
echo.

git add -A
git commit -m "%COMMIT_MSG%"
echo.

echo [3/3] Pushing to GitHub (origin main)...
git push -u origin main

:FINISH
echo.
if %ERRORLEVEL%==0 (
    echo ============================================================
    echo   [SUCCESS] Push complete!
    echo   Quiz website is now live at:
    echo   https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/
    echo ============================================================
) else (
    echo [ERROR] Push failed. Check your internet connection or git permissions.
)
echo.
pause
