# retrieval.py

> 28 nodes · cohesion 0.11

## Key Concepts

- **retrieval.py** (13 connections) — `evaluation/metrics/retrieval.py`
- **normalize_doc_name()** (11 connections) — `evaluation/metrics/retrieval.py`
- **compute_hit_rate()** (8 connections) — `evaluation/metrics/retrieval.py`
- **compute_mrr()** (8 connections) — `evaluation/metrics/retrieval.py`
- **compute_precision_at_k()** (8 connections) — `evaluation/metrics/retrieval.py`
- **compute_recall_at_k()** (8 connections) — `evaluation/metrics/retrieval.py`
- **TestRetrievalMetrics** (8 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **_matches_any_relevant()** (7 connections) — `evaluation/metrics/retrieval.py`
- **.test_compute_all_retrieval_metrics()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_doc_normalization()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_hit_rate()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_mrr()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_precision_at_k()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_recall_at_k()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Retrieval quality metrics: Recall@K, Precision@K, Mean Reciprocal Rank (MRR),…** (1 connections) — `evaluation/metrics/retrieval.py`
- **Compute Hit Rate@K: 1.0 if at least one relevant document appears in top-K,…** (1 connections) — `evaluation/metrics/retrieval.py`
- **Check if retrieved doc name matches any ground truth relevant document.** (1 connections) — `evaluation/metrics/retrieval.py`
- **Compute Recall@K: proportion of ground-truth relevant documents retrieved in…** (1 connections) — `evaluation/metrics/retrieval.py`
- **Compute Precision@K: proportion of top-K retrieved documents that are relevant.…** (1 connections) — `evaluation/metrics/retrieval.py`
- **Normalize document filenames and titles for deterministic comparison.** (1 connections) — `evaluation/metrics/retrieval.py`
- **Compute Mean Reciprocal Rank (MRR): 1 / rank of the first relevant document.…** (1 connections) — `evaluation/metrics/retrieval.py`
- **MRR computes reciprocal rank of the first relevant document.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Hit Rate is 1.0 if at least one relevant doc is in top-K, else 0.0.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Batch retrieval calculator generates all standard keys.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Verify Recall@K, Precision@K, MRR, and Hit Rate calculations.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- *... and 3 more nodes in this community*

## Relationships

- [eval_runner.py](eval_runner.py.md) (7 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (7 shared connections)
- [metrics/__init__.py](metrics-__init__.py.md) (6 shared connections)
- [ViolationType](ViolationType.md) (2 shared connections)
- [typing](typing.md) (1 shared connections)

## Source Files

- `evaluation/metrics/retrieval.py`
- `tests/unit_tests/test_evaluation_framework.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*