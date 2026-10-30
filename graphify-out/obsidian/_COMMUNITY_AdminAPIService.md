---
type: community
cohesion: 0.12
members: 22
---

# AdminAPIService

**Cohesion:** 0.12 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_35]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[dot-get_audit_logs()]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[dot-get_ticket()]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[dot-list_incidents()]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[dot-list_tickets()_1]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[AdminAPIService]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[Enterprise Admin API Service handling tickets, incidents, evaluation, and audit…]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[Fast, low-overhead liveness check confirming the HTTP service is running.]] - rationale - src/mcp_rag_agent/api/routes/health.py
- [[Fetch sanitized security audit log stream.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[List active or all incidents.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[Path_5]] - code
- [[Query tickets with optional operational filters.]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[Retrieve active and historical incidents. Requires IT_ADMIN or SYSTEM_ADMIN…]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[Retrieve filtered tickets. Requires IT_ADMIN or SYSTEM_ADMIN role.]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[Retrieve sanitized security audit logs. Requires VIEW_AUDIT_LOGS permission.]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[Retrieve ticket details. Requires IT_ADMIN or SYSTEM_ADMIN role.]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[get()]] - code - tests/unit_tests/security/test_audit.py
- [[get_admin_audit_logs()]] - code - src/mcp_rag_agent/api/routes/admin.py
- [[get_admin_ticket()]] - code - src/mcp_rag_agent/api/routes/admin.py
- [[health_check()]] - code - src/mcp_rag_agent/api/routes/health.py
- [[list_admin_incidents()]] - code - src/mcp_rag_agent/api/routes/admin.py
- [[list_admin_tickets()]] - code - src/mcp_rag_agent/api/routes/admin.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AdminAPIService
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_dependencies.py]]
- 7 edges to [[_COMMUNITY_IncidentRecord]]
- 6 edges to [[_COMMUNITY_get_admin_evaluation]]
- 5 edges to [[_COMMUNITY_TicketRecord]]
- 4 edges to [[_COMMUNITY_SecuritySubject]]
- 3 edges to [[_COMMUNITY_audit.py]]
- 3 edges to [[_COMMUNITY_TicketService]]
- 3 edges to [[_COMMUNITY_datetime]]
- 2 edges to [[_COMMUNITY_ConversationService]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]

## Top bridge nodes
- [[AdminAPIService]] - degree 27, connects to 6 communities
- [[get()]] - degree 12, connects to 5 communities
- [[get_admin_audit_logs()]] - degree 8, connects to 3 communities
- [[get_admin_ticket()]] - degree 8, connects to 3 communities
- [[list_admin_incidents()]] - degree 8, connects to 3 communities