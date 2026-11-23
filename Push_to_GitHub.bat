@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title PLE-CC Quiz Practice -- Google Sheets Sync ^& GitHub Deploy
cd /d "%~dp0"

echo ================================================================
echo   [PLE-CC Quiz Practice] Google Sheets Sync ^& GitHub Deploy
echo   Target Repo  : pharmacistlicenserxcu/PLE-CC-Quiz-practice (main)
echo   Google Sheet : 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
echo ================================================================
echo.
echo [ข้อกำหนดความปลอดภัย]
echo ระบบจะดึงข้อมูลสดจาก Google Sheets เท่านั้น (ไม่ใช้ Local Cache เก่า)
echo เพื่อป้องกันการนำข้อสอบเก่าที่ไม่ได้อัปเดตขึ้นเว็บ
echo.

set "CONFIRM="
set /p "CONFIRM=ต้องการดึงข้อสอบสดและ Deploy ขึ้น GitHub หรือไม่? [กด Y แล้ว Enter]: "
if /i not "!CONFIRM!"=="Y" (
    echo.
    echo [CANCELLED] ยกเลิกการทำงาน ไม่มีการเปลี่ยนแปลงใดๆ
    echo.
    pause
    exit /b 0
)

echo.
echo [0/3] กำลังเคลียร์สถานะ Git และดึงความเปลี่ยนแปลงล่าสุดจาก Remote...
git rebase --abort 2>nul
git merge --abort 2>nul
git fetch origin main

echo.
echo [1/3] กำลังดาวน์โหลดและ Compile ข้อมูลสดจาก Google Sheets...
python compile_offline_db.py --source sheets
if errorlevel 1 (
    echo.
    echo ================================================================
    echo  [ERROR] การ Compile ข้อมูลจาก Google Sheets ล้มเหลว!
    echo  ระบบยกเลิกการ Push เพื่อป้องกันข้อสอบเสียหาย กรุณาตรวจสอบข้อผิดพลาด
    echo ================================================================
    echo.
    pause
    exit /b 1
)
echo.

echo [2/3] ตรวจสอบไฟล์ที่มีการเปลี่ยนแปลงและเตรียม Commit...
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

echo [INFO] Commit message: !COMMIT_MSG!
git commit -m "!COMMIT_MSG!"

echo.
echo [3/3] กำลัง Push ขึ้น GitHub origin main...
git push origin main
if errorlevel 1 (
    echo.
    echo [INFO] Remote มีการเปลี่ยนแปลงใหม่ กำลังซิงก์และ Push ซ้ำ...
    git fetch origin main
    git reset --soft origin/main
    git commit -m "!COMMIT_MSG!"
    git push origin main
)

if errorlevel 1 (
    echo.
    echo ================================================================
    echo  [ERROR] Push ขึ้น GitHub ไม่สำเร็จ กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
    echo ================================================================
) else (
    echo.
    echo ================================================================
    echo   [SUCCESS] Deploy ข้อสอบจาก Google Sheets สำเร็จเรียบร้อยแล้ว!
    echo   เว็บไซต์พร้อมใช้งานที่: https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/
    echo ================================================================
)
echo.
pause
