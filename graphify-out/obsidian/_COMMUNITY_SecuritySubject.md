---
type: community
cohesion: 0.09
members: 48
---

# SecuritySubject

**Cohesion:** 0.09 - loosely connected
**Members:** 48 nodes

## Members
- [[dot-allow()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-can()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-can_access_device()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-can_access_ticket()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-can_access_user()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-can_execute_tool()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-deny()]] - code - src/mcp_rag_agent/security/authorization.py
- [[dot-filter_documents_for_subject()]] - code - src/mcp_rag_agent/security/authorization.py
- [[Any_36]] - code
- [[Authoritative granular permissions.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Authorization service providing role-based, resource-level, tool, and retrieval…]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[AuthorizationDecision]] - code - src/mcp_rag_agent/security/authorization.py
- [[AuthorizationService]] - code - src/mcp_rag_agent/security/authorization.py
- [[BaseModel_24]] - code
- [[BaseModel_25]] - code
- [[Check authorization before executing an MCP operational or diagnostic tool.]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Check authorization to access device context.]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Check authorization to access user context.]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Check resource-level authorization for support tickets. Rules - Employees can…]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Check role-level permission.]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Check whether a given role has the requested permission.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Context manager setting active security subject.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Employee attempting admin-only operations is strictly DENIED.]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[Enterprise authorization service for IT operations and support.]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Filter retrieved document chunks BEFORE LLM synthesis based on access level.…]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Permission]] - code - src/mcp_rag_agent/security/rbac.py
- [[Public security, RBAC, authorization, approval, and audit exports.]] - rationale - src/mcp_rag_agent/security/__init__.py
- [[Represents an authenticated callersubject in the system.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Retrieve all granted permissions for a role.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Role-Based Access Control (RBAC) models, roles, permissions, and authoritative…]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[SecuritySubject]] - code - src/mcp_rag_agent/security/rbac.py
- [[Set the active SecuritySubject in contextvars.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Structured result of an authorization evaluation.]] - rationale - src/mcp_rag_agent/security/authorization.py
- [[Test setting and resetting security subject in execution context.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify Employee role has minimal, least-privilege permissions.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify IT Support role permissions.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[authorization.py]] - code - src/mcp_rag_agent/security/authorization.py
- [[contextvars]] - concept
- [[get_role_permissions()]] - code - src/mcp_rag_agent/security/rbac.py
- [[has_permission()]] - code - src/mcp_rag_agent/security/rbac.py
- [[mcp_rag_agentsecurity__init__.py]] - code - src/mcp_rag_agent/security/__init__.py
- [[rbac.py]] - code - src/mcp_rag_agent/security/rbac.py
- [[set_current_subject()]] - code - src/mcp_rag_agent/security/rbac.py
- [[test_employee_attempting_admin_operations_denied()]] - code - tests/unit_tests/security/test_security_regression.py
- [[test_employee_role_permissions()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_it_support_role_permissions()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_subject_contextvars_tracking()]] - code - tests/unit_tests/security/test_rbac.py
- [[with_security_subject()]] - code - src/mcp_rag_agent/security/rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecuritySubject
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Role]]
- 18 edges to [[_COMMUNITY_approval.py]]
- 17 edges to [[_COMMUNITY_pydantic]]
- 14 edges to [[_COMMUNITY_dependencies.py]]
- 6 edges to [[_COMMUNITY_RiskLevel]]
- 6 edges to [[_COMMUNITY_mcp_servertools.py]]
- 5 edges to [[_COMMUNITY_test_approval.py]]
- 4 edges to [[_COMMUNITY_audit.py]]
- 4 edges to [[_COMMUNITY_AdminAPIService]]
- 2 edges to [[_COMMUNITY_get_admin_evaluation]]
- 2 edges to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 2 edges to [[_COMMUNITY_ObservabilityTracer]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_TestTypedToolInterface]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]

## Top bridge nodes
- [[SecuritySubject]] - degree 49, connects to 10 communities
- [[rbac.py]] - degree 21, connects to 9 communities
- [[mcp_rag_agentsecurity__init__.py]] - degree 26, connects to 7 communities
- [[Permission]] - degree 28, connects to 5 communities
- [[has_permission()]] - degree 15, connects to 4 communities