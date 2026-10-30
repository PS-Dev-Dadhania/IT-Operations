# datetime

> 21 nodes · cohesion 0.14

## Key Concepts

- **datetime** (27 connections)
- **conversations.py** (17 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **routes/health.py** (17 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **FastAPI** (10 connections)
- **readiness_check()** (9 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **schemas/health.py** (9 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **routes/__init__.py** (8 connections) — `src/mcp_rag_agent/api/routes/__init__.py`
- **HealthResponse** (6 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **ReadinessDetails** (6 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **ReadinessResponse** (6 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **BaseModel** (3 connections)
- **Conversation session management endpoints.** (1 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **Response** (1 connections)
- **Health and readiness diagnostic endpoints.** (1 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **Deep readiness probe verifying database connectivity and model configuration.** (1 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **_ping_mongo()** (1 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **API router aggregation for v1 endpoints.** (1 connections) — `src/mcp_rag_agent/api/routes/__init__.py`
- **Pydantic schemas for health and readiness endpoints.** (1 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **Response model for liveness check (/api/v1/health).** (1 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **Component-level readiness diagnostic status.** (1 connections) — `src/mcp_rag_agent/api/schemas/health.py`
- **Response model for deep readiness probe (/api/v1/ready).** (1 connections) — `src/mcp_rag_agent/api/schemas/health.py`

## Relationships

- [ConversationService](ConversationService.md) (16 shared connections)
- [typing](typing.md) (10 shared connections)
- [dependencies.py](dependencies.py.md) (8 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (4 shared connections)
- [tickets/models.py](tickets-models.py.md) (3 shared connections)
- [AdminAPIService](AdminAPIService.md) (3 shared connections)
- [AnswerGenerator](AnswerGenerator.md) (2 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (2 shared connections)
- [ServiceStatusRecord](ServiceStatusRecord.md) (2 shared connections)
- [agent/models.py](agent-models.py.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [Config](Config.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/api/routes/__init__.py`
- `src/mcp_rag_agent/api/routes/conversations.py`
- `src/mcp_rag_agent/api/routes/health.py`
- `src/mcp_rag_agent/api/schemas/health.py`

## Audit Trail

- EXTRACTED: 93 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*