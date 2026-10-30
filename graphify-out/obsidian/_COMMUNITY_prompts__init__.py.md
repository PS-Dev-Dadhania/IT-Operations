---
type: community
cohesion: 0.33
members: 6
---

# prompts/__init__.py

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[COSTAR Prompting Framework definition for the XYZ Policy Assistant.]] - rationale - src/mcp_rag_agent/agent/prompts/system_prompt.py
- [[COSTAR prompt for the optional IT support experience.]] - rationale - src/mcp_rag_agent/agent/prompts/it_support_prompt.py
- [[Init file for agent prompts.]] - rationale - src/mcp_rag_agent/agent/prompts/__init__.py
- [[it_support_prompt.py]] - code - src/mcp_rag_agent/agent/prompts/it_support_prompt.py
- [[prompts__init__.py]] - code - src/mcp_rag_agent/agent/prompts/__init__.py
- [[system_prompt.py]] - code - src/mcp_rag_agent/agent/prompts/system_prompt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/prompts/__init__py
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_agentmodels.py]]

## Top bridge nodes
- [[prompts__init__.py]] - degree 4, connects to 1 community
- [[system_prompt.py]] - degree 3, connects to 1 community