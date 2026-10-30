# StepExecutionResult

> 13 nodes · cohesion 0.28

## Key Concepts

- **StepExecutionResult** (11 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **.execute_step()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **.select_and_start()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **.start_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **._state_to_result()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **Any** (6 connections)
- **._config()** (6 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **.resume_runbook()** (5 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **Start a new runbook execution from its initial step.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **Evaluate the current step outcome and deterministically advance the runbook.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **Inspect and return the current pending step instruction without advancing.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **Select the best matching runbook for a query and initiate execution.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/executor.py`
- **Return contract from advancing or querying the runbook engine.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`

## Relationships

- [RunbookExecutor](RunbookExecutor.md) (8 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (7 shared connections)
- [create_runbook_subgraph](create_runbook_subgraph.md) (1 shared connections)
- [ITCategory](ITCategory.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/runbooks/executor.py`
- `src/mcp_rag_agent/it_support/runbooks/models.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*