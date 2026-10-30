---
type: community
cohesion: 0.10
members: 27
---

# ServiceStatusChecker

**Cohesion:** 0.10 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-__init__()_29]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[dot-check_service_status()]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[dot-list_all_services()]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[dot-set_service_status()]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[Any_14]] - code
- [[Check operational status of a service with incident correlation. Args…]] - rationale - src/mcp_rag_agent/it_support/services/service.py
- [[Domain service checking synthetic operational status of enterprise services.]] - rationale - src/mcp_rag_agent/it_support/services/service.py
- [[Idempotently seed users, devices, and service statuses.]] - rationale - scripts/seed_it_operations_data.py
- [[List statuses for all stored or standard services.]] - rationale - src/mcp_rag_agent/it_support/services/service.py
- [[Normalize input service query into a canonical service key.]] - rationale - src/mcp_rag_agent/it_support/services/service.py
- [[Operational status of a monitored synthetic enterprise service.]] - rationale - src/mcp_rag_agent/it_support/services/models.py
- [[ServiceOperationalStatus]] - code - src/mcp_rag_agent/it_support/services/models.py
- [[ServiceStatusChecker]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[Unit tests for service status models, store, and domain service.]] - rationale - tests/unit_tests/it_support/test_services.py
- [[Update or register status for a service in the store.]] - rationale - src/mcp_rag_agent/it_support/services/service.py
- [[get_seed_devices()]] - code - scripts/seed_it_operations_data.py
- [[get_seed_service_statuses()]] - code - scripts/seed_it_operations_data.py
- [[mcp_rag_agent_it_support_incidents_models]] - concept
- [[mcp_rag_agent_it_support_incidents_service]] - concept
- [[normalize_service_name()]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[seed_it_operations_data()]] - code - scripts/seed_it_operations_data.py
- [[str_5]] - code
- [[test_service_status_invalid_input_raises_value_error()]] - code - tests/unit_tests/it_support/test_services.py
- [[test_service_status_known_services_and_aliases()]] - code - tests/unit_tests/it_support/test_services.py
- [[test_service_status_store_mongodb_adapter()]] - code - tests/unit_tests/it_support/test_services.py
- [[test_service_status_unknown_service()]] - code - tests/unit_tests/it_support/test_services.py
- [[test_services.py]] - code - tests/unit_tests/it_support/test_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServiceStatusChecker
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_ServiceStatusRecord]]
- 6 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 5 edges to [[_COMMUNITY_IncidentRecord]]
- 4 edges to [[_COMMUNITY_MemoryIncidentStore]]
- 3 edges to [[_COMMUNITY_test_admin_api.py]]
- 2 edges to [[_COMMUNITY_DeviceRecord]]
- 2 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_setup_services]]
- 2 edges to [[_COMMUNITY_pytest]]
- 2 edges to [[_COMMUNITY_test_incidents.py]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_UserContextRecord]]
- 1 edge to [[_COMMUNITY_usersstore.py]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[ServiceStatusChecker]] - degree 23, connects to 6 communities
- [[test_services.py]] - degree 16, connects to 6 communities
- [[seed_it_operations_data()]] - degree 9, connects to 6 communities
- [[ServiceOperationalStatus]] - degree 16, connects to 3 communities
- [[normalize_service_name()]] - degree 6, connects to 2 communities