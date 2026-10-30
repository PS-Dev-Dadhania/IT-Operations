# TicketService

> 15 nodes · cohesion 0.14

## Key Concepts

- **TicketService** (38 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **TicketLifecycleStatus** (24 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **_get_default_seed_tickets()** (6 connections) — `src/mcp_rag_agent/it_support/tickets/store.py`
- **.transition_status()** (4 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.add_comment()** (3 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.update_fields()** (3 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.__init__()** (3 connections) — `src/mcp_rag_agent/it_support/tickets/store.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/api/services/it_ticket_service.py`
- **Enum** (2 connections)
- **.assign_team()** (2 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.get_ticket()** (2 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.list_tickets()** (2 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **str** (1 connections)
- **Update non-lifecycle fields after the API schema has restricted them.** (1 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`

## Relationships

- [tickets/models.py](tickets-models.py.md) (17 shared connections)
- [TicketRecord](TicketRecord.md) (13 shared connections)
- [pytest](pytest.md) (7 shared connections)
- [dependencies.py](dependencies.py.md) (5 shared connections)
- [TicketStore](TicketStore.md) (5 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (4 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (3 shared connections)
- [AdminAPIService](AdminAPIService.md) (3 shared connections)
- [IncidentRecord](IncidentRecord.md) (2 shared connections)
- [setup_services](setup_services.md) (2 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (1 shared connections)
- [Role](Role.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/services/it_ticket_service.py`
- `src/mcp_rag_agent/it_support/tickets/models.py`
- `src/mcp_rag_agent/it_support/tickets/service.py`
- `src/mcp_rag_agent/it_support/tickets/store.py`

## Audit Trail

- EXTRACTED: 49 (61%)
- INFERRED: 31 (39%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*