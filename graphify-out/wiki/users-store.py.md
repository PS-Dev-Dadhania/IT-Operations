# users/store.py

> 18 nodes · cohesion 0.21

## Key Concepts

- **users/store.py** (14 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **users/models.py** (13 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **SupportTier** (12 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **UserStatus** (12 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **users/__init__.py** (11 connections) — `src/mcp_rag_agent/it_support/users/__init__.py`
- **users/service.py** (9 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **get_seed_users()** (5 connections) — `scripts/seed_it_operations_data.py`
- **_get_default_seed_users()** (5 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **test_user_model_instantiation_and_validation()** (4 connections) — `tests/unit_tests/it_support/test_users.py`
- **Enum** (3 connections)
- **.__init__()** (3 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **datetime** (2 connections)
- **str** (2 connections)
- **_utc_now()** (2 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **Public user context exports for IT support operations.** (1 connections) — `src/mcp_rag_agent/it_support/users/__init__.py`
- **User domain models and typed schemas for IT support operations.** (1 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **User domain service for fetching and managing user context.** (1 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **MongoDB persistence adapter for users with in-memory fallback support.** (1 connections) — `src/mcp_rag_agent/it_support/users/store.py`

## Relationships

- [UserContextRecord](UserContextRecord.md) (10 shared connections)
- [UserNotFoundError](UserNotFoundError.md) (7 shared connections)
- [typing](typing.md) (5 shared connections)
- [setup_services](setup_services.md) (4 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (3 shared connections)
- [UserService](UserService.md) (2 shared connections)
- [ServiceStatusChecker](ServiceStatusChecker.md) (1 shared connections)
- [test_mcp_it_tools.py](test_mcp_it_tools.py.md) (1 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (1 shared connections)
- [pydantic](pydantic.md) (1 shared connections)
- [audit.py](audit.py.md) (1 shared connections)
- [datetime](datetime.md) (1 shared connections)

## Source Files

- `scripts/seed_it_operations_data.py`
- `src/mcp_rag_agent/it_support/users/__init__.py`
- `src/mcp_rag_agent/it_support/users/models.py`
- `src/mcp_rag_agent/it_support/users/service.py`
- `src/mcp_rag_agent/it_support/users/store.py`
- `tests/unit_tests/it_support/test_users.py`

## Audit Trail

- EXTRACTED: 56 (81%)
- INFERRED: 13 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*