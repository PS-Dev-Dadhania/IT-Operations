---
type: community
cohesion: 0.10
members: 39
---

# eval_runner.py

**Cohesion:** 0.10 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-__init__()_12]] - code - evaluation/runners/eval_runner.py
- [[dot-_evaluate_it_workflow_offline()]] - code - evaluation/runners/eval_runner.py
- [[dot-evaluate_item_full()]] - code - evaluation/runners/eval_runner.py
- [[dot-evaluate_item_offline()]] - code - evaluation/runners/eval_runner.py
- [[dot-evaluate_item_retrieval_only()]] - code - evaluation/runners/eval_runner.py
- [[dot-get_agent()]] - code - evaluation/runners/eval_runner.py
- [[dot-run_evaluation()]] - code - evaluation/runners/eval_runner.py
- [[dot-test_runner_retrieval_only_mode()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-to_dataframe()]] - code - evaluation/runners/eval_runner.py
- [[A single evaluation benchmark test case for IT Support workflows.]] - rationale - evaluation/datasets/loader.py
- [[A single evaluation benchmark test case for RAG policies.]] - rationale - evaluation/datasets/loader.py
- [[Any_5]] - code
- [[BaseModel_3]] - code
- [[BenchmarkItem]] - code - evaluation/datasets/loader.py
- [[Calculate all standard retrieval metrics across multiple K cutoffs. Args…]] - rationale - evaluation/metrics/retrieval.py
- [[DataFrame]] - code
- [[EvalRunItemResult]] - code - evaluation/runners/eval_runner.py
- [[Evaluate full end-to-end RAG pipeline or IT workflow.]] - rationale - evaluation/runners/eval_runner.py
- [[Evaluate offline without external API dependencies using deterministic workflow…]] - rationale - evaluation/runners/eval_runner.py
- [[Evaluate retrieval performance without executing LLM generation.]] - rationale - evaluation/runners/eval_runner.py
- [[Evaluation result for an individual benchmark item.]] - rationale - evaluation/runners/eval_runner.py
- [[Evaluation runners package.]] - rationale - evaluation/runners/__init__.py
- [[Execute evaluation loop over benchmark dataset and persist outputs.]] - rationale - evaluation/runners/eval_runner.py
- [[Flatten item results into a pandas DataFrame.]] - rationale - evaluation/runners/eval_runner.py
- [[ITBenchmarkItem]] - code - evaluation/datasets/loader.py
- [[Lazily initialize agent instance.]] - rationale - evaluation/runners/eval_runner.py
- [[Path_1]] - code
- [[Perform deterministic IT workflow evaluation (intent, runbook, escalation,…]] - rationale - evaluation/runners/eval_runner.py
- [[Production evaluation runner executing full, retrieval-only, offline, or IT…]] - rationale - evaluation/runners/eval_runner.py
- [[ProductionEvalRunner]] - code - evaluation/runners/eval_runner.py
- [[Retrieval-only mode tests retriever without calling LLM generation.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[TestProductionEvalRunner]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Unified evaluation orchestrator for measuring retrieval, generation, and IT…]] - rationale - evaluation/runners/eval_runner.py
- [[Verify evaluation runner execution modes.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[asyncio_1]] - code
- [[compute_retrieval_metrics()]] - code - evaluation/metrics/retrieval.py
- [[eval_runner.py]] - code - evaluation/runners/eval_runner.py
- [[main()_6]] - code - evaluation/runners/eval_runner.py
- [[runners__init__.py]] - code - evaluation/runners/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/eval_runnerpy
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_test_it_evaluation.py]]
- 22 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 7 edges to [[_COMMUNITY_retrieval.py]]
- 5 edges to [[_COMMUNITY_agentmodels.py]]
- 4 edges to [[_COMMUNITY_metrics__init__.py]]
- 4 edges to [[_COMMUNITY_typing]]
- 4 edges to [[_COMMUNITY_unittest_mock]]
- 3 edges to [[_COMMUNITY_ITCategory]]
- 3 edges to [[_COMMUNITY_operational.py]]
- 3 edges to [[_COMMUNITY_compute_it_metrics]]
- 2 edges to [[_COMMUNITY_RunbookExecutor]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_test_runbooks.py]]
- 1 edge to [[_COMMUNITY_datetime]]

## Top bridge nodes
- [[eval_runner.py]] - degree 41, connects to 14 communities
- [[ProductionEvalRunner]] - degree 24, connects to 5 communities
- [[compute_retrieval_metrics()]] - degree 13, connects to 3 communities
- [[dot-run_evaluation()]] - degree 12, connects to 3 communities
- [[dot-__init__()_12]] - degree 8, connects to 3 communities