# RetrievedChunk

> 20 nodes · cohesion 0.12

## Key Concepts

- **RetrievedChunk** (22 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **LLMReranker** (10 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **TestRerankerAbstraction** (8 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_cross_encoder_reranks_and_updates_scores()** (5 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.to_dict()** (3 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **.rerank()** (3 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.rerank()** (3 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.rerank()** (2 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.test_factory_returns_expected_instances()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Any** (1 connections)
- **Convert chunk into standard dictionary representation.** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **Represents a final retrieved chunk with ranking provenance and metadata.** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **.name()** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **LLM-based reranker that scores relevance using prompt evaluation.** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **Initialize LLMReranker. Args: model_name: Model identifier. score_fn: Optional…** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **Rerank candidate chunks according to deep cross-relevance with the query. Args:…** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **Return top_k candidates directly without altering order or scores.** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **Test suite for NoOp, Cross-Encoder, and LLM rerankers.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Verify cross encoder alters chunk ordering based on scoring.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`

## Relationships

- [retrieval/pipeline.py](retrieval-pipeline.py.md) (18 shared connections)
- [TestTypedToolInterface](TestTypedToolInterface.md) (4 shared connections)
- [AdvancedRetriever](AdvancedRetriever.md) (3 shared connections)
- [.retrieve](retrieve.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/retrieval/models.py`
- `src/mcp_rag_agent/retrieval/reranker.py`
- `tests/unit_tests/test_advanced_retrieval.py`

## Audit Trail

- EXTRACTED: 33 (69%)
- INFERRED: 15 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*