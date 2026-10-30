# RunbookExecutor

> 22 nodes · cohesion 0.21

## Key Concepts

- **RunbookExecutor** (36 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **RunbookRegistry** (36 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **_create_sample_runbook()** (15 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **TestStatePersistenceAndValidation** (13 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **TestRunbookExecutionLifecycle** (11 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.__init__()** (6 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **.test_conditional_branching()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_explicit_and_failure_escalation()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_failed_step_transitions_to_failure_path()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_step_retry_logic()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_successful_runbook_completion()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_advancing_terminal_runbook_raises_value_error()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_invalid_outcome_string_raises_value_error()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_state_restoration_across_executor_instances()** (4 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.test_runbook_registration_and_active_versioning()** (3 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **.get_canonical_id()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **Stateful orchestrator for troubleshooting runbooks backed by LangGraph.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **In-memory thread-safe registry of validated troubleshooting runbooks.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **Resolve internal runbook_id to standard enterprise canonical code (e.g. RB-NET-…** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **Test the Step -> Evaluate -> Branch state machine execution.** (1 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **Test state persistence across turns, checkpointer restoration, and input…** (1 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **Helper creating a test runbook with step, retry, branching, and escalation.** (1 connections) — `tests/unit_tests/it_support/test_runbooks.py`

## Relationships

- [runbooks/__init__.py](runbooks-__init__.py.md) (16 shared connections)
- [test_runbooks.py](test_runbooks.py.md) (11 shared connections)
- [StepExecutionResult](StepExecutionResult.md) (8 shared connections)
- [Runbook](Runbook.md) (8 shared connections)
- [ITCategory](ITCategory.md) (6 shared connections)
- [create_runbook_subgraph](create_runbook_subgraph.md) (5 shared connections)
- [.find_for_query](find_for_query.md) (3 shared connections)
- [agent/models.py](agent-models.py.md) (2 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (2 shared connections)
- [eval_runner.py](eval_runner.py.md) (2 shared connections)
- [get_checkpointer](get_checkpointer.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/runbooks/executor.py`
- `src/mcp_rag_agent/it_support/runbooks/registry.py`
- `tests/unit_tests/it_support/test_runbooks.py`

## Audit Trail

- EXTRACTED: 61 (54%)
- INFERRED: 51 (46%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*