---
type: community
cohesion: 0.21
members: 16
---

# test_incidents.py

**Cohesion:** 0.21 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-__init__()_45]] - code - tests/unit_tests/it_support/test_incidents.py
- [[dot-create()_13]] - code - tests/unit_tests/it_support/test_incidents.py
- [[dot-find_matching()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[dot-get()_20]] - code - tests/unit_tests/it_support/test_incidents.py
- [[dot-list_active()_1]] - code - tests/unit_tests/it_support/test_incidents.py
- [[Incident persistence and deterministic known-incident matching tests.]] - rationale - tests/unit_tests/it_support/test_incidents.py
- [[MemoryIncidentStore_1]] - code - tests/unit_tests/it_support/test_incidents.py
- [[_incident()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[mcp_rag_agent_it_support_incidents_store]] - concept
- [[test_incident_create_retrieve_and_status_update()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[test_incident_resolve_sets_end_time()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[test_incident_service_find_known_case_insensitivity_and_partial_signals()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[test_incident_store_queries_and_not_found_handling()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[test_incident_store_uses_mongodb()]] - code - tests/unit_tests/it_support/test_incidents.py
- [[test_incidents.py]] - code - tests/unit_tests/it_support/test_incidents.py
- [[test_known_incident_detection_requires_structured_match()]] - code - tests/unit_tests/it_support/test_incidents.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_incidentspy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_IncidentRecord]]
- 4 edges to [[_COMMUNITY_IncidentStore]]
- 3 edges to [[_COMMUNITY_ITCategory]]
- 2 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[test_incidents.py]] - degree 14, connects to 3 communities
- [[_incident()]] - degree 10, connects to 3 communities
- [[test_incident_store_queries_and_not_found_handling()]] - degree 8, connects to 3 communities
- [[test_known_incident_detection_requires_structured_match()]] - degree 6, connects to 2 communities
- [[test_incident_resolve_sets_end_time()]] - degree 5, connects to 2 communities