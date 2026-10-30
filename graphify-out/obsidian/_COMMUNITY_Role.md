---
type: community
cohesion: 0.06
members: 40
---

# Role

**Cohesion:** 0.06 - loosely connected
**Members:** 40 nodes

## Members
- [[All authenticated enterprise roles can search knowledge.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Authoritative enterprise roles for IT Support Copilot.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Cross-user isolation User A cannot read or modify User B's private ticket.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Employee can only inspect assigned device; IT Support can inspect any device.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Employee can only query own profile context; IT Support can query any profile.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Employee querying device assigned to another employee is DENIED.]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[Employees are authorized to access and comment on their own tickets.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Employees can create tickets for themselves, but cannot spoof other requesters.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Execution of unmapped or arbitrary tools is strictly denied.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[IT Support personnel can access tickets across users.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Role]] - code - src/mcp_rag_agent/security/rbac.py
- [[Subject must be non-empty and authenticated.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Test standard role-permission checks.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Tool get_user_context enforces resource-level constraints.]] - rationale - tests/unit_tests/security/test_authorization.py
- [[Unit tests for AuthorizationService, resource-level security, tool execution,…]] - rationale - tests/unit_tests/security/test_authorization.py
- [[User A (EMP-1001) attempting to accessupdate User B's (EMP-1002) ticket is…]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[Verify document chunks are filtered BEFORE synthesis based on role and…]] - rationale - tests/unit_tests/security/test_authorization.py
- [[asyncio]] - code
- [[auth_service()]] - code - tests/unit_tests/security/test_authorization.py
- [[employee_subject()]] - code - tests/unit_tests/security/test_authorization.py
- [[fixture_4]] - code
- [[it_admin_subject()]] - code - tests/unit_tests/security/test_authorization.py
- [[it_support_subject()]] - code - tests/unit_tests/security/test_authorization.py
- [[other_employee_subject()]] - code - tests/unit_tests/security/test_authorization.py
- [[security_analyst_subject()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_authorization.py]] - code - tests/unit_tests/security/test_authorization.py
- [[test_can_check_role_permissions()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_can_execute_tool_create_ticket()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_can_execute_tool_get_user_context()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_can_execute_tool_search_policy()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_can_execute_tool_unknown_tool()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_can_requires_valid_subject()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_cross_user_device_access_blocked()]] - code - tests/unit_tests/security/test_security_regression.py
- [[test_cross_user_ticket_isolation_regression()]] - code - tests/unit_tests/security/test_security_regression.py
- [[test_device_context_resource_authorization()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_retrieval_document_access_filtering()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_ticket_resource_authorization_cross_user_isolation()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_ticket_resource_authorization_employee_own_ticket()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_ticket_resource_authorization_it_support_access()]] - code - tests/unit_tests/security/test_authorization.py
- [[test_user_context_resource_authorization()]] - code - tests/unit_tests/security/test_authorization.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Role
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_SecuritySubject]]
- 7 edges to [[_COMMUNITY_RiskLevel]]
- 7 edges to [[_COMMUNITY_pydantic]]
- 5 edges to [[_COMMUNITY_mcp_servertools.py]]
- 5 edges to [[_COMMUNITY_test_admin_api.py]]
- 4 edges to [[_COMMUNITY_dependencies.py]]
- 4 edges to [[_COMMUNITY_audit.py]]
- 4 edges to [[_COMMUNITY_test_approval.py]]
- 3 edges to [[_COMMUNITY_DeviceRecord]]
- 2 edges to [[_COMMUNITY_approval.py]]
- 2 edges to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 2 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 2 edges to [[_COMMUNITY_setup_services]]
- 1 edge to [[_COMMUNITY_TicketRecord]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_RetrievedChunkOutput]]
- 1 edge to [[_COMMUNITY_TicketService]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[Role]] - degree 51, connects to 11 communities
- [[test_cross_user_ticket_isolation_regression()]] - degree 11, connects to 7 communities
- [[test_cross_user_device_access_blocked()]] - degree 11, connects to 5 communities
- [[test_authorization.py]] - degree 25, connects to 4 communities
- [[employee_subject()]] - degree 4, connects to 1 community