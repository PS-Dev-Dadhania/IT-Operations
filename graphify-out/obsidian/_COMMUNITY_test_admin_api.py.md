---
type: community
cohesion: 0.06
members: 40
---

# test_admin_api.py

**Cohesion:** 0.06 - loosely connected
**Members:** 40 nodes

## Members
- [[HTTP contract tests for the IT ticket routes without a live MongoDB connection.]] - rationale - tests/unit_tests/it_support/test_ticket_api.py
- [[Security regression tests for cross-user isolation, privilege escalation, and…]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[Test recursive redaction of sensitive credentials, API keys, passwords, and…]] - rationale - tests/unit_tests/security/test_audit.py
- [[Unit tests for MongoDB-backed structured audit logging and secret redaction.]] - rationale - tests/unit_tests/security/test_audit.py
- [[Unit tests for Phase 13-F Admin Operations API and RBAC route protection.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[Verify admin ticket details endpoint for existing and nonexistent tickets.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[Verify audit log viewing requires appropriate permission.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[Verify employee cannot access admin tickets endpoint, but IT admin can.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[Verify evaluation benchmark summary endpoint.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[Verify incidents endpoint security and returned records.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[Verify operational KPIs aggregation endpoint.]] - rationale - tests/unit_tests/api/test_admin_api.py
- [[_build_test_client()]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[audit_service()]] - code - tests/unit_tests/security/test_audit.py
- [[fastapi_testclient]] - concept
- [[fixture_3]] - code
- [[mcp_rag_agent_api]] - concept
- [[mcp_rag_agent_api_dependencies]] - concept
- [[mcp_rag_agent_api_services_admin_service]] - concept
- [[mcp_rag_agent_api_services_it_ticket_service]] - concept
- [[mcp_rag_agent_it_support_models]] - concept
- [[mcp_rag_agent_it_support_tickets_models]] - concept
- [[mcp_rag_agent_it_support_tickets_service]] - concept
- [[mcp_rag_agent_it_support_tickets_store]] - concept
- [[mcp_rag_agent_security_approval]] - concept
- [[mcp_rag_agent_security_audit]] - concept
- [[mcp_rag_agent_security_authorization]] - concept
- [[mcp_rag_agent_security_rbac]] - concept
- [[test_admin_api.py]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_admin_audit_logs_rbac()]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_admin_evaluation_endpoint()]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_admin_incidents_rbac_and_data()]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_admin_metrics_endpoint()]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_admin_ticket_detail_endpoint()]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_admin_tickets_rbac_protection()]] - code - tests/unit_tests/api/test_admin_api.py
- [[test_audit.py]] - code - tests/unit_tests/security/test_audit.py
- [[test_audit_details_secret_sanitization()]] - code - tests/unit_tests/security/test_audit.py
- [[test_security_regression.py]] - code - tests/unit_tests/security/test_security_regression.py
- [[test_ticket_api.py]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[test_ticket_routes_disabled_when_feature_flag_off()]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[test_ticket_routes_lifecycle_and_validation()]] - code - tests/unit_tests/it_support/test_ticket_api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_admin_apipy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_unittest_mock]]
- 7 edges to [[_COMMUNITY_pytest]]
- 6 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 5 edges to [[_COMMUNITY_Role]]
- 4 edges to [[_COMMUNITY_TicketRecord]]
- 4 edges to [[_COMMUNITY_datetime]]
- 3 edges to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 3 edges to [[_COMMUNITY_test_api.py]]
- 3 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 2 edges to [[_COMMUNITY_IncidentRecord]]
- 2 edges to [[_COMMUNITY_DeviceRecord]]
- 2 edges to [[_COMMUNITY_audit.py]]
- 2 edges to [[_COMMUNITY_RiskLevel]]
- 2 edges to [[_COMMUNITY_test_approval.py]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_TicketService]]
- 1 edge to [[_COMMUNITY_approval.py]]
- 1 edge to [[_COMMUNITY_TestTypedToolInterface]]
- 1 edge to [[_COMMUNITY_SecuritySubject]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_test_runbooks.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_ITCategory]]
- 1 edge to [[_COMMUNITY_test_incidents.py]]

## Top bridge nodes
- [[test_security_regression.py]] - degree 23, connects to 11 communities
- [[mcp_rag_agent_it_support_models]] - degree 9, connects to 7 communities
- [[test_admin_api.py]] - degree 26, connects to 6 communities
- [[test_audit.py]] - degree 13, connects to 5 communities
- [[_build_test_client()]] - degree 8, connects to 5 communities