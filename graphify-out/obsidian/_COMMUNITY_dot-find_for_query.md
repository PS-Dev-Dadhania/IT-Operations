---
type: community
cohesion: 0.40
members: 6
---

# .find_for_query

**Cohesion:** 0.40 - moderately connected
**Members:** 6 nodes

## Members
- [[dot-find_for_query()]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[dot-get_by_category()]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[dot-list_active()_4]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[List all currently active runbooks.]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Return all active runbooks matching an ITCategory.]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Select the most appropriate runbook following User issue - IT Intent -…]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/find_for_query
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Runbook]]
- 3 edges to [[_COMMUNITY_RunbookExecutor]]
- 2 edges to [[_COMMUNITY_ITCategory]]
- 1 edge to [[_COMMUNITY_intent.py]]

## Top bridge nodes
- [[dot-find_for_query()]] - degree 7, connects to 4 communities
- [[dot-get_by_category()]] - degree 6, connects to 3 communities
- [[dot-list_active()_4]] - degree 5, connects to 2 communities