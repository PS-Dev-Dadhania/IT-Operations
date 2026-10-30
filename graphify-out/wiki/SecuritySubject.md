# SecuritySubject

> 48 nodes · cohesion 0.09

## Key Concepts

- **SecuritySubject** (49 connections) — `src/mcp_rag_agent/security/rbac.py`
- **Permission** (28 connections) — `src/mcp_rag_agent/security/rbac.py`
- **mcp_rag_agent/security/__init__.py** (26 connections) — `src/mcp_rag_agent/security/__init__.py`
- **rbac.py** (21 connections) — `src/mcp_rag_agent/security/rbac.py`
- **AuthorizationService** (17 connections) — `src/mcp_rag_agent/security/authorization.py`
- **has_permission()** (15 connections) — `src/mcp_rag_agent/security/rbac.py`
- **authorization.py** (12 connections) — `src/mcp_rag_agent/security/authorization.py`
- **AuthorizationDecision** (12 connections) — `src/mcp_rag_agent/security/authorization.py`
- **get_role_permissions()** (11 connections) — `src/mcp_rag_agent/security/rbac.py`
- **.can()** (9 connections) — `src/mcp_rag_agent/security/authorization.py`
- **.can_execute_tool()** (9 connections) — `src/mcp_rag_agent/security/authorization.py`
- **.can_access_device()** (8 connections) — `src/mcp_rag_agent/security/authorization.py`
- **.can_access_user()** (8 connections) — `src/mcp_rag_agent/security/authorization.py`
- **.allow()** (7 connections) — `src/mcp_rag_agent/security/authorization.py`
- **.deny()** (7 connections) — `src/mcp_rag_agent/security/authorization.py`
- **.can_access_ticket()** (7 connections) — `src/mcp_rag_agent/security/authorization.py`
- **test_subject_contextvars_tracking()** (7 connections) — `tests/unit_tests/security/test_rbac.py`
- **test_employee_attempting_admin_operations_denied()** (6 connections) — `tests/unit_tests/security/test_security_regression.py`
- **set_current_subject()** (5 connections) — `src/mcp_rag_agent/security/rbac.py`
- **with_security_subject()** (5 connections) — `src/mcp_rag_agent/security/rbac.py`
- **test_employee_role_permissions()** (5 connections) — `tests/unit_tests/security/test_rbac.py`
- **test_it_support_role_permissions()** (5 connections) — `tests/unit_tests/security/test_rbac.py`
- **.filter_documents_for_subject()** (4 connections) — `src/mcp_rag_agent/security/authorization.py`
- **Any** (4 connections)
- **contextvars** (2 connections)
- *... and 23 more nodes in this community*

## Relationships

- [Role](Role.md) (20 shared connections)
- [approval.py](approval.py.md) (18 shared connections)
- [pydantic](pydantic.md) (17 shared connections)
- [dependencies.py](dependencies.py.md) (14 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (6 shared connections)
- [RiskLevel](RiskLevel.md) (6 shared connections)
- [test_approval.py](test_approval.py.md) (5 shared connections)
- [audit.py](audit.py.md) (4 shared connections)
- [AdminAPIService](AdminAPIService.md) (4 shared connections)
- [ObservabilityTracer](ObservabilityTracer.md) (2 shared connections)
- [typing](typing.md) (2 shared connections)
- [get_admin_evaluation](get_admin_evaluation.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/security/__init__.py`
- `src/mcp_rag_agent/security/authorization.py`
- `src/mcp_rag_agent/security/rbac.py`
- `tests/unit_tests/security/test_rbac.py`
- `tests/unit_tests/security/test_security_regression.py`

## Audit Trail

- EXTRACTED: 148 (71%)
- INFERRED: 60 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*