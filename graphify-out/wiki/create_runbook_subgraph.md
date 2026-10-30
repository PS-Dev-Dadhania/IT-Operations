# create_runbook_subgraph

> 19 nodes · cohesion 0.12

## Key Concepts

- **create_runbook_subgraph()** (17 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **_get_runbook_from_state()** (9 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **RunbookNotFoundError** (9 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **RunbookGraphState** (5 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **.get()** (5 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **escalate_node()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **evaluate_node()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **resolve_node()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **step_node()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **advance_step_node()** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **branch_router()** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **entry_router()** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **Any** (1 connections)
- **Execution state container passed through the LangGraph runbook subgraph.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **Build and compile the LangGraph runbook state machine. Target Workflow: START ↓…** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/graph.py`
- **KeyError** (1 connections)
- **Raised when a requested runbook or version does not exist.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **Retrieve a runbook by ID or canonical code, resolving to active version.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **TypedDict** (1 connections)

## Relationships

- [runbooks/__init__.py](runbooks-__init__.py.md) (10 shared connections)
- [RunbookExecutor](RunbookExecutor.md) (5 shared connections)
- [test_runbooks.py](test_runbooks.py.md) (2 shared connections)
- [Runbook](Runbook.md) (2 shared connections)
- [StepExecutionResult](StepExecutionResult.md) (1 shared connections)
- [ITCategory](ITCategory.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/runbooks/graph.py`
- `src/mcp_rag_agent/it_support/runbooks/registry.py`

## Audit Trail

- EXTRACTED: 27 (64%)
- INFERRED: 15 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*