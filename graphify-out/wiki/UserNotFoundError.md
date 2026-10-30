# UserNotFoundError

> 21 nodes · cohesion 0.14

## Key Concepts

- **UserNotFoundError** (20 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **test_users.py** (13 connections) — `tests/unit_tests/it_support/test_users.py`
- **MemoryUserStore** (13 connections) — `tests/unit_tests/it_support/test_users.py`
- **_sample_user()** (7 connections) — `tests/unit_tests/it_support/test_users.py`
- **MemoryUserStore** (6 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **test_user_service_missing_user_raises_not_found()** (5 connections) — `tests/unit_tests/it_support/test_users.py`
- **test_user_store_mongodb_adapter()** (5 connections) — `tests/unit_tests/it_support/test_users.py`
- **test_user_service_invalid_id_raises_value_error()** (4 connections) — `tests/unit_tests/it_support/test_users.py`
- **test_user_service_valid_lookup()** (4 connections) — `tests/unit_tests/it_support/test_users.py`
- **.get()** (3 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **.get()** (3 connections) — `tests/unit_tests/it_support/test_users.py`
- **.update_fields()** (3 connections) — `tests/unit_tests/it_support/test_users.py`
- **.create()** (2 connections) — `tests/unit_tests/it_support/test_users.py`
- **.upsert()** (2 connections) — `tests/unit_tests/it_support/test_users.py`
- **KeyError** (1 connections)
- **Raised when a requested user cannot be found.** (1 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **.__init__()** (1 connections) — `tests/unit_tests/it_support/test_it_agent_flows.py`
- **.__init__()** (1 connections) — `tests/unit_tests/it_support/test_users.py`
- **.list()** (1 connections) — `tests/unit_tests/it_support/test_users.py`
- **Unit tests for user context models, store, and domain service.** (1 connections) — `tests/unit_tests/it_support/test_users.py`
- **In-memory test double for UserStore.** (1 connections) — `tests/unit_tests/it_support/test_users.py`

## Relationships

- [UserContextRecord](UserContextRecord.md) (12 shared connections)
- [users/store.py](users-store.py.md) (7 shared connections)
- [test_mcp_it_tools.py](test_mcp_it_tools.py.md) (4 shared connections)
- [pytest](pytest.md) (4 shared connections)
- [setup_services](setup_services.md) (3 shared connections)
- [UserService](UserService.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (1 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/users/store.py`
- `tests/unit_tests/it_support/test_it_agent_flows.py`
- `tests/unit_tests/it_support/test_users.py`

## Audit Trail

- EXTRACTED: 48 (72%)
- INFERRED: 19 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*