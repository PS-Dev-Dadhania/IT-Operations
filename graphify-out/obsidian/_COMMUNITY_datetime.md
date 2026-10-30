---
type: community
cohesion: 0.14
members: 21
---

# datetime

**Cohesion:** 0.14 - loosely connected
**Members:** 21 nodes

## Members
- [[API router aggregation for v1 endpoints.]] - rationale - src/mcp_rag_agent/api/routes/__init__.py
- [[BaseModel_18]] - code
- [[Component-level readiness diagnostic status.]] - rationale - src/mcp_rag_agent/api/schemas/health.py
- [[Conversation session management endpoints.]] - rationale - src/mcp_rag_agent/api/routes/conversations.py
- [[Deep readiness probe verifying database connectivity and model configuration.]] - rationale - src/mcp_rag_agent/api/routes/health.py
- [[FastAPI]] - code
- [[Health and readiness diagnostic endpoints.]] - rationale - src/mcp_rag_agent/api/routes/health.py
- [[HealthResponse]] - code - src/mcp_rag_agent/api/schemas/health.py
- [[Pydantic schemas for health and readiness endpoints.]] - rationale - src/mcp_rag_agent/api/schemas/health.py
- [[ReadinessDetails]] - code - src/mcp_rag_agent/api/schemas/health.py
- [[ReadinessResponse]] - code - src/mcp_rag_agent/api/schemas/health.py
- [[Response_1]] - code
- [[Response model for deep readiness probe (apiv1ready).]] - rationale - src/mcp_rag_agent/api/schemas/health.py
- [[Response model for liveness check (apiv1health).]] - rationale - src/mcp_rag_agent/api/schemas/health.py
- [[_ping_mongo()]] - code - src/mcp_rag_agent/api/routes/health.py
- [[conversations.py]] - code - src/mcp_rag_agent/api/routes/conversations.py
- [[datetime_9]] - concept
- [[readiness_check()]] - code - src/mcp_rag_agent/api/routes/health.py
- [[routes__init__.py]] - code - src/mcp_rag_agent/api/routes/__init__.py
- [[routeshealth.py]] - code - src/mcp_rag_agent/api/routes/health.py
- [[schemashealth.py]] - code - src/mcp_rag_agent/api/schemas/health.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/datetime
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_ConversationService]]
- 10 edges to [[_COMMUNITY_typing]]
- 8 edges to [[_COMMUNITY_dependencies.py]]
- 4 edges to [[_COMMUNITY_test_admin_api.py]]
- 3 edges to [[_COMMUNITY_AdminAPIService]]
- 3 edges to [[_COMMUNITY_ticketsmodels.py]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 2 edges to [[_COMMUNITY_ServiceStatusRecord]]
- 2 edges to [[_COMMUNITY_AnswerGenerator]]
- 2 edges to [[_COMMUNITY_ChatService]]
- 2 edges to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_delete_conversation]]
- 1 edge to [[_COMMUNITY_eval_runner.py]]
- 1 edge to [[_COMMUNITY_ObservabilityTracer]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_DeviceRecord]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_ingestion__init__.py]]
- 1 edge to [[_COMMUNITY_test_approval.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_usersstore.py]]
- 1 edge to [[_COMMUNITY_metrics_evaluator.py]]

## Top bridge nodes
- [[datetime_9]] - degree 27, connects to 17 communities
- [[FastAPI]] - degree 10, connects to 6 communities
- [[conversations.py]] - degree 17, connects to 4 communities
- [[routeshealth.py]] - degree 17, connects to 4 communities
- [[routes__init__.py]] - degree 8, connects to 4 communities