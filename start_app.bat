@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "PYTHONPATH=%CD%\src;%PYTHONPATH%"
set "PYTHON_EXE="
set "PYTHON_ARGS="

if exist "%CD%\.venv\Scripts\python.exe" (
    set "PYTHON_EXE=%CD%\.venv\Scripts\python.exe"
) else (
    where py >nul 2>nul
    if not errorlevel 1 (
        set "PYTHON_EXE=py"
        set "PYTHON_ARGS=-3.12"
    ) else (
        where python >nul 2>nul
        if not errorlevel 1 set "PYTHON_EXE=python"
    )
)

if not defined PYTHON_EXE (
    echo ERROR: No Python interpreter found. Create .venv and install requirements first.
    exit /b 1
)

title IT Operations ^& Support Copilot
echo =========================================================================
echo Starting IT Operations ^& Support Copilot (Localhost Mode)
echo =========================================================================

echo.
echo Launching Web Platform on http://127.0.0.1:8000 ...
echo The application and static UI are bundled together.
echo.

:: Automatically open the web browser after a 2-second delay
start /b cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:8000"

:: Start Uvicorn ASGI server with the application factory
"%PYTHON_EXE%" %PYTHON_ARGS% -m uvicorn mcp_rag_agent.api.app:create_app --factory --host 127.0.0.1 --port 8000 --reload

pause
