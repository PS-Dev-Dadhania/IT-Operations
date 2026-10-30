# test_runbooks.py

> 26 nodes · cohesion 0.09

## Key Concepts

- **test_runbooks.py** (15 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **get_default_registry()** (11 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **create_runbook_tool()** (11 connections) — `src/mcp_rag_agent/it_support/runbooks/tools.py`
- **TestRunbookRegistrationAndLookup** (9 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **TestRunbookSelection** (6 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **TestRunbookToolIntegration** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **mcp_rag_agent_it_support_runbooks_registry** (2 connections)
- **_execute()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/tools.py`
- **.test_category_filtering()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_default_registry_contains_all_ten_standard_runbooks()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_lookup_missing_runbook_raises_error()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_executor_select_and_start()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_selection_by_exact_tag_and_title_keywords()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_tool_list_action()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_tool_start_and_evaluate_flow()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **mcp_rag_agent_it_support_runbooks_executor** (1 connections)
- **mcp_rag_agent_it_support_runbooks_graph** (1 connections)
- **mcp_rag_agent_it_support_runbooks_models** (1 connections)
- **mcp_rag_agent_it_support_runbooks_tools** (1 connections)
- **Return the global default RunbookRegistry singleton.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **StructuredTool** (1 connections)
- **Create the execute_runbook_step LangChain StructuredTool.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/tools.py`
- **Unit tests for the IT troubleshooting runbook engine (Phase 13-C).** (1 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **Test heuristic and intent-assisted runbook selection from user queries.** (1 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **Test LangChain execute_runbook_step tool interface.** (1 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- *... and 1 more nodes in this community*

## Relationships

- [RunbookExecutor](RunbookExecutor.md) (11 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (8 shared connections)
- [create_runbook_subgraph](create_runbook_subgraph.md) (2 shared connections)
- [ITCategory](ITCategory.md) (2 shared connections)
- [agent/models.py](agent-models.py.md) (2 shared connections)
- [eval_runner.py](eval_runner.py.md) (1 shared connections)
- [pytest](pytest.md) (1 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/runbooks/registry.py`
- `src/mcp_rag_agent/it_support/runbooks/tools.py`
- `tests/unit_tests/it_support/test_runbooks.py`

## Audit Trail

- EXTRACTED: 44 (77%)
- INFERRED: 13 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*