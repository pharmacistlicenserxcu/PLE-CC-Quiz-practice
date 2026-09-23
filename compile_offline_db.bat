@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo ============================================
echo   📝 PLE-CC Quiz Practice - Compile Offline DB
echo ============================================
echo.

python compile_offline_db.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Compilation failed! Check error details above.
) else (
    echo.
    echo [SUCCESS] quiz-data-offline.js has been compiled successfully.
)
echo.
pause
