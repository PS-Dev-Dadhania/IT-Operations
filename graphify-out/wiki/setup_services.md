# setup_services

> 18 nodes · cohesion 0.13

## Key Concepts

- **setup_services()** (18 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **setup_services()** (18 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **reset_retriever()** (7 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **set_device_service()** (6 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **set_ticket_service()** (6 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **set_user_service()** (6 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **MemoryUserStore** (6 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **.get()** (3 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **.teardown_method()** (3 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **.teardown_method()** (2 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Reset the cached retriever, IT services, and MongoDB client instances.** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Set or override the UserService instance.** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Set or override the DeviceService instance.** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Set or override the TicketService instance.** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **fixture** (1 connections)
- **.__init__()** (1 connections) — `tests/unit_tests/it_support/test_mcp_it_tools.py`
- **fixture** (1 connections)
- **Clean up retriever singleton after each test.** (1 connections) — `tests/unit_tests/test_tools_and_retriever.py`

## Relationships

- [mcp_server/tools.py](mcp_server-tools.py.md) (9 shared connections)
- [DeviceRecord](DeviceRecord.md) (6 shared connections)
- [UserContextRecord](UserContextRecord.md) (4 shared connections)
- [users/store.py](users-store.py.md) (4 shared connections)
- [UserNotFoundError](UserNotFoundError.md) (3 shared connections)
- [test_mcp_it_tools.py](test_mcp_it_tools.py.md) (3 shared connections)
- [test_tool_authorization_success_emits_audit_log](test_tool_authorization_success_emits_audit_log.md) (2 shared connections)
- [Role](Role.md) (2 shared connections)
- [TicketRecord](TicketRecord.md) (2 shared connections)
- [ServiceStatusChecker](ServiceStatusChecker.md) (2 shared connections)
- [TicketService](TicketService.md) (2 shared connections)
- [UserService](UserService.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/mcp_server/tools.py`
- `tests/unit_tests/it_support/test_it_agent_flows.py`
- `tests/unit_tests/it_support/test_mcp_it_tools.py`
- `tests/unit_tests/test_agent_architecture.py`
- `tests/unit_tests/test_tools_and_retriever.py`

## Audit Trail

- EXTRACTED: 29 (46%)
- INFERRED: 34 (54%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*