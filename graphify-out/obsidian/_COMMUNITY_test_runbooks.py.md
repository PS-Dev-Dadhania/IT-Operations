---
type: community
cohesion: 0.09
members: 26
---

# test_runbooks.py

**Cohesion:** 0.09 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-test_category_filtering()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_default_registry_contains_all_ten_standard_runbooks()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_executor_select_and_start()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_lookup_missing_runbook_raises_error()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_selection_by_exact_tag_and_title_keywords()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_tool_list_action()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-test_tool_start_and_evaluate_flow()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[Create the execute_runbook_step LangChain StructuredTool.]] - rationale - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[Return the global default RunbookRegistry singleton.]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[StructuredTool_1]] - code
- [[Test LangChain execute_runbook_step tool interface.]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[Test heuristic and intent-assisted runbook selection from user queries.]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[Test runbook registration, versioning, and retrieval.]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[TestRunbookRegistrationAndLookup]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[TestRunbookSelection]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[TestRunbookToolIntegration]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[Unit tests for the IT troubleshooting runbook engine (Phase 13-C).]] - rationale - tests/unit_tests/it_support/test_runbooks.py
- [[_execute()]] - code - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[create_runbook_tool()]] - code - src/mcp_rag_agent/it_support/runbooks/tools.py
- [[get_default_registry()]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[mcp_rag_agent_it_support_runbooks_executor]] - concept
- [[mcp_rag_agent_it_support_runbooks_graph]] - concept
- [[mcp_rag_agent_it_support_runbooks_models]] - concept
- [[mcp_rag_agent_it_support_runbooks_registry]] - concept
- [[mcp_rag_agent_it_support_runbooks_tools]] - concept
- [[test_runbooks.py]] - code - tests/unit_tests/it_support/test_runbooks.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_runbookspy
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_RunbookExecutor]]
- 8 edges to [[_COMMUNITY_runbooks__init__.py]]
- 2 edges to [[_COMMUNITY_create_runbook_subgraph]]
- 2 edges to [[_COMMUNITY_ITCategory]]
- 2 edges to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_eval_runner.py]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]

## Top bridge nodes
- [[test_runbooks.py]] - degree 15, connects to 4 communities
- [[get_default_registry()]] - degree 11, connects to 4 communities
- [[create_runbook_tool()]] - degree 11, connects to 3 communities
- [[TestRunbookRegistrationAndLookup]] - degree 9, connects to 3 communities
- [[TestRunbookSelection]] - degree 6, connects to 2 communities