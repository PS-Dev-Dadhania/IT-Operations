# eval_runner.py

> 39 nodes · cohesion 0.10

## Key Concepts

- **eval_runner.py** (41 connections) — `evaluation/runners/eval_runner.py`
- **ProductionEvalRunner** (24 connections) — `evaluation/runners/eval_runner.py`
- **BenchmarkItem** (15 connections) — `evaluation/datasets/loader.py`
- **EvalRunItemResult** (15 connections) — `evaluation/runners/eval_runner.py`
- **ITBenchmarkItem** (13 connections) — `evaluation/datasets/loader.py`
- **compute_retrieval_metrics()** (13 connections) — `evaluation/metrics/retrieval.py`
- **.run_evaluation()** (12 connections) — `evaluation/runners/eval_runner.py`
- **.evaluate_item_full()** (11 connections) — `evaluation/runners/eval_runner.py`
- **.evaluate_item_retrieval_only()** (10 connections) — `evaluation/runners/eval_runner.py`
- **.evaluate_item_offline()** (8 connections) — `evaluation/runners/eval_runner.py`
- **.__init__()** (8 connections) — `evaluation/runners/eval_runner.py`
- **.test_runner_retrieval_only_mode()** (8 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **._evaluate_it_workflow_offline()** (7 connections) — `evaluation/runners/eval_runner.py`
- **TestProductionEvalRunner** (6 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **main()** (5 connections) — `evaluation/runners/eval_runner.py`
- **.get_agent()** (5 connections) — `evaluation/runners/eval_runner.py`
- **runners/__init__.py** (5 connections) — `evaluation/runners/__init__.py`
- **BaseModel** (4 connections)
- **.to_dataframe()** (4 connections) — `evaluation/runners/eval_runner.py`
- **Any** (3 connections)
- **Path** (2 connections)
- **A single evaluation benchmark test case for RAG policies.** (1 connections) — `evaluation/datasets/loader.py`
- **A single evaluation benchmark test case for IT Support workflows.** (1 connections) — `evaluation/datasets/loader.py`
- **Calculate all standard retrieval metrics across multiple K cutoffs. Args:…** (1 connections) — `evaluation/metrics/retrieval.py`
- **DataFrame** (1 connections)
- *... and 14 more nodes in this community*

## Relationships

- [test_it_evaluation.py](test_it_evaluation.py.md) (30 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (22 shared connections)
- [retrieval.py](retrieval.py.md) (7 shared connections)
- [agent/models.py](agent-models.py.md) (5 shared connections)
- [metrics/__init__.py](metrics-__init__.py.md) (4 shared connections)
- [typing](typing.md) (4 shared connections)
- [unittest_mock](unittest_mock.md) (4 shared connections)
- [compute_it_metrics](compute_it_metrics.md) (3 shared connections)
- [operational.py](operational.py.md) (3 shared connections)
- [ITCategory](ITCategory.md) (3 shared connections)
- [RunbookExecutor](RunbookExecutor.md) (2 shared connections)
- [middleware.py](middleware.py.md) (1 shared connections)

## Source Files

- `evaluation/datasets/loader.py`
- `evaluation/metrics/retrieval.py`
- `evaluation/runners/__init__.py`
- `evaluation/runners/eval_runner.py`
- `tests/unit_tests/test_evaluation_framework.py`

## Audit Trail

- EXTRACTED: 140 (85%)
- INFERRED: 25 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*