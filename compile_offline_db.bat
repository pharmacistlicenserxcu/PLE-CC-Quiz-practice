@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title PLE-CC Quiz Practice -- Compiler ^& GitHub Deploy
cd /d "%~dp0"

echo ================================================================
echo   [PLE-CC Quiz Practice] Compiler ^& GitHub Deploy
echo   Target Repo  : pharmacistlicenserxcu/PLE-CC-Quiz-practice (main)
echo   Google Sheet : 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
echo ================================================================
echo.

if not "%~1"=="" (
    python compile_offline_db.py %*
    goto :GIT_DEPLOY
)

echo เลือกโหมดการทำงาน:
echo   [1] Cloud Sync Compile (ดึงสดจาก Google Sheets) และ Push ขึ้น GitHub [ค่าเริ่มต้น แนะนำ]
echo   [2] Rebuild เฉพาะหมวดวิชา (Selective Category)
echo   [3] Git Push ทันที (ไม่ Recompile ข้อมูล)
echo   [9] [คำเตือน] Fast Local Compile (ใช้ไฟล์ Excel เก่าบนเครื่อง - เสี่ยงข้อมูลไม่อัปเดต)
echo.
set "CHOICE=1"
set /p "CHOICE=กรุณาเลือก [1-3, 9] (กด Enter เลือก [1] ดึงสดจาก Google Sheets): "

if "%CHOICE%"=="1" (
    echo.
    echo ================================================================
    echo  ยืนยันการดึงข้อมูลสดจาก Google Sheets และ Push ขึ้น GitHub
    echo ================================================================
    set "CONFIRM="
    set /p "CONFIRM=กด Y เพื่อเริ่ม (หรือ N เพื่อยกเลิก) [Y/N]: "
    if /i not "!CONFIRM!"=="Y" (
        echo [CANCELLED] ยกเลิกการทำงาน
        pause
        exit /b 0
    )
    echo.
    echo [0/3] กำลังเคลียร์สถานะ Git...
    git rebase --abort 2>nul
    git merge --abort 2>nul
    git fetch origin main

    echo.
    echo [1/3] กำลังดึงข้อมูลสดและ Recompile จาก Google Sheets...
    python compile_offline_db.py --source sheets
) else if "%CHOICE%"=="2" (
    echo.
    set /p "CAT_QUERY=พิมพ์ชื่อหมวดวิชา (เช่น Musculo, Cardio, Calc, Titration): "
    git rebase --abort 2>nul
    git merge --abort 2>nul
    git fetch origin main
    python compile_offline_db.py --mode category --query "!CAT_QUERY!"
) else if "%CHOICE%"=="3" (
    echo.
    echo [INFO] ข้ามขั้นตอน Compile...
    goto :GIT_DEPLOY
) else if "%CHOICE%"=="9" (
    echo.
    echo ================================================================
    echo  [คำเตือนความเสี่ยง] โหมด Fast Local จะใช้ไฟล์ PLE CC QUIZ.xlsx เก่าบนเครื่อง
    echo  ข้อสอบที่เพิ่งแก้หรือเพิ่มบน Google Sheets จะไม่ถูกนำมาประมวลผล!
    echo ================================================================
    set "CONFIRM_LOCAL="
    set /p "CONFIRM_LOCAL=หากต้องการใช้ไฟล์เก่าบนเครื่องจริง ให้พิมพ์คำว่า YES: "
    if not "!CONFIRM_LOCAL!"=="YES" (
        echo [CANCELLED] ยกเลิกโหมด Local เพื่อความปลอดภัย แนะนำให้ใช้โหมด [1]
        pause
        exit /b 0
    )
    echo.
    echo [1/3] กำลัง Recompile จากไฟล์ Excel ในเครื่อง...
    python compile_offline_db.py --source excel --allow-local
) else (
    echo.
    echo [1/3] กำลังดึงข้อมูลสดและ Recompile จาก Google Sheets...
    git rebase --abort 2>nul
    git merge --abort 2>nul
    git fetch origin main
    python compile_offline_db.py --source sheets
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ================================================================
    echo  [ERROR] การ Compile ข้อมูลไม่สำเร็จ ยกเลิกการ Push ขึ้น GitHub
    echo ================================================================
    pause
    exit /b 1
)

:GIT_DEPLOY
echo.
echo [2/3] กำลังเตรียม Push ไฟล์ขึ้น GitHub...
git fetch origin main
git reset --soft origin/main
git add -A

for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value 2^>nul') do set "dt=%%I"
if defined dt (
    set "YYYY=!dt:~0,4!"
    set "MM=!dt:~4,2!"
    set "DD=!dt:~6,2!"
    set "HH=!dt:~8,2!"
    set "MIN=!dt:~10,2!"
    set "COMMIT_MSG=update: sync quiz database from Google Sheets (!YYYY!-!MM!-!DD! !HH!:!MIN!)"
) else (
    set "COMMIT_MSG=update: sync quiz database from Google Sheets (%date% %time%)"
)

git commit -m "!COMMIT_MSG!"
echo.
echo [3/3] กำลัง Push ขึ้น GitHub origin main...
git push origin main
if errorlevel 1 (
    echo.
    echo [INFO] Remote มีการอัปเดตใหม่ กำลังซิงก์และ Push ซ้ำ...
    git fetch origin main
    git reset --soft origin/main
    git commit -m "!COMMIT_MSG!"
    git push origin main
)

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
