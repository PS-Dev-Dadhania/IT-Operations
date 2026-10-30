# AdvancedRetriever

> 25 nodes · cohesion 0.13

## Key Concepts

- **AdvancedRetriever** (30 connections) — `src/mcp_rag_agent/retrieval/pipeline.py`
- **test_advanced_retrieval.py** (13 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **asyncio** (8 connections)
- **TestOverfetchingAndFiltering** (5 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **TestRetrievalDebugAndObservability** (5 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **TestRRFRankingAndDeduplication** (5 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_candidate_overfetching_multiplier()** (4 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_metadata_filtering_passed_to_searches()** (4 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **TestRetrievedChunkSchemaCompliance** (4 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_pure_keyword_weight_ranks_keyword_first()** (4 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_rrf_scoring_and_deduplication_exact_math()** (4 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_debug_mode_exposes_trace_without_chain_of_thought()** (3 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_latency_metrics_tracked()** (3 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_all_nine_fields_present_in_chunk_to_dict()** (3 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **mcp_rag_agent_retrieval_preprocessor** (1 connections)
- **Production-grade hybrid retriever featuring over-fetching, RRF fusion,…** (1 connections) — `src/mcp_rag_agent/retrieval/pipeline.py`
- **Comprehensive unit tests for advanced retrieval, RRF ranking, deduplication,…** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Verify semantic_weight=0.0 turns retrieval into pure keyword ranking.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Test suite for candidate oversampling and metadata filters.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Verify retriever requests top_k * oversample_factor candidates.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Verify filter_query is forwarded to both vector and text searches.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Test suite for debug inspection mode and latency tracking.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Verify all 9 mandatory fields are exposed on every chunk.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Test suite for Reciprocal Rank Fusion, candidate merging, and deduplication.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **Verify RRF formula: weight / (rrf_k + rank) and duplicate merging.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`

## Relationships

- [retrieval/pipeline.py](retrieval-pipeline.py.md) (5 shared connections)
- [benchmark_retrieval.py](benchmark_retrieval.py.md) (4 shared connections)
- [TestTypedToolInterface](TestTypedToolInterface.md) (3 shared connections)
- [RetrievedChunk](RetrievedChunk.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [.retrieve](retrieve.md) (2 shared connections)
- [typing](typing.md) (2 shared connections)
- [QueryPreprocessor](QueryPreprocessor.md) (2 shared connections)
- [unittest_mock](unittest_mock.md) (2 shared connections)
- [pytest](pytest.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/retrieval/pipeline.py`
- `tests/unit_tests/test_advanced_retrieval.py`

## Audit Trail

- EXTRACTED: 44 (67%)
- INFERRED: 22 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*