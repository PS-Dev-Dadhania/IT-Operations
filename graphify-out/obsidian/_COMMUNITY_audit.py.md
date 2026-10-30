---
type: community
cohesion: 0.11
members: 27
---

# audit.py

**Cohesion:** 0.11 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-__init__()_30]] - code - src/mcp_rag_agent/security/audit.py
- [[dot-__init__()_31]] - code - src/mcp_rag_agent/security/audit.py
- [[dot-_collection()_3]] - code - src/mcp_rag_agent/security/audit.py
- [[dot-insert()]] - code - src/mcp_rag_agent/security/audit.py
- [[dot-log_event()]] - code - src/mcp_rag_agent/security/audit.py
- [[dot-query()]] - code - src/mcp_rag_agent/security/audit.py
- [[dot-query_events()]] - code - src/mcp_rag_agent/security/audit.py
- [[Any_15]] - code
- [[Any_16]] - code
- [[AuditEvent]] - code - src/mcp_rag_agent/security/audit.py
- [[AuditStore]] - code - src/mcp_rag_agent/security/audit.py
- [[BaseModel_14]] - code
- [[Create and persist a sanitized audit event.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[Mask credentials, API keys, passwords, bearer tokens, and connection strings.]] - rationale - src/mcp_rag_agent/core/log_setup.py
- [[MongoDB client and semantic search modules.]] - rationale - src/mcp_rag_agent/mongodb/__init__.py
- [[MongoDB-backed structured audit logging service for enterprise IT operations.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[Persistence store for security audit records.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[Pydantic model representing an immutable security audit event.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[Query historical audit events.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[Recursively mask secrets and remove private credential fields.]] - rationale - src/mcp_rag_agent/security/audit.py
- [[_get_default_seed_audits()]] - code - src/mcp_rag_agent/security/audit.py
- [[_sanitize_details()]] - code - src/mcp_rag_agent/security/audit.py
- [[_utc_now()_7]] - code - src/mcp_rag_agent/security/audit.py
- [[audit.py]] - code - src/mcp_rag_agent/security/audit.py
- [[datetime_7]] - code
- [[mask_sensitive()_1]] - code - src/mcp_rag_agent/core/log_setup.py
- [[mcp_rag_agentmongodb__init__.py]] - code - src/mcp_rag_agent/mongodb/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/auditpy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_dependencies.py]]
- 8 edges to [[_COMMUNITY_typing]]
- 5 edges to [[_COMMUNITY_RiskLevel]]
- 4 edges to [[_COMMUNITY_Role]]
- 4 edges to [[_COMMUNITY_SecuritySubject]]
- 3 edges to [[_COMMUNITY_AdminAPIService]]
- 3 edges to [[_COMMUNITY_IncidentRecord]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 1 edge to [[_COMMUNITY_dot-run]]
- 1 edge to [[_COMMUNITY_get_checkpointer]]
- 1 edge to [[_COMMUNITY_TestStructuredLoggingAndRedaction]]
- 1 edge to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_approval.py]]
- 1 edge to [[_COMMUNITY_ServiceStatusRecord]]
- 1 edge to [[_COMMUNITY_DeviceRecord]]
- 1 edge to [[_COMMUNITY_usersstore.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[mcp_rag_agentmongodb__init__.py]] - degree 11, connects to 8 communities
- [[audit.py]] - degree 22, connects to 7 communities
- [[AuditEvent]] - degree 19, connects to 6 communities
- [[AuditStore]] - degree 15, connects to 6 communities
- [[mask_sensitive()_1]] - degree 10, connects to 5 communities