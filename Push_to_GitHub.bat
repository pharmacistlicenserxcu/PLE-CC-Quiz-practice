@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title PLE-CC Quiz Practice -- 1-Click Fast Deploy
cd /d "%~dp0"

echo ================================================================
echo   [PLE-CC Quiz Practice] 1-Click Fast Deploy (Compile + Push)
echo   Target: pharmacistlicenserxcu/PLE-CC-Quiz-practice (main)
echo ================================================================
echo.

REM --- STEP 1: Compile offline database ---
echo [1/2] Compiling offline database (19-Column Schema + KaTeX)...
echo.
python compile_offline_db.py --source auto
if errorlevel 1 (
    echo.
    echo ================================================================
    echo  [ERROR] Compilation failed! Push aborted.
    echo ================================================================
    pause
    exit /b 1
)
echo.

REM --- STEP 2: Git add, commit, push ---
echo [2/2] Pushing all updates to GitHub...
echo.

git status --short
echo.

set MYDATE=%date:~0,10%
set MYTIME=%time:~0,5%
set COMMIT_MSG=update: sync quiz database and web app %MYDATE% %MYTIME%

echo [INFO] Commit message: %COMMIT_MSG%
echo.
git add -A
git commit -m "%COMMIT_MSG%"
echo.
echo [INFO] Pulling rebase from origin main...
git pull --rebase origin main
echo.
echo [INFO] Pushing to origin main...
git push origin main

if errorlevel 1 (
    echo.
    echo ================================================================
    echo  [ERROR] Push failed. Check internet connection or credentials.
    echo ================================================================
) else (
    echo.
    echo ================================================================
    echo   [SUCCESS] Deploy complete!
    echo   Live at: https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/
    echo ================================================================
)
echo.
pause
