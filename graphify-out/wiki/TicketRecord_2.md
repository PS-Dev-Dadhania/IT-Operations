# TicketRecord

> God node · 79 connections · `src/mcp_rag_agent/it_support/tickets/models.py`

**Community:** [TicketRecord](TicketRecord.md)

## Connections by Relation

### calls
- _get_default_seed_tickets() `EXTRACTED`
- .create_ticket() `EXTRACTED`

### contains
- [tickets/models.py](tickets-models.py.md) `EXTRACTED`

### imports
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) `EXTRACTED`
- admin.py `EXTRACTED`
- admin_service.py `EXTRACTED`
- tickets/store.py `EXTRACTED`
- tickets/service.py `EXTRACTED`
- tickets/__init__.py `EXTRACTED`
- it_ticket_service.py `EXTRACTED`
- schemas/it_tickets.py `EXTRACTED`

### inherits
- TicketCreate `EXTRACTED`

### references
- .patch() `EXTRACTED`
- patch_ticket() `EXTRACTED`
- .update_fields() `EXTRACTED`
- get_ticket() `EXTRACTED`
- .add_comment() `EXTRACTED`
- .get() `EXTRACTED`
- ._to_record() `EXTRACTED`
- .list() `EXTRACTED`
- .list_tickets() `EXTRACTED`
- .list_tickets() `EXTRACTED`
- .get() `EXTRACTED`
- .transition_status() `EXTRACTED`
- .find_unresolved_duplicate() `EXTRACTED`
- .update() `EXTRACTED`
- .update_status() `EXTRACTED`
- .get_ticket() `EXTRACTED`
- .list() `EXTRACTED`
- .list_tickets() `EXTRACTED`
- .add_comment() `EXTRACTED`
- .update_fields() `EXTRACTED`
- *…and 30 more `references` connection(s) not listed (lowest-degree first to go)*

### uses
- [TicketService](TicketService.md) `INFERRED`
- [TicketStore](TicketStore.md) `INFERRED`
- [AdminAPIService](AdminAPIService.md) `INFERRED`
- test_setup() `INFERRED`
- ITTicketAPIService `INFERRED`
- MemoryTicketStore `INFERRED`
- MemoryTicketStore `INFERRED`
- MemoryTicketStore `INFERRED`
- MemoryTicketStore `INFERRED`
- MemoryTicketStore `INFERRED`
- list_admin_tickets() `INFERRED`
- get_admin_ticket() `INFERRED`
- MemoryTicketStore `INFERRED`
- test_ticket_comments_and_service_methods() `INFERRED`
- test_ticket_store_queries_and_not_found_handling() `INFERRED`
- test_mongodb_failure_is_not_silenced() `INFERRED`
- test_ticket_store_crud_uses_shared_mongodb_client() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*