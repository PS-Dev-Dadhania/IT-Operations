# get_admin_evaluation

> 13 nodes · cohesion 0.19

## Key Concepts

- **get_admin_evaluation()** (8 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **get_admin_metrics()** (8 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **AdminEvaluationSummary** (6 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **OperationalKPIs** (6 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **.get_evaluation_summary()** (5 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **.get_metrics()** (5 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **BaseModel** (2 connections)
- **Retrieve operational KPIs. Requires IT_ADMIN or SYSTEM_ADMIN role.** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Retrieve latest evaluation benchmark metrics. Requires IT_ADMIN or SYSTEM_ADMIN…** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Compute live aggregated KPIs across tickets, incidents, and telemetry.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Load latest evaluation run artifacts.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Real-time IT operational summary metrics.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Summary of latest evaluation benchmark runs.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`

## Relationships

- [dependencies.py](dependencies.py.md) (8 shared connections)
- [AdminAPIService](AdminAPIService.md) (6 shared connections)
- [SecuritySubject](SecuritySubject.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/api/routes/admin.py`
- `src/mcp_rag_agent/api/services/admin_service.py`

## Audit Trail

- EXTRACTED: 23 (74%)
- INFERRED: 8 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*