---
type: community
cohesion: 0.29
members: 8
---

# MemoryIncidentStore

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-__init__()_55]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-create()_17]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-find_matching()_2]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-get()_24]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-list_active()_3]] - code - tests/unit_tests/it_support/test_services.py
- [[In-memory test double for IncidentStore.]] - rationale - tests/unit_tests/it_support/test_services.py
- [[MemoryIncidentStore_2]] - code - tests/unit_tests/it_support/test_services.py
- [[test_service_status_active_incident_correlation()]] - code - tests/unit_tests/it_support/test_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MemoryIncidentStore
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_IncidentRecord]]
- 4 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]

## Top bridge nodes
- [[test_service_status_active_incident_correlation()]] - degree 8, connects to 3 communities
- [[MemoryIncidentStore_2]] - degree 10, connects to 2 communities
- [[dot-create()_17]] - degree 2, connects to 1 community
- [[dot-get()_24]] - degree 2, connects to 1 community