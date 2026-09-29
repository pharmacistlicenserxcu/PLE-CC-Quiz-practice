@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ============================================
echo   📝 PLE-CC Quiz Practice - Compile + Push
echo ============================================
echo.

python compile_offline_db.py

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
echo   🚀 Pushing to GitHub...
echo ============================================
echo.

cd /d "%~dp0\.."
git add "PLE CC Quiz/quiz-data-offline.js"
git commit -m "chore: recompile quiz-data-offline.js [auto]"
git push

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARN] Git push failed. Check your internet connection or auth.
) else (
    echo.
    echo [DONE] Pushed to GitHub successfully!
)

echo.
pause
