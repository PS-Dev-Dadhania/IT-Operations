# UserContextRecord

> 13 nodes · cohesion 0.37

## Key Concepts

- **UserContextRecord** (34 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **UserStore** (20 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **._collection()** (7 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **.get()** (6 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **._to_record()** (6 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **.update_fields()** (6 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **.list()** (5 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **Any** (4 connections)
- **.create()** (3 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **.upsert()** (3 connections) — `src/mcp_rag_agent/it_support/users/store.py`
- **BaseModel** (1 connections)
- **Pydantic model representing an enterprise employee / support user.** (1 connections) — `src/mcp_rag_agent/it_support/users/models.py`
- **Persistence store for enterprise user context with in-memory fallback.** (1 connections) — `src/mcp_rag_agent/it_support/users/store.py`

## Relationships

- [UserNotFoundError](UserNotFoundError.md) (12 shared connections)
- [users/store.py](users-store.py.md) (10 shared connections)
- [UserService](UserService.md) (7 shared connections)
- [setup_services](setup_services.md) (4 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (2 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [test_tool_authorization_success_emits_audit_log](test_tool_authorization_success_emits_audit_log.md) (1 shared connections)
- [ServiceStatusChecker](ServiceStatusChecker.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/users/models.py`
- `src/mcp_rag_agent/it_support/users/store.py`

## Audit Trail

- EXTRACTED: 55 (81%)
- INFERRED: 13 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*