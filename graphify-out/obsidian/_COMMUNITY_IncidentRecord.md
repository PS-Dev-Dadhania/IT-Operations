---
type: community
cohesion: 0.13
members: 34
---

# IncidentRecord

**Cohesion:** 0.13 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-__init__()_16]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-create()_7]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-create_incident()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-find_known_incident()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-get()_7]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-get_incident()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-list_active()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-list_active_incidents()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-list_all()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-list_all_incidents()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-update_status()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-update_status()_1]] - code - tests/unit_tests/it_support/test_incidents.py
- [[BaseModel_9]] - code
- [[Incident persistence and known-incident detection domain.]] - rationale - src/mcp_rag_agent/it_support/incidents/__init__.py
- [[Incident use cases, including deterministic known-incident detection.]] - rationale - src/mcp_rag_agent/it_support/incidents/service.py
- [[IncidentCreate]] - code - src/mcp_rag_agent/it_support/incidents/models.py
- [[IncidentMatchCriteria]] - code - src/mcp_rag_agent/it_support/incidents/models.py
- [[IncidentRecord]] - code - src/mcp_rag_agent/it_support/incidents/models.py
- [[IncidentService]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[IncidentStatus]] - code - src/mcp_rag_agent/it_support/models.py
- [[Match active incidents on service plus exact structured incident signals.]] - rationale - src/mcp_rag_agent/it_support/incidents/service.py
- [[MemoryIncidentStore]] - code - tests/unit_tests/api/test_admin_api.py
- [[MongoDB persistence adapter for incidents with in-memory fallback support.]] - rationale - src/mcp_rag_agent/it_support/incidents/store.py
- [[Persisted incident contracts and structured incident matching criteria.]] - rationale - src/mcp_rag_agent/it_support/incidents/models.py
- [[_get_default_seed_incidents()]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[_utc_now()_2]] - code - src/mcp_rag_agent/it_support/incidents/models.py
- [[_val()]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[datetime_2]] - code
- [[fixture_5]] - code
- [[incidents__init__.py]] - code - src/mcp_rag_agent/it_support/incidents/__init__.py
- [[incidentsmodels.py]] - code - src/mcp_rag_agent/it_support/incidents/models.py
- [[incidentsservice.py]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[incidentsstore.py]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[test_setup()]] - code - tests/unit_tests/api/test_admin_api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IncidentRecord
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_IncidentStore]]
- 18 edges to [[_COMMUNITY_test_incidents.py]]
- 17 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 12 edges to [[_COMMUNITY_dependencies.py]]
- 7 edges to [[_COMMUNITY_MemoryIncidentStore]]
- 7 edges to [[_COMMUNITY_AdminAPIService]]
- 5 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 5 edges to [[_COMMUNITY_ServiceStatusRecord]]
- 4 edges to [[_COMMUNITY_ITCategory]]
- 3 edges to [[_COMMUNITY_audit.py]]
- 2 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_TicketRecord]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_test_admin_api.py]]
- 2 edges to [[_COMMUNITY_TicketService]]
- 1 edge to [[_COMMUNITY_Role]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_RiskLevel]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_datetime]]

## Top bridge nodes
- [[test_setup()]] - degree 20, connects to 12 communities
- [[IncidentService]] - degree 30, connects to 9 communities
- [[IncidentStatus]] - degree 27, connects to 8 communities
- [[IncidentRecord]] - degree 44, connects to 6 communities
- [[incidentsmodels.py]] - degree 18, connects to 6 communities