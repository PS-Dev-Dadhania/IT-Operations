---
type: community
cohesion: 0.28
members: 13
---

# StepExecutionResult

**Cohesion:** 0.28 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-_config()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[dot-_state_to_result()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[dot-execute_step()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[dot-resume_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[dot-select_and_start()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[dot-start_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[Any_32]] - code
- [[Evaluate the current step outcome and deterministically advance the runbook.]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[Inspect and return the current pending step instruction without advancing.]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[Return contract from advancing or querying the runbook engine.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Select the best matching runbook for a query and initiate execution.]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[Start a new runbook execution from its initial step.]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[StepExecutionResult]] - code - src/mcp_rag_agent/it_support/runbooks/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StepExecutionResult
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_RunbookExecutor]]
- 7 edges to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_create_runbook_subgraph]]
- 1 edge to [[_COMMUNITY_ITCategory]]

## Top bridge nodes
- [[dot-select_and_start()]] - degree 7, connects to 3 communities
- [[StepExecutionResult]] - degree 11, connects to 2 communities
- [[dot-execute_step()]] - degree 7, connects to 2 communities
- [[dot-_state_to_result()]] - degree 7, connects to 2 communities
- [[dot-_config()]] - degree 6, connects to 2 communities