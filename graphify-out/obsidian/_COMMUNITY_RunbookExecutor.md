---
type: community
cohesion: 0.21
members: 22
---

# RunbookExecutor

**Cohesion:** 0.21 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_37]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[dot-get_canonical_id()]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[dot-test_advancing_terminal_runbook_raises_value_error()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_conditional_branching()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_explicit_and_failure_escalation()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_failed_step_transitions_to_failure_path()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_invalid_outcome_string_raises_value_error()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_runbook_registration_and_active_versioning()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_state_restoration_across_executor_instances()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_step_retry_logic()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_successful_runbook_completion()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[Helper creating a test runbook with step, retry, branching, and escalation.]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[In-memory thread-safe registry of validated troubleshooting runbooks.]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Resolve internal runbook_id to standard enterprise canonical code (e.g. RB-NET-…]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[RunbookExecutor]] - code - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[RunbookRegistry]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Stateful orchestrator for troubleshooting runbooks backed by LangGraph.]] - rationale - src/mcp_rag_agent/it_support/runbooks/executor.py
- [[Test state persistence across turns, checkpointer restoration, and input…]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[Test the Step - Evaluate - Branch state machine execution.]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[TestRunbookExecutionLifecycle]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[TestStatePersistenceAndValidation]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[_create_sample_runbook()]] - code - tests/unit_tests/it_support/test_runbooks.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RunbookExecutor
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_runbooks__init__.py]]
- 11 edges to [[_COMMUNITY_test_runbooks.py]]
- 8 edges to [[_COMMUNITY_Runbook]]
- 8 edges to [[_COMMUNITY_StepExecutionResult]]
- 6 edges to [[_COMMUNITY_ITCategory]]
- 5 edges to [[_COMMUNITY_create_runbook_subgraph]]
- 3 edges to [[_COMMUNITY_dot-find_for_query]]
- 2 edges to [[_COMMUNITY_eval_runner.py]]
- 2 edges to [[_COMMUNITY_agentmodels.py]]
- 2 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_get_checkpointer]]

## Top bridge nodes
- [[RunbookRegistry]] - degree 36, connects to 8 communities
- [[RunbookExecutor]] - degree 36, connects to 7 communities
- [[_create_sample_runbook()]] - degree 15, connects to 4 communities
- [[TestStatePersistenceAndValidation]] - degree 13, connects to 4 communities
- [[dot-__init__()_37]] - degree 6, connects to 4 communities