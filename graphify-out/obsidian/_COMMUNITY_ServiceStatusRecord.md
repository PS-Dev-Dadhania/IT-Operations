---
type: community
cohesion: 0.12
members: 33
---

# ServiceStatusRecord

**Cohesion:** 0.12 - loosely connected
**Members:** 33 nodes

## Members
- [[dot-__init__()_19]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[dot-__init__()_20]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-_collection()_1]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[dot-_to_record()]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[dot-get()_9]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[dot-get()_10]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-list_all()_1]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[dot-list_all()_2]] - code - tests/unit_tests/it_support/test_services.py
- [[dot-upsert()]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[dot-upsert()_1]] - code - tests/unit_tests/it_support/test_services.py
- [[Any_10]] - code
- [[BaseModel_11]] - code
- [[Enum_3]] - code
- [[In-memory test double for ServiceStatusStore.]] - rationale - tests/unit_tests/it_support/test_services.py
- [[KeyError_2]] - code
- [[MemoryServiceStore]] - code - tests/unit_tests/it_support/test_services.py
- [[MongoDB persistence adapter for service statuses with in-memory fallback…]] - rationale - src/mcp_rag_agent/it_support/services/store.py
- [[Persistence store for enterprise service statuses with in-memory fallback.]] - rationale - src/mcp_rag_agent/it_support/services/store.py
- [[Public service status exports for IT support operations.]] - rationale - src/mcp_rag_agent/it_support/services/__init__.py
- [[Pydantic model representing syntheticdemo operational status of an enterprise…]] - rationale - src/mcp_rag_agent/it_support/services/models.py
- [[Raised when a requested service status cannot be found.]] - rationale - src/mcp_rag_agent/it_support/services/store.py
- [[Service status domain models and typed schemas for IT operational monitoring.]] - rationale - src/mcp_rag_agent/it_support/services/models.py
- [[Service status domain service for monitoring enterprise service health.]] - rationale - src/mcp_rag_agent/it_support/services/service.py
- [[ServiceNotFoundError]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[ServiceStatusRecord]] - code - src/mcp_rag_agent/it_support/services/models.py
- [[ServiceStatusStore]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[_get_default_seed_services()]] - code - src/mcp_rag_agent/it_support/services/store.py
- [[_utc_now()_4]] - code - src/mcp_rag_agent/it_support/services/models.py
- [[datetime_4]] - code
- [[it_supportservices__init__.py]] - code - src/mcp_rag_agent/it_support/services/__init__.py
- [[servicesmodels.py]] - code - src/mcp_rag_agent/it_support/services/models.py
- [[servicesservice.py]] - code - src/mcp_rag_agent/it_support/services/service.py
- [[servicesstore.py]] - code - src/mcp_rag_agent/it_support/services/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ServiceStatusRecord
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 6 edges to [[_COMMUNITY_typing]]
- 5 edges to [[_COMMUNITY_IncidentRecord]]
- 5 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_datetime]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_audit.py]]

## Top bridge nodes
- [[servicesservice.py]] - degree 20, connects to 6 communities
- [[servicesstore.py]] - degree 13, connects to 4 communities
- [[ServiceStatusStore]] - degree 18, connects to 3 communities
- [[servicesmodels.py]] - degree 11, connects to 3 communities
- [[ServiceStatusRecord]] - degree 23, connects to 2 communities