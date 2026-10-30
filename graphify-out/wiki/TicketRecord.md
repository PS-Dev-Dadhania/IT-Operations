# TicketRecord

> 46 nodes · cohesion 0.08

## Key Concepts

- **TicketRecord** (79 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **TicketNotFoundError** (20 connections) — `src/mcp_rag_agent/it_support/tickets/store.py`
- **MemoryTicketStore** (14 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **MemoryTicketStore** (11 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **MemoryTicketStore** (11 connections) — `tests/unit_tests/it_support/test_ticket_api.py`
- **MemoryTicketStore** (11 connections) — `tests/unit_tests/security/test_security_regression.py`
- **MemoryTicketStore** (10 connections) — `tests/unit_tests/api/test_admin_api.py`
- **MemoryTicketStore** (7 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **test_ticket_comments_and_service_methods()** (7 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **.list()** (3 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.list_tickets()** (3 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.add_comment()** (3 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **.get()** (3 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **.update_fields()** (3 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **.get()** (3 connections) — `tests/unit_tests/it_support/test_ticket_api.py`
- **.update_fields()** (3 connections) — `tests/unit_tests/it_support/test_ticket_api.py`
- **.create()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.find_unresolved_duplicate()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.get()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.update_fields()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.create()** (2 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **.find_unresolved_duplicate()** (2 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **.get()** (2 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **.create()** (2 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **.find_unresolved_duplicate()** (2 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- *... and 21 more nodes in this community*

## Relationships

- [tickets/models.py](tickets-models.py.md) (19 shared connections)
- [TicketStore](TicketStore.md) (17 shared connections)
- [TicketService](TicketService.md) (13 shared connections)
- [pytest](pytest.md) (11 shared connections)
- [AdminAPIService](AdminAPIService.md) (5 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (4 shared connections)
- [dependencies.py](dependencies.py.md) (2 shared connections)
- [IncidentRecord](IncidentRecord.md) (2 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [setup_services](setup_services.md) (2 shared connections)
- [test_mcp_it_tools.py](test_mcp_it_tools.py.md) (2 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/tickets/models.py`
- `src/mcp_rag_agent/it_support/tickets/store.py`
- `tests/unit_tests/api/test_admin_api.py`
- `tests/unit_tests/it_support/test_it_agent_flows.py`
- `tests/unit_tests/it_support/test_mcp_it_tools.py`
- `tests/unit_tests/it_support/test_ticket_api.py`
- `tests/unit_tests/it_support/test_tickets.py`
- `tests/unit_tests/security/test_security_regression.py`

## Audit Trail

- EXTRACTED: 126 (78%)
- INFERRED: 35 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*