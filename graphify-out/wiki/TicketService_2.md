# TicketService

> God node · 38 connections · `src/mcp_rag_agent/it_support/tickets/service.py`

**Community:** [TicketService](TicketService.md)

## Connections by Relation

### calls
- get_admin_service() `EXTRACTED`
- get_it_ticket_service() `EXTRACTED`
- get_ticket_service() `EXTRACTED`

### contains
- tickets/service.py `EXTRACTED`

### imports
- [mcp_server/tools.py](mcp_server-tools.py.md) `EXTRACTED`
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) `EXTRACTED`
- [dependencies.py](dependencies.py.md) `EXTRACTED`
- admin_service.py `EXTRACTED`
- tickets/__init__.py `EXTRACTED`
- it_ticket_service.py `EXTRACTED`

### method
- .create_ticket() `EXTRACTED`
- .transition_status() `EXTRACTED`
- .update_fields() `EXTRACTED`
- .add_comment() `EXTRACTED`
- .__init__() `EXTRACTED`
- .get_ticket() `EXTRACTED`
- .list_tickets() `EXTRACTED`
- .assign_team() `EXTRACTED`

### references
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- [TicketRecord](TicketRecord.md) `INFERRED`
- [TicketStore](TicketStore.md) `INFERRED`
- [AdminAPIService](AdminAPIService.md) `INFERRED`
- TicketLifecycleStatus `INFERRED`
- test_setup() `INFERRED`
- TicketCreate `INFERRED`
- ITTicketAPIService `INFERRED`
- setup_services() `INFERRED`
- setup_services() `INFERRED`
- TicketComment `INFERRED`
- TicketOperationResult `INFERRED`
- test_cross_user_ticket_isolation_regression() `INFERRED`
- _build_test_client() `INFERRED`
- test_invalid_lifecycle_transition_is_rejected() `INFERRED`
- test_ticket_comments_and_service_methods() `INFERRED`
- test_escalation_is_allowed_only_from_open_or_in_progress() `INFERRED`
- test_lifecycle_allows_only_deterministic_transitions() `INFERRED`
- test_create_and_duplicate_detection() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*