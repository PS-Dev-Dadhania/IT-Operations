---
type: community
cohesion: 0.11
members: 28
---

# retrieval.py

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[dot-test_compute_all_retrieval_metrics()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_doc_normalization()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_hit_rate()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_mrr()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_precision_at_k()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_recall_at_k()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Batch retrieval calculator generates all standard keys.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Check if retrieved doc name matches any ground truth relevant document.]] - rationale - evaluation/metrics/retrieval.py
- [[Compute Hit Rate@K 1.0 if at least one relevant document appears in top-K,…]] - rationale - evaluation/metrics/retrieval.py
- [[Compute Mean Reciprocal Rank (MRR) 1  rank of the first relevant document.…]] - rationale - evaluation/metrics/retrieval.py
- [[Compute Precision@K proportion of top-K retrieved documents that are relevant.…]] - rationale - evaluation/metrics/retrieval.py
- [[Compute Recall@K proportion of ground-truth relevant documents retrieved in…]] - rationale - evaluation/metrics/retrieval.py
- [[Document names are normalized across extensions, case, and unicode dashes.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Hit Rate is 1.0 if at least one relevant doc is in top-K, else 0.0.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[MRR computes reciprocal rank of the first relevant document.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Normalize document filenames and titles for deterministic comparison.]] - rationale - evaluation/metrics/retrieval.py
- [[Precision@K calculates proportion of top-K results that are relevant.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Recall@K calculates proportion of relevant documents found in top-K.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Retrieval quality metrics Recall@K, Precision@K, Mean Reciprocal Rank (MRR),…]] - rationale - evaluation/metrics/retrieval.py
- [[TestRetrievalMetrics]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Verify Recall@K, Precision@K, MRR, and Hit Rate calculations.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[_matches_any_relevant()]] - code - evaluation/metrics/retrieval.py
- [[compute_hit_rate()]] - code - evaluation/metrics/retrieval.py
- [[compute_mrr()]] - code - evaluation/metrics/retrieval.py
- [[compute_precision_at_k()]] - code - evaluation/metrics/retrieval.py
- [[compute_recall_at_k()]] - code - evaluation/metrics/retrieval.py
- [[normalize_doc_name()]] - code - evaluation/metrics/retrieval.py
- [[retrieval.py]] - code - evaluation/metrics/retrieval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/retrievalpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 7 edges to [[_COMMUNITY_eval_runner.py]]
- 6 edges to [[_COMMUNITY_metrics__init__.py]]
- 2 edges to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_typing]]

## Top bridge nodes
- [[retrieval.py]] - degree 13, connects to 5 communities
- [[normalize_doc_name()]] - degree 11, connects to 3 communities
- [[compute_hit_rate()]] - degree 8, connects to 3 communities
- [[compute_mrr()]] - degree 8, connects to 3 communities
- [[compute_precision_at_k()]] - degree 8, connects to 3 communities