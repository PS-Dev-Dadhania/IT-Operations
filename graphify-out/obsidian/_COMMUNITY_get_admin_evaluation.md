---
type: community
cohesion: 0.19
members: 13
---

# get_admin_evaluation

**Cohesion:** 0.19 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-get_evaluation_summary()]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[dot-get_metrics()]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[AdminEvaluationSummary]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[BaseModel_21]] - code
- [[Compute live aggregated KPIs across tickets, incidents, and telemetry.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[Load latest evaluation run artifacts.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[OperationalKPIs]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[Real-time IT operational summary metrics.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[Retrieve latest evaluation benchmark metrics. Requires IT_ADMIN or SYSTEM_ADMIN…]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[Retrieve operational KPIs. Requires IT_ADMIN or SYSTEM_ADMIN role.]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[Summary of latest evaluation benchmark runs.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[get_admin_evaluation()]] - code - src/mcp_rag_agent/api/routes/admin.py
- [[get_admin_metrics()]] - code - src/mcp_rag_agent/api/routes/admin.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_admin_evaluation
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_dependencies.py]]
- 6 edges to [[_COMMUNITY_AdminAPIService]]
- 2 edges to [[_COMMUNITY_SecuritySubject]]

## Top bridge nodes
- [[get_admin_evaluation()]] - degree 8, connects to 3 communities
- [[get_admin_metrics()]] - degree 8, connects to 3 communities
- [[AdminEvaluationSummary]] - degree 6, connects to 1 community
- [[OperationalKPIs]] - degree 6, connects to 1 community
- [[dot-get_evaluation_summary()]] - degree 5, connects to 1 community