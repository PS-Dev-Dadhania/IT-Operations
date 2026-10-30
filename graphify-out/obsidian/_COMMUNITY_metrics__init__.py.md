---
type: community
cohesion: 0.07
members: 50
---

# metrics/__init__.py

**Cohesion:** 0.07 - loosely connected
**Members:** 50 nodes

## Members
- [[dot-__init__()_51]] - code - evaluation/metrics/ragas_evaluator.py
- [[dot-evaluate_batch()]] - code - evaluation/metrics/ragas_evaluator.py
- [[dot-evaluate_single()]] - code - evaluation/metrics/ragas_evaluator.py
- [[dot-test_answer_correctness()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_compute_generation_metrics_bundle()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_context_precision_and_recall()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_faithfulness_detects_hallucination()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_faithfulness_grounded_answer()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_faithfulness_refusal_standard()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[A valid grounded refusal correctly scores 1.0 faithfulness.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Answer agreeing with ground truth achieves high correctness score.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Answer making claims unsupported by context achieves low faithfulness score.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Answer whose statements are supported by context achieves 1.0 faithfulness.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Backward compatibility module for evaluation.metrics.]] - rationale - evaluation/metrics.py
- [[Bundle computes all 5 generation metrics with valid bounds.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Compute all 5 core generation quality metrics.]] - rationale - evaluation/metrics/generation.py
- [[Context precision measures signal-to-noise; recall measures fact coverage.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Evaluate a batch of question-answer pairs.]] - rationale - evaluation/metrics/ragas_evaluator.py
- [[Evaluate a single question-answer pair. Args question The input question…]] - rationale - evaluation/metrics/ragas_evaluator.py
- [[Evaluation metrics package Retrieval, Generation, and Operational metrics.]] - rationale - evaluation/metrics/__init__.py
- [[Extract lowercased non-stopword tokens of length = 3.]] - rationale - evaluation/metrics/generation.py
- [[Extract numeric values, percentages, and currencies.]] - rationale - evaluation/metrics/generation.py
- [[Generation quality metrics Answer Relevancy, Answer Correctness, Faithfulness,…]] - rationale - evaluation/metrics/generation.py
- [[Initialize the RAGAS evaluator. Args model_name Name of the model to use for…]] - rationale - evaluation/metrics/ragas_evaluator.py
- [[Measure factual agreement between generated answer and ground-truth reference…]] - rationale - evaluation/metrics/generation.py
- [[Measure the proportion of claims in the generated answer supported by retrieved…]] - rationale - evaluation/metrics/generation.py
- [[Measure the signal-to-noise ratio proportion of retrieved chunks containing…]] - rationale - evaluation/metrics/generation.py
- [[Measure whether the generated answer is directly responsive to the question.]] - rationale - evaluation/metrics/generation.py
- [[Measure whether the retrieved context contains all facts needed to answer the…]] - rationale - evaluation/metrics/generation.py
- [[RAGAS metrics computation module with safe native fallback.]] - rationale - evaluation/metrics/ragas_evaluator.py
- [[RAGASEvaluator]] - code - evaluation/metrics/ragas_evaluator.py
- [[TestGenerationMetrics]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Verify Faithfulness, Correctness, Relevancy, and Context PrecisionRecall.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Wrapper for RAGAS evaluation metrics with native fallback.]] - rationale - evaluation/metrics/ragas_evaluator.py
- [[_extract_content_tokens()]] - code - evaluation/metrics/generation.py
- [[_extract_numbers()]] - code - evaluation/metrics/generation.py
- [[compute_answer_correctness()]] - code - evaluation/metrics/generation.py
- [[compute_answer_relevancy()]] - code - evaluation/metrics/generation.py
- [[compute_context_precision()]] - code - evaluation/metrics/generation.py
- [[compute_context_recall()]] - code - evaluation/metrics/generation.py
- [[compute_faithfulness()]] - code - evaluation/metrics/generation.py
- [[compute_generation_metrics()]] - code - evaluation/metrics/generation.py
- [[datasets]] - concept
- [[extract_scalar()]] - code - evaluation/metrics/ragas_evaluator.py
- [[generation.py]] - code - evaluation/metrics/generation.py
- [[metrics.py]] - code - evaluation/metrics.py
- [[metrics__init__.py]] - code - evaluation/metrics/__init__.py
- [[ragas]] - concept
- [[ragas_evaluator.py]] - code - evaluation/metrics/ragas_evaluator.py
- [[ragas_metrics]] - concept

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/metrics/__init__py
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 6 edges to [[_COMMUNITY_retrieval.py]]
- 5 edges to [[_COMMUNITY_operational.py]]
- 5 edges to [[_COMMUNITY_typing]]
- 4 edges to [[_COMMUNITY_eval_runner.py]]
- 4 edges to [[_COMMUNITY_ViolationType]]
- 3 edges to [[_COMMUNITY_compute_it_metrics]]
- 2 edges to [[_COMMUNITY_AnswerGenerator]]
- 2 edges to [[_COMMUNITY_metrics_evaluator.py]]

## Top bridge nodes
- [[metrics__init__.py]] - degree 26, connects to 5 communities
- [[generation.py]] - degree 15, connects to 4 communities
- [[compute_generation_metrics()]] - degree 12, connects to 2 communities
- [[compute_faithfulness()]] - degree 11, connects to 2 communities
- [[RAGASEvaluator]] - degree 9, connects to 2 communities