"""Health and readiness diagnostic endpoints."""

import asyncio
import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Response, status
try:
    from pymongo import MongoClient
except ImportError:
    class MongoClient:  # type: ignore
        pass

from mcp_rag_agent.api.dependencies import get_config
from mcp_rag_agent.api.schemas.health import (
    HealthResponse,
    ReadinessDetails,
    ReadinessResponse,
)
from mcp_rag_agent.core.config import Config
from mcp_rag_agent.database.client import LocalDatabaseClient

logger = logging.getLogger("HealthRoutes")

router = APIRouter(tags=["Health & Diagnostics"])


@router.get("/health", response_model=HealthResponse, summary="Liveness Probe")
async def health_check() -> HealthResponse:
    """Fast, low-overhead liveness check confirming the HTTP service is running."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(timezone.utc).isoformat(),
        app_name="MCP RAG Agent",
        app_version="0.1.0",
    )


@router.get("/ready", response_model=ReadinessResponse, summary="Readiness Probe")
async def readiness_check(
    response: Response,
    cfg: Config = Depends(get_config),
) -> ReadinessResponse:
    """Deep readiness probe verifying database connectivity and model configuration."""
    # 1. Database check (supports local SQLite database or MongoDB)
    db_status = "disconnected"
    if cfg.db_url and cfg.db_name:
        try:

            def _ping_database() -> bool:
                if cfg.db_url.startswith("mongodb://") or cfg.db_url.startswith("mongodb+srv://"):
                    client = MongoClient(
                        cfg.db_url,
                        serverSelectionTimeoutMS=1500,
                        connectTimeoutMS=1500,
                    )
                    client.admin.command("ping")
                    return True
                else:
                    db_path = getattr(cfg, "local_db_path", "./data/local_storage.db")
                    if cfg.db_url and not cfg.db_url.startswith("sqlite://"):
                        db_path = cfg.db_url
                    client = LocalDatabaseClient(database_path=db_path)
                    return client.ping()

            is_connected = await asyncio.to_thread(_ping_database)
            if is_connected:
                db_status = "connected"
        except Exception as e:
            logger.debug(f"[READINESS] Database ping failed: {e}")
            db_status = "degraded" if cfg.ff_session_memory else "disconnected"
    else:
        db_status = "disconnected"

    # 2. Model configuration check
    has_model_key = bool(getattr(cfg, "model_api_key", None))
    model_status = "configured" if has_model_key else "unconfigured"

    # 3. Session memory check
    memory_status = "active" if cfg.ff_session_memory else "disabled"

    checks = ReadinessDetails(
        database=db_status,
        model=model_status,
        session_memory=memory_status,
    )

    is_ready = (db_status in ("connected", "degraded")) and (
        model_status == "configured"
    )
    overall_status = "ready" if is_ready else "not_ready"

    if not is_ready:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return ReadinessResponse(
        status=overall_status,
        checks=checks,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
