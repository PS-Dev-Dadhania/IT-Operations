---
type: community
cohesion: 0.06
members: 53
---

# test_it_evaluation.py

**Cohesion:** 0.06 - loosely connected
**Members:** 53 nodes

## Members
- [[dot-__getitem__()]] - code - evaluation/datasets/loader.py
- [[dot-__getitem__()_1]] - code - evaluation/datasets/loader.py
- [[dot-__iter__()]] - code - evaluation/datasets/loader.py
- [[dot-__iter__()_1]] - code - evaluation/datasets/loader.py
- [[dot-__len__()]] - code - evaluation/datasets/loader.py
- [[dot-__len__()_1]] - code - evaluation/datasets/loader.py
- [[dot-filter_by_category()]] - code - evaluation/datasets/loader.py
- [[dot-filter_by_category()_1]] - code - evaluation/datasets/loader.py
- [[dot-filter_by_difficulty()]] - code - evaluation/datasets/loader.py
- [[dot-filter_by_intent()]] - code - evaluation/datasets/loader.py
- [[dot-save_json()]] - code - evaluation/datasets/loader.py
- [[dot-save_json()_1]] - code - evaluation/datasets/loader.py
- [[dot-test_dataset_to_dataframe()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_filter_by_category_and_difficulty()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_load_canonical_v1_benchmark()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Benchmark dataset converts cleanly to a pandas DataFrame.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[BenchmarkDataset]] - code - evaluation/datasets/loader.py
- [[BenchmarkDataset supports filtering by category or difficulty.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Canonical v1 benchmark loads cleanly with required schema fields.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Container for a versioned evaluation benchmark dataset.]] - rationale - evaluation/datasets/loader.py
- [[Container for versioned IT Support benchmark dataset.]] - rationale - evaluation/datasets/loader.py
- [[Convert legacy expected_behaviour.xlsx to strongly typed versioned…]] - rationale - evaluation/datasets/loader.py
- [[Dataset loading and validation models for production RAG and IT Support…]] - rationale - evaluation/datasets/loader.py
- [[Evaluation benchmark datasets package.]] - rationale - evaluation/datasets/__init__.py
- [[Explicit loader for IT Support benchmark datasets.]] - rationale - evaluation/datasets/loader.py
- [[Filter dataset by IT intent.]] - rationale - evaluation/datasets/loader.py
- [[Filter dataset by difficulty level.]] - rationale - evaluation/datasets/loader.py
- [[Filter dataset by domain category.]] - rationale - evaluation/datasets/loader.py
- [[ITBenchmarkDataset]] - code - evaluation/datasets/loader.py
- [[Load and validate a versioned benchmark dataset from file or version tag. Args…]] - rationale - evaluation/datasets/loader.py
- [[Path_8]] - code
- [[Resolve default path for a named benchmark version.]] - rationale - evaluation/datasets/loader.py
- [[Serialize benchmark dataset to JSON file.]] - rationale - evaluation/datasets/loader.py
- [[TestDatasetLoader]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Unit tests for Phase 13-F IT Support evaluation dataset, metric formulas, and…]] - rationale - tests/unit_tests/it_support/test_it_evaluation.py
- [[Verify end-to-end execution of the production evaluation runner in offline mode.]] - rationale - tests/unit_tests/it_support/test_it_evaluation.py
- [[Verify error handling when loading invalid or missing benchmark datasets.]] - rationale - tests/unit_tests/it_support/test_it_evaluation.py
- [[Verify that the 105-scenario IT support benchmark loads with correct typing.]] - rationale - tests/unit_tests/it_support/test_it_evaluation.py
- [[Verify versioned benchmark dataset loading and schema validation.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[asyncio_13]] - code
- [[convert_excel_to_benchmark()]] - code - evaluation/datasets/loader.py
- [[datasets__init__.py]] - code - evaluation/datasets/__init__.py
- [[get_default_dataset_path()]] - code - evaluation/datasets/loader.py
- [[json]] - concept
- [[load_benchmark_dataset()]] - code - evaluation/datasets/loader.py
- [[load_it_benchmark_dataset()]] - code - evaluation/datasets/loader.py
- [[loader.py]] - code - evaluation/datasets/loader.py
- [[pandas]] - concept
- [[tempfile]] - concept
- [[test_it_benchmark_dataset_loading()]] - code - tests/unit_tests/it_support/test_it_evaluation.py
- [[test_it_evaluation.py]] - code - tests/unit_tests/it_support/test_it_evaluation.py
- [[test_malformed_benchmark_handling()]] - code - tests/unit_tests/it_support/test_it_evaluation.py
- [[test_offline_eval_runner_execution()]] - code - tests/unit_tests/it_support/test_it_evaluation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_it_evaluationpy
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_eval_runner.py]]
- 14 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 4 edges to [[_COMMUNITY_compute_it_metrics]]
- 3 edges to [[_COMMUNITY_metrics_evaluator.py]]
- 2 edges to [[_COMMUNITY_dot-to_dataframe]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 2 edges to [[_COMMUNITY_pytest]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_AnswerGenerator]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_test_observability.py]]

## Top bridge nodes
- [[json]] - degree 13, connects to 7 communities
- [[pandas]] - degree 8, connects to 5 communities
- [[test_it_evaluation.py]] - degree 24, connects to 4 communities
- [[loader.py]] - degree 18, connects to 4 communities
- [[BenchmarkDataset]] - degree 20, connects to 3 communities