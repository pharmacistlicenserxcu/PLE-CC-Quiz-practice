@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ============================================
echo   📝 PLE-CC Quiz Practice - Compiler v2.1
echo ============================================
echo.

if not "%~1"=="" (
    python compile_offline_db.py %*
    goto git_push
)

echo เลือกโหมดการทำงาน:
echo   [1] Rebuild ทั้งหมดทุกหมวด (All - 34 หมวด)
echo   [2] Rebuild แยกเรื่อง / เฉพาะหมวดวิชา (Category)
echo   [3] Rebuild แยกสายวิชา (Track - Clinic / Product / SAP)
echo.
set /p choice="กรุณาใส่ตัวเลข [1-3] (Default: 1): "

if "%choice%"=="2" (
    echo.
    set /p cat_query="พิมพ์ชื่อหมวดวิชา (เช่น Musculo, Cardio, Calc, Titration): "
    python compile_offline_db.py --mode category --query "%cat_query%"
) else if "%choice%"=="3" (
    echo.
    set /p track_query="พิมพ์สายวิชา [Clinic / Product / SAP]: "
    python compile_offline_db.py --mode track --query "%track_query%"
) else (
    python compile_offline_db.py --mode all
)

:git_push
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Compilation failed! Check error details above.
    echo [SKIP]  Git push skipped due to compile error.
    echo.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] quiz-data-offline.js compiled successfully.
echo.
echo ============================================
echo   🚀 Pushing to GitHub (Submodule)...
echo ============================================
echo.

git add quiz-data-offline.js sw.js
git commit -m "chore: recompile quiz offline database [local auto]"
git push origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARN] Git push in submodule failed. Check your network or credentials.
) else (
    echo.
    echo [DONE] Pushed to GitHub submodule successfully!
)

echo.
pause
