# test_tool_authorization_success_emits_audit_log

> 14 nodes · cohesion 0.18

## Key Concepts

- **test_tool_authorization_success_emits_audit_log()** (15 connections) — `tests/unit_tests/security/test_audit.py`
- **setup_security_environment()** (10 connections) — `tests/unit_tests/security/test_security_regression.py`
- **test_tool_authorization_denial_emits_audit_log()** (9 connections) — `tests/unit_tests/security/test_audit.py`
- **reset_it_services()** (6 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **set_audit_service()** (6 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **asyncio** (2 connections)
- **Reset cached IT domain service and security instances.** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Set or override the AuditService instance.** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Verify tool authorization rejection creates a DENIED audit record.** (1 connections) — `tests/unit_tests/security/test_audit.py`
- **Verify authorized tool execution creates an AUTHORIZED audit record.** (1 connections) — `tests/unit_tests/security/test_audit.py`
- **create()** (1 connections) — `tests/unit_tests/security/test_audit.py`
- **__init__()** (1 connections) — `tests/unit_tests/security/test_audit.py`
- **fixture** (1 connections)
- **Ensure clean services and memory stores for regression testing.** (1 connections) — `tests/unit_tests/security/test_security_regression.py`

## Relationships

- [mcp_server/tools.py](mcp_server-tools.py.md) (8 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (3 shared connections)
- [setup_services](setup_services.md) (2 shared connections)
- [Role](Role.md) (2 shared connections)
- [SecuritySubject](SecuritySubject.md) (2 shared connections)
- [approval.py](approval.py.md) (2 shared connections)
- [AdminAPIService](AdminAPIService.md) (1 shared connections)
- [UserContextRecord](UserContextRecord.md) (1 shared connections)
- [UserService](UserService.md) (1 shared connections)
- [audit.py](audit.py.md) (1 shared connections)
- [dependencies.py](dependencies.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/mcp_server/tools.py`
- `tests/unit_tests/security/test_audit.py`
- `tests/unit_tests/security/test_security_regression.py`

## Audit Trail

- EXTRACTED: 18 (45%)
- INFERRED: 22 (55%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*