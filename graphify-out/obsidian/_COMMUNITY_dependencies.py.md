---
type: community
cohesion: 0.15
members: 23
---

# dependencies.py

**Cohesion:** 0.15 - loosely connected
**Members:** 23 nodes

## Members
- [[Admin operations service aggregating ticket analytics, incidents, metrics,…]] - rationale - src/mcp_rag_agent/api/services/admin_service.py
- [[AuditService]] - code - src/mcp_rag_agent/security/audit.py
- [[Build the AdminAPIService dependency with shared stores.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[Build the IT ticket dependency with the shared MongoDB client abstraction.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[Dependency provider for ConversationService, retrieving from app.state.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[Dependency provider for application configuration.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[Domain service for capturing and querying immutable audit trails.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[Extract and validate the authenticated SecuritySubject from request headers or…]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[FastAPI dependencies for injecting configuration, application services, and…]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[FastAPI routes for IT Administrator operations, ticket dashboards, incidents,…]] - rationale - src/mcp_rag_agent/api/routes/admin.py
- [[RBAC dependency requiring IT_ADMIN or SYSTEM_ADMIN role.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[RBAC dependency requiring VIEW_AUDIT_LOGS permission.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[Request_1]] - code
- [[admin.py]] - code - src/mcp_rag_agent/api/routes/admin.py
- [[admin_service.py]] - code - src/mcp_rag_agent/api/services/admin_service.py
- [[dependencies.py]] - code - src/mcp_rag_agent/api/dependencies.py
- [[get_admin_service()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[get_config()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[get_conversation_service()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[get_current_security_subject()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[get_it_ticket_service()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[require_admin_role()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[require_audit_permission()]] - code - src/mcp_rag_agent/api/dependencies.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/dependenciespy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_audit.py]]
- 14 edges to [[_COMMUNITY_AdminAPIService]]
- 14 edges to [[_COMMUNITY_SecuritySubject]]
- 12 edges to [[_COMMUNITY_IncidentRecord]]
- 11 edges to [[_COMMUNITY_ticketsmodels.py]]
- 8 edges to [[_COMMUNITY_typing]]
- 8 edges to [[_COMMUNITY_get_admin_evaluation]]
- 8 edges to [[_COMMUNITY_datetime]]
- 5 edges to [[_COMMUNITY_TicketService]]
- 4 edges to [[_COMMUNITY_Role]]
- 4 edges to [[_COMMUNITY_ChatService]]
- 4 edges to [[_COMMUNITY_mcp_servertools.py]]
- 3 edges to [[_COMMUNITY_ConversationService]]
- 3 edges to [[_COMMUNITY_TicketStore]]
- 2 edges to [[_COMMUNITY_TicketRecord]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_IncidentStore]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_RiskLevel]]
- 1 edge to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_test_it_evaluation.py]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[dependencies.py]] - degree 48, connects to 16 communities
- [[admin_service.py]] - degree 26, connects to 13 communities
- [[admin.py]] - degree 27, connects to 9 communities
- [[AuditService]] - degree 18, connects to 9 communities
- [[get_admin_service()]] - degree 14, connects to 7 communities