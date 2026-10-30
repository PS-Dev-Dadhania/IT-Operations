# tickets/models.py

> 38 nodes · cohesion 0.12

## Key Concepts

- **tickets/models.py** (22 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **routes/it_tickets.py** (19 connections) — `src/mcp_rag_agent/api/routes/it_tickets.py`
- **TicketCreate** (19 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **tickets/store.py** (19 connections) — `src/mcp_rag_agent/it_support/tickets/store.py`
- **ITTicketAPIService** (18 connections) — `src/mcp_rag_agent/api/services/it_ticket_service.py`
- **.patch()** (17 connections) — `src/mcp_rag_agent/api/services/it_ticket_service.py`
- **tickets/service.py** (16 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **tickets/__init__.py** (15 connections) — `src/mcp_rag_agent/it_support/tickets/__init__.py`
- **TicketComment** (14 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **it_ticket_service.py** (12 connections) — `src/mcp_rag_agent/api/services/it_ticket_service.py`
- **TicketOperationResult** (12 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **patch_ticket()** (10 connections) — `src/mcp_rag_agent/api/routes/it_tickets.py`
- **TicketPatch** (10 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- **InvalidTicketTransitionError** (10 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **create_ticket()** (9 connections) — `src/mcp_rag_agent/api/routes/it_tickets.py`
- **get_ticket()** (8 connections) — `src/mcp_rag_agent/api/routes/it_tickets.py`
- **schemas/it_tickets.py** (8 connections) — `src/mcp_rag_agent/api/schemas/it_tickets.py`
- **_ensure_enabled()** (5 connections) — `src/mcp_rag_agent/api/routes/it_tickets.py`
- **.create()** (4 connections) — `src/mcp_rag_agent/api/services/it_ticket_service.py`
- **.get()** (4 connections) — `src/mcp_rag_agent/api/services/it_ticket_service.py`
- **BaseModel** (4 connections)
- **.create_ticket()** (4 connections) — `src/mcp_rag_agent/it_support/tickets/service.py`
- **.test_legacy_agent_attribute_issues_deprecation_warning()** (3 connections) — `tests/unit_tests/test_agent_creation.py`
- **datetime** (2 connections)
- **_utc_now()** (2 connections) — `src/mcp_rag_agent/it_support/tickets/models.py`
- *... and 13 more nodes in this community*

## Relationships

- [TicketRecord](TicketRecord.md) (19 shared connections)
- [TicketService](TicketService.md) (17 shared connections)
- [dependencies.py](dependencies.py.md) (11 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (11 shared connections)
- [Config](Config.md) (10 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (6 shared connections)
- [TicketStore](TicketStore.md) (5 shared connections)
- [datetime](datetime.md) (3 shared connections)
- [typing](typing.md) (3 shared connections)
- [ConversationService](ConversationService.md) (3 shared connections)
- [ITCategory](ITCategory.md) (3 shared connections)
- [pytest](pytest.md) (3 shared connections)

## Source Files

- `src/mcp_rag_agent/api/routes/it_tickets.py`
- `src/mcp_rag_agent/api/schemas/it_tickets.py`
- `src/mcp_rag_agent/api/services/it_ticket_service.py`
- `src/mcp_rag_agent/it_support/tickets/__init__.py`
- `src/mcp_rag_agent/it_support/tickets/models.py`
- `src/mcp_rag_agent/it_support/tickets/service.py`
- `src/mcp_rag_agent/it_support/tickets/store.py`
- `tests/unit_tests/test_agent_creation.py`

## Audit Trail

- EXTRACTED: 149 (77%)
- INFERRED: 44 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*