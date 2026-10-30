---
type: community
cohesion: 0.16
members: 17
---

# intent.py

**Cohesion:** 0.16 - loosely connected
**Members:** 17 nodes

## Members
- [[dot-__init__()_44]] - code - src/mcp_rag_agent/it_support/intent.py
- [[dot-classify()]] - code - src/mcp_rag_agent/it_support/intent.py
- [[dot-classify()_1]] - code - src/mcp_rag_agent/it_support/intent.py
- [[dot-classify_async()]] - code - src/mcp_rag_agent/it_support/intent.py
- [[Convenience deterministic API; it never invokes an LLM.]] - rationale - src/mcp_rag_agent/it_support/intent.py
- [[Deterministic-first intent classification for IT support requests.]] - rationale - src/mcp_rag_agent/it_support/intent.py
- [[ITEntities]] - code - src/mcp_rag_agent/it_support/models.py
- [[ITIntentResult]] - code - src/mcp_rag_agent/it_support/models.py
- [[IntentLLMFallback]] - code - src/mcp_rag_agent/it_support/intent.py
- [[Optional adapter used only for a query no rule can classify.]] - rationale - src/mcp_rag_agent/it_support/intent.py
- [[Protocol]] - code
- [[Return a validated, concise classification result.]] - rationale - src/mcp_rag_agent/it_support/intent.py
- [[Safe classification output; ``reason`` is not model chain-of-thought.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[Simple, explainable entity extraction results for Phase 13-A.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[_extract_entities()]] - code - src/mcp_rag_agent/it_support/intent.py
- [[classify_intent()]] - code - src/mcp_rag_agent/it_support/intent.py
- [[intent.py]] - code - src/mcp_rag_agent/it_support/intent.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/intentpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ITCategory]]
- 8 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_dot-find_for_query]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_typing]]

## Top bridge nodes
- [[intent.py]] - degree 13, connects to 4 communities
- [[ITIntentResult]] - degree 12, connects to 2 communities
- [[dot-classify()_1]] - degree 5, connects to 2 communities
- [[ITEntities]] - degree 6, connects to 1 community
- [[classify_intent()]] - degree 4, connects to 1 community