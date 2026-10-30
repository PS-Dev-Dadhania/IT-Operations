---
type: community
cohesion: 0.10
members: 31
---

# test_mcp_it_tools.py

**Cohesion:** 0.10 - loosely connected
**Members:** 31 nodes

## Members
- [[Deterministic, idempotent seed script for IT operations data (Users, Devices,…]] - rationale - scripts/seed_it_operations_data.py
- [[Integration and workflow tests for IT Operations agent capabilities and tool…]] - rationale - tests/unit_tests/it_support/test_it_agent_flows.py
- [[Test tools invoked during a VPN diagnostic scenario.]] - rationale - tests/unit_tests/it_support/test_it_agent_flows.py
- [[Test tools invoked during an access provisioning  ticket scenario.]] - rationale - tests/unit_tests/it_support/test_it_agent_flows.py
- [[Unit tests for typed IT Operations MCP tools and FastMCP registration.]] - rationale - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[asyncio_4]] - code
- [[asyncio_5]] - code
- [[mcp_rag_agent_it_support_devices_models]] - concept
- [[mcp_rag_agent_it_support_devices_store]] - concept
- [[mcp_rag_agent_it_support_runbooks]] - concept
- [[mcp_rag_agent_it_support_services_models]] - concept
- [[mcp_rag_agent_it_support_services_service]] - concept
- [[mcp_rag_agent_it_support_services_store]] - concept
- [[mcp_rag_agent_it_support_tools]] - concept
- [[mcp_rag_agent_it_support_users_models]] - concept
- [[mcp_rag_agent_it_support_users_service]] - concept
- [[mcp_rag_agent_it_support_users_store]] - concept
- [[seed_it_operations_data.py]] - code - scripts/seed_it_operations_data.py
- [[test_agent_toolbelt_includes_it_operations_when_flag_enabled()]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[test_check_service_status_operational_and_unknown()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_create_ticket_flow_and_duplicate_detection()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_get_device_info_by_device_id_and_user_id()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_get_device_info_missing_args()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_get_user_context_not_found()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_get_user_context_success()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_it_agent_flows.py]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[test_it_operations_tools_instantiation()]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[test_it_tools_access_request_and_ticket_creation()]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[test_it_tools_vpn_workflow()]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[test_mask_sensitive_no_credential_leakage()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[test_mcp_it_tools.py]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_mcp_it_toolspy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_mcp_servertools.py]]
- 7 edges to [[_COMMUNITY_unittest_mock]]
- 6 edges to [[_COMMUNITY_DeviceRecord]]
- 6 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 6 edges to [[_COMMUNITY_test_admin_api.py]]
- 4 edges to [[_COMMUNITY_UserNotFoundError]]
- 3 edges to [[_COMMUNITY_setup_services]]
- 2 edges to [[_COMMUNITY_TicketRecord]]
- 2 edges to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_usersstore.py]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_metrics_evaluator.py]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]
- 1 edge to [[_COMMUNITY_test_observability.py]]
- 1 edge to [[_COMMUNITY_test_mongodb_integration.py]]
- 1 edge to [[_COMMUNITY_datetime]]

## Top bridge nodes
- [[seed_it_operations_data.py]] - degree 18, connects to 9 communities
- [[test_mcp_it_tools.py]] - degree 27, connects to 7 communities
- [[test_it_agent_flows.py]] - degree 25, connects to 7 communities
- [[mcp_rag_agent_it_support_devices_models]] - degree 5, connects to 2 communities
- [[test_agent_toolbelt_includes_it_operations_when_flag_enabled()]] - degree 4, connects to 2 communities