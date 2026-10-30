# UserService

> 12 nodes · cohesion 0.17

## Key Concepts

- **UserService** (19 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **.list_users()** (4 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **.create_user()** (3 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **.get_user_context()** (3 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **.upsert_user()** (3 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **Any** (1 connections)
- **Domain service managing user context lookups and updates.** (1 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **Retrieve user context by user_id with validation. Args: user_id: Unique…** (1 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **Create or register a user record.** (1 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **Upsert a user record (idempotent seeding).** (1 connections) — `src/mcp_rag_agent/it_support/users/service.py`
- **List users matching optional filter criteria.** (1 connections) — `src/mcp_rag_agent/it_support/users/service.py`

## Relationships

- [UserContextRecord](UserContextRecord.md) (7 shared connections)
- [UserNotFoundError](UserNotFoundError.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [users/store.py](users-store.py.md) (2 shared connections)
- [setup_services](setup_services.md) (2 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (1 shared connections)
- [test_tool_authorization_success_emits_audit_log](test_tool_authorization_success_emits_audit_log.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/users/service.py`

## Audit Trail

- EXTRACTED: 21 (72%)
- INFERRED: 8 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*