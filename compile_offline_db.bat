@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title PLE-CC Quiz Practice -- Compile ^& Push to GitHub
cd /d "%~dp0"

echo ================================================================
echo   [PLE-CC Quiz Practice] Compiler ^& GitHub Deploy
echo   Target: pharmacistlicenserxcu/PLE-CC-Quiz-practice (main)
echo ================================================================
echo.

if not "%~1"=="" (
    python compile_offline_db.py %*
    goto :GIT_DEPLOY
)

echo เลือกโหมดการทำงาน:
echo   [1] Fast Local Compile (จาก PLE CC QUIZ.xlsx) และ Push ขึ้น GitHub (~3 วิ)
echo   [2] Cloud Sync Compile (ดึงสดจาก Google Sheets) และ Push ขึ้น GitHub (~30 วิ)
echo   [3] Rebuild เฉพาะหมวดวิชา (Selective Category)
echo   [4] Git Push ทันที (ไม่ Recompile ข้อมูล)
echo.
set "CHOICE=1"
set /p "CHOICE=กรุณาเลือก [1-4] (กด Enter เลือก [1] Fast Local): "

if "%CHOICE%"=="1" (
    echo.
    echo [1/2] กำลัง Recompile ข้อมูลจาก PLE CC QUIZ.xlsx...
    python compile_offline_db.py --source excel
) else if "%CHOICE%"=="2" (
    echo.
    echo [1/2] กำลังดึงข้อมูลและ Recompile จาก Google Sheets...
    python compile_offline_db.py --source sheets
) else if "%CHOICE%"=="3" (
    echo.
    set /p "CAT_QUERY=พิมพ์ชื่อหมวดวิชา (เช่น Musculo, Cardio, Calc, Titration): "
    python compile_offline_db.py --mode category --query "!CAT_QUERY!"
) else if "%CHOICE%"=="4" (
    echo.
    echo [INFO] ข้ามขั้นตอน Compile...
    goto :GIT_DEPLOY
) else (
    echo.
    echo [1/2] กำลัง Recompile ข้อมูลจาก PLE CC QUIZ.xlsx...
    python compile_offline_db.py --source excel
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ================================================================
    echo  [ERROR] การ Compile ข้อมูลไม่สำเร็จ กรุณาตรวจสอบข้อผิดพลาดด้านบน
    echo ================================================================
    pause
    exit /b 1
)

:GIT_DEPLOY
echo.
echo [2/2] กำลังเตรียม Push ไฟล์ขึ้น GitHub...
git status --short
echo.
set MYDATE=%date:~0,10%
set MYTIME=%time:~0,5%
set COMMIT_MSG=update: sync quiz database and web app %MYDATE% %MYTIME%

git add -A
git commit -m "%COMMIT_MSG%"
echo.
echo [INFO] กำลัง Pull Rebase เพื่อป้องกันข้อขัดแย้ง...
git pull --rebase origin main
echo.
echo [INFO] กำลัง Push ขึ้น GitHub origin main...
git push origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================
    echo   [SUCCESS] Deploy สำเร็จเรียบร้อยแล้ว!
    echo   เว็บไซต์พร้อมใช้งานที่: https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/
    echo ================================================================
) else (
    echo.
    echo ================================================================
    echo   [WARNING] Git Push ไม่สำเร็จ กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
    echo ================================================================
)

echo.
pause
