@echo off
title IT Operations & Support Copilot
echo =========================================================================
echo Starting IT Operations & Support Copilot (Localhost Mode)
echo =========================================================================

echo.
echo Launching Web Platform on http://127.0.0.1:8000 ...
echo The application and static UI are bundled together.
echo.

:: Automatically open the web browser after a 2-second delay
start /b cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:8000"

:: Start Uvicorn ASGI server with the application factory
py -3.12 -m uvicorn mcp_rag_agent.api.app:create_app --factory --host 127.0.0.1 --port 8000 --reload
if %errorlevel% neq 0 (
    echo.
    echo py -3.12 not found, falling back to python...
    python -m uvicorn mcp_rag_agent.api.app:create_app --factory --host 127.0.0.1 --port 8000 --reload
)

pause
