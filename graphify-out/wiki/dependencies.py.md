# dependencies.py

> 23 nodes · cohesion 0.15

## Key Concepts

- **dependencies.py** (48 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **admin.py** (27 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **admin_service.py** (26 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **AuditService** (18 connections) — `src/mcp_rag_agent/security/audit.py`
- **get_admin_service()** (14 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **require_admin_role()** (12 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **get_current_security_subject()** (9 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **get_it_ticket_service()** (9 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **require_audit_permission()** (9 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **get_config()** (8 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **Request** (8 connections)
- **get_conversation_service()** (5 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **FastAPI dependencies for injecting configuration, application services, and…** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **Extract and validate the authenticated SecuritySubject from request headers or…** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **RBAC dependency requiring IT_ADMIN or SYSTEM_ADMIN role.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **RBAC dependency requiring VIEW_AUDIT_LOGS permission.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **Dependency provider for application configuration.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **Dependency provider for ConversationService, retrieving from app.state.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **Build the IT ticket dependency with the shared MongoDB client abstraction.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **Build the AdminAPIService dependency with shared stores.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **FastAPI routes for IT Administrator operations, ticket dashboards, incidents,…** (1 connections) — `src/mcp_rag_agent/api/routes/admin.py`
- **Admin operations service aggregating ticket analytics, incidents, metrics,…** (1 connections) — `src/mcp_rag_agent/api/services/admin_service.py`
- **Domain service for capturing and querying immutable audit trails.** (1 connections) — `src/mcp_rag_agent/security/audit.py`

## Relationships

- [audit.py](audit.py.md) (14 shared connections)
- [SecuritySubject](SecuritySubject.md) (14 shared connections)
- [AdminAPIService](AdminAPIService.md) (14 shared connections)
- [IncidentRecord](IncidentRecord.md) (12 shared connections)
- [tickets/models.py](tickets-models.py.md) (11 shared connections)
- [typing](typing.md) (8 shared connections)
- [datetime](datetime.md) (8 shared connections)
- [get_admin_evaluation](get_admin_evaluation.md) (8 shared connections)
- [TicketService](TicketService.md) (5 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (4 shared connections)
- [Role](Role.md) (4 shared connections)
- [ChatService](ChatService.md) (4 shared connections)

## Source Files

- `src/mcp_rag_agent/api/dependencies.py`
- `src/mcp_rag_agent/api/routes/admin.py`
- `src/mcp_rag_agent/api/services/admin_service.py`
- `src/mcp_rag_agent/security/audit.py`

## Audit Trail

- EXTRACTED: 154 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*