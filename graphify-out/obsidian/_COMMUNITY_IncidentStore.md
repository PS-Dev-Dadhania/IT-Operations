---
type: community
cohesion: 0.27
members: 15
---

# IncidentStore

**Cohesion:** 0.27 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-__init__()_49]] - code - src/mcp_rag_agent/it_support/incidents/service.py
- [[dot-__init__()_50]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-_collection()_4]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-_to_record()_2]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-create()_14]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-find_matching()_1]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-get()_21]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-list_active()_2]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-list_all()_3]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[dot-update_status()_2]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[Any_27]] - code
- [[IncidentNotFoundError]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[IncidentStore]] - code - src/mcp_rag_agent/it_support/incidents/store.py
- [[KeyError_6]] - code
- [[Return active exact structured candidates for deterministic scoring.]] - rationale - src/mcp_rag_agent/it_support/incidents/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IncidentStore
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_IncidentRecord]]
- 4 edges to [[_COMMUNITY_test_incidents.py]]
- 2 edges to [[_COMMUNITY_dependencies.py]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]

## Top bridge nodes
- [[IncidentStore]] - degree 25, connects to 5 communities
- [[IncidentNotFoundError]] - degree 7, connects to 2 communities
- [[dot-__init__()_50]] - degree 3, connects to 2 communities
- [[dot-_to_record()_2]] - degree 8, connects to 1 community
- [[dot-find_matching()_1]] - degree 6, connects to 1 community