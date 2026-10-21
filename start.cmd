@echo off
title IT Operations & Support Copilot - Local Launcher
echo =========================================================================
echo Starting IT Operations & Support Copilot (Localhost Mode)
echo =========================================================================

echo.
echo Launching server on http://127.0.0.1:8000 ...
echo Opening http://localhost:8000 in your browser...
echo.

:: Automatically open browser
start /b cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:8000"

:: Launch ASGI app
py -3.12 -m uvicorn mcp_rag_agent.api.app:create_app --factory --host 127.0.0.1 --port 8000 --reload
if %errorlevel% neq 0 (
    python -m uvicorn mcp_rag_agent.api.app:create_app --factory --host 127.0.0.1 --port 8000 --reload
)

pause
