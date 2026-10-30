# Role

> 40 nodes · cohesion 0.06

## Key Concepts

- **Role** (51 connections) — `src/mcp_rag_agent/security/rbac.py`
- **test_authorization.py** (25 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_cross_user_device_access_blocked()** (11 connections) — `tests/unit_tests/security/test_security_regression.py`
- **test_cross_user_ticket_isolation_regression()** (11 connections) — `tests/unit_tests/security/test_security_regression.py`
- **fixture** (6 connections)
- **employee_subject()** (4 connections) — `tests/unit_tests/security/test_authorization.py`
- **it_admin_subject()** (4 connections) — `tests/unit_tests/security/test_authorization.py`
- **it_support_subject()** (4 connections) — `tests/unit_tests/security/test_authorization.py`
- **other_employee_subject()** (4 connections) — `tests/unit_tests/security/test_authorization.py`
- **security_analyst_subject()** (4 connections) — `tests/unit_tests/security/test_authorization.py`
- **auth_service()** (3 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_can_check_role_permissions()** (3 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_can_requires_valid_subject()** (3 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_retrieval_document_access_filtering()** (3 connections) — `tests/unit_tests/security/test_authorization.py`
- **asyncio** (3 connections)
- **test_can_execute_tool_create_ticket()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_can_execute_tool_get_user_context()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_can_execute_tool_search_policy()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_can_execute_tool_unknown_tool()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_device_context_resource_authorization()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_ticket_resource_authorization_cross_user_isolation()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_ticket_resource_authorization_employee_own_ticket()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_ticket_resource_authorization_it_support_access()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **test_user_context_resource_authorization()** (2 connections) — `tests/unit_tests/security/test_authorization.py`
- **Authoritative enterprise roles for IT Support Copilot.** (1 connections) — `src/mcp_rag_agent/security/rbac.py`
- *... and 15 more nodes in this community*

## Relationships

- [SecuritySubject](SecuritySubject.md) (20 shared connections)
- [RiskLevel](RiskLevel.md) (7 shared connections)
- [pydantic](pydantic.md) (7 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (5 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (5 shared connections)
- [dependencies.py](dependencies.py.md) (4 shared connections)
- [audit.py](audit.py.md) (4 shared connections)
- [test_approval.py](test_approval.py.md) (4 shared connections)
- [DeviceRecord](DeviceRecord.md) (3 shared connections)
- [approval.py](approval.py.md) (2 shared connections)
- [test_tool_authorization_success_emits_audit_log](test_tool_authorization_success_emits_audit_log.md) (2 shared connections)
- [TestTypedToolInterface](TestTypedToolInterface.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/security/rbac.py`
- `tests/unit_tests/security/test_authorization.py`
- `tests/unit_tests/security/test_security_regression.py`

## Audit Trail

- EXTRACTED: 67 (54%)
- INFERRED: 57 (46%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*