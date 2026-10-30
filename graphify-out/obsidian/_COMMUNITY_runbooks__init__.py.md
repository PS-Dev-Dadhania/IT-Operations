---
type: community
cohesion: 0.12
members: 34
---

# runbooks/__init__.py

**Cohesion:** 0.12 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-get_state()]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[Audit record of a single step execution attempt.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[BaseModel_7]] - code
- [[BaseModel_8]] - code
- [[Enum_2]] - code
- [[Input parameters for the execute_runbook_step tool.]] - rationale - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[Input payload when evaluating user feedback or action on the current step.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[LangChain tool integration exposing execute_runbook_step to agent runners.]] - rationale - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[LangGraph subgraph for stateful IT troubleshooting runbooks (Step - Evaluate…]] - rationale - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[Lifecycle status of a runbook execution.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Possible outcomes reported for a runbook step.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Retrieve persisted execution state from checkpointer.]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[RunbookExecutionState]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[RunbookExecutor coordinating registry, state persistence, and LangGraph…]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[RunbookStatus]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[RunbookToolInput]] - code - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[Stateful IT troubleshooting runbook engine and registry.]] - rationale - src/mcp_rag_agent/it_support/runbooks/__init__.py
- [[Stateful tracking container for runbook execution; compatible with checkpoints.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[StepActionType]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[StepEvaluationInput]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[StepExecutionRecord]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[StepOutcome]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Type of action demanded by a runbook step.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Typed schemas and contracts for IT troubleshooting runbooks.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[_utc_now()_1]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[datetime_1]] - code
- [[executor.py]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[graph.py]] - code - src/mcp_rag_agent/it_support/runbooks/graph.py
- [[langgraph_graph]] - concept
- [[runbooks__init__.py]] - code - src/mcp_rag_agent/it_support/runbooks/__init__.py
- [[runbooksmodels.py]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[runbookstools.py]] - code - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[str_2]] - code
- [[uuid]] - concept

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/runbooks/__init__py
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Runbook]]
- 16 edges to [[_COMMUNITY_RunbookExecutor]]
- 10 edges to [[_COMMUNITY_create_runbook_subgraph]]
- 9 edges to [[_COMMUNITY_typing]]
- 8 edges to [[_COMMUNITY_test_runbooks.py]]
- 7 edges to [[_COMMUNITY_StepExecutionResult]]
- 6 edges to [[_COMMUNITY_ITCategory]]
- 4 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 3 edges to [[_COMMUNITY_ObservabilityTracer]]
- 2 edges to [[_COMMUNITY_pydantic]]
- 2 edges to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_get_checkpointer]]
- 1 edge to [[_COMMUNITY_eval_runner.py]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_ConversationService]]
- 1 edge to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_test_it_evaluation.py]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_approval.py]]
- 1 edge to [[_COMMUNITY_DeviceRecord]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_AnswerGenerator]]
- 1 edge to [[_COMMUNITY_usersstore.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_test_mongodb_integration.py]]

## Top bridge nodes
- [[uuid]] - degree 21, connects to 15 communities
- [[executor.py]] - degree 23, connects to 9 communities
- [[runbooks__init__.py]] - degree 26, connects to 7 communities
- [[runbooksmodels.py]] - degree 24, connects to 6 communities
- [[graph.py]] - degree 17, connects to 6 communities