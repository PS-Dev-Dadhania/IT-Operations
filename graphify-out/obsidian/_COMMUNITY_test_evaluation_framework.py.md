---
type: community
cohesion: 0.09
members: 46
---

# test_evaluation_framework.py

**Cohesion:** 0.09 - loosely connected
**Members:** 46 nodes

## Members
- [[dot-__init__()_5]] - code - evaluation/reports/comparator.py
- [[dot-_load_summary()]] - code - evaluation/reports/comparator.py
- [[dot-compute_metric_table()]] - code - evaluation/reports/comparator.py
- [[dot-generate_markdown_report()]] - code - evaluation/reports/comparator.py
- [[dot-identify_failures()]] - code - evaluation/reports/comparator.py
- [[dot-mock_eval_summaries()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_comparator_identifies_all_failures()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_comparator_metric_differences()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_markdown_report_formatting()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Aggregated summary of an evaluation benchmark execution.]] - rationale - evaluation/runners/eval_runner.py
- [[BaseModel_1]] - code
- [[BaseModel_2]] - code
- [[Comparator accurately computes baseline, current, difference, and status…]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Comparator catches underperforming questions and categorizes failures without…]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Comparator renders GitHub-flavored Markdown with comparison table and failure…]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Compares baseline vs current evaluation runs and generates transparent failure…]] - rationale - evaluation/reports/comparator.py
- [[Create baseline and current EvalRunSummary objects.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Detailed diagnostic representation of an evaluation failure.]] - rationale - evaluation/reports/comparator.py
- [[Detect structured failures across RAG, IT intents, runbooks, tickets, and…]] - rationale - evaluation/reports/comparator.py
- [[EvalRunSummary]] - code - evaluation/runners/eval_runner.py
- [[Evaluation reports and regression comparison package.]] - rationale - evaluation/reports/__init__.py
- [[FailureCase]] - code - evaluation/reports/comparator.py
- [[Generate structured comparison table across RAG and IT support metrics.]] - rationale - evaluation/reports/comparator.py
- [[MetricComparisonRow]] - code - evaluation/reports/comparator.py
- [[Path]] - code
- [[Produce GitHub-flavored Markdown regression report with full metric delta and…]] - rationale - evaluation/reports/comparator.py
- [[Regression comparator for benchmarking RAG and IT Support performance across…]] - rationale - evaluation/reports/comparator.py
- [[Regression comparator runner entrypoint.]] - rationale - evaluation/runners/regression_comparator.py
- [[RegressionComparator]] - code - evaluation/reports/comparator.py
- [[Row in the regression comparison table.]] - rationale - evaluation/reports/comparator.py
- [[Script to generate a sample baseline and current run, and execute the…]] - rationale - scripts/generate_sample_regression_report.py
- [[TestRegressionComparator]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Unit test suite for Phase 7 Production RAG Evaluation Framework. Tests 1.…]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Verify metric delta calculations, failure categorization, and report formatting.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Verify regression comparator classifies all 9 IT failure categories.]] - rationale - tests/unit_tests/it_support/test_it_evaluation.py
- [[argparse]] - concept
- [[comparator.py]] - code - evaluation/reports/comparator.py
- [[fixture]] - code
- [[generate_sample_regression_report.py]] - code - scripts/generate_sample_regression_report.py
- [[main()_4]] - code - evaluation/reports/comparator.py
- [[main()_5]] - code - scripts/generate_sample_regression_report.py
- [[pathlib]] - concept
- [[regression_comparator.py]] - code - evaluation/runners/regression_comparator.py
- [[reports__init__.py]] - code - evaluation/reports/__init__.py
- [[test_evaluation_framework.py]] - code - tests/unit_tests/test_evaluation_framework.py
- [[test_regression_comparator_failure_detection()]] - code - tests/unit_tests/it_support/test_it_evaluation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_evaluation_frameworkpy
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_eval_runner.py]]
- 14 edges to [[_COMMUNITY_test_it_evaluation.py]]
- 8 edges to [[_COMMUNITY_metrics__init__.py]]
- 7 edges to [[_COMMUNITY_retrieval.py]]
- 5 edges to [[_COMMUNITY_operational.py]]
- 4 edges to [[_COMMUNITY_typing]]
- 4 edges to [[_COMMUNITY_unittest_mock]]
- 3 edges to [[_COMMUNITY_AnswerGenerator]]
- 2 edges to [[_COMMUNITY_datetime]]
- 2 edges to [[_COMMUNITY_metrics_evaluator.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_ingestion__init__.py]]
- 1 edge to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_agentmodels.py]]

## Top bridge nodes
- [[pathlib]] - degree 21, connects to 11 communities
- [[test_evaluation_framework.py]] - degree 42, connects to 7 communities
- [[comparator.py]] - degree 20, connects to 5 communities
- [[EvalRunSummary]] - degree 17, connects to 2 communities
- [[generate_sample_regression_report.py]] - degree 9, connects to 2 communities