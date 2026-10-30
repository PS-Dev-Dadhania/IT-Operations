---
type: community
cohesion: 0.12
members: 19
---

# create_runbook_subgraph

**Cohesion:** 0.12 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-get()_18]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Any_26]] - code
- [[Build and compile the LangGraph runbook state machine. Target Workflow START ↓…]] - rationale - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[Execution state container passed through the LangGraph runbook subgraph.]] - rationale - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[KeyError_5]] - code
- [[Raised when a requested runbook or version does not exist.]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Retrieve a runbook by ID or canonical code, resolving to active version.]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[RunbookGraphState]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[RunbookNotFoundError]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[TypedDict]] - code
- [[_get_runbook_from_state()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[advance_step_node()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[branch_router()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[create_runbook_subgraph()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[entry_router()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[escalate_node()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[evaluate_node()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[resolve_node()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[step_node()]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/create_runbook_subgraph
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_runbooks__init__.py]]
- 5 edges to [[_COMMUNITY_RunbookExecutor]]
- 2 edges to [[_COMMUNITY_Runbook]]
- 2 edges to [[_COMMUNITY_test_runbooks.py]]
- 1 edge to [[_COMMUNITY_StepExecutionResult]]
- 1 edge to [[_COMMUNITY_ITCategory]]

## Top bridge nodes
- [[RunbookNotFoundError]] - degree 9, connects to 5 communities
- [[create_runbook_subgraph()]] - degree 17, connects to 3 communities
- [[_get_runbook_from_state()]] - degree 9, connects to 3 communities
- [[dot-get()_18]] - degree 5, connects to 2 communities
- [[RunbookGraphState]] - degree 5, connects to 1 community