# AdminAPIService

> 22 nodes · cohesion 0.12

## Key Concepts

- **AdminAPIService** (27 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **get()** (12 connections) — `tests/unit_tests/security/test_audit.py`
- **get_admin_audit_logs()** (8 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **get_admin_ticket()** (8 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **list_admin_incidents()** (8 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **list_admin_tickets()** (8 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **.__init__()** (5 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **health_check()** (4 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **.get_audit_logs()** (4 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **.list_incidents()** (4 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **.list_tickets()** (4 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **.get_ticket()** (3 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Retrieve sanitized security audit logs. Requires VIEW_AUDIT_LOGS permission.** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Retrieve filtered tickets. Requires IT_ADMIN or SYSTEM_ADMIN role.** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Retrieve ticket details. Requires IT_ADMIN or SYSTEM_ADMIN role.** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Retrieve active and historical incidents. Requires IT_ADMIN or SYSTEM_ADMIN…** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Fast, low-overhead liveness check confirming the HTTP service is running.** (1 connections) — `src/mcp_rag_agent/api/routes/health.py`
- **Path** (1 connections)
- **List active or all incidents.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Fetch sanitized security audit log stream.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Enterprise Admin API Service handling tickets, incidents, evaluation, and audit…** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Query tickets with optional operational filters.** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`

## Relationships

- [dependencies.py](dependencies.py.md) (14 shared connections)
- [IncidentRecord](IncidentRecord.md) (7 shared connections)
- [get_admin_evaluation](get_admin_evaluation.md) (6 shared connections)
- [TicketRecord](TicketRecord.md) (5 shared connections)
- [SecuritySubject](SecuritySubject.md) (4 shared connections)
- [audit.py](audit.py.md) (3 shared connections)
- [datetime](datetime.md) (3 shared connections)
- [TicketService](TicketService.md) (3 shared connections)
- [ConversationService](ConversationService.md) (2 shared connections)
- [tickets/models.py](tickets-models.py.md) (1 shared connections)
- [test_tool_authorization_success_emits_audit_log](test_tool_authorization_success_emits_audit_log.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/routes/admin.py`
- `src/mcp_rag_agent/api/routes/health.py`
- `src/mcp_rag_agent/api/services/admin_service.py`
- `tests/unit_tests/security/test_audit.py`

## Audit Trail

- EXTRACTED: 49 (64%)
- INFERRED: 28 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*