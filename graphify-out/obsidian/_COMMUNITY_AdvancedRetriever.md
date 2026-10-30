---
type: community
cohesion: 0.13
members: 25
---

# AdvancedRetriever

**Cohesion:** 0.13 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-test_all_nine_fields_present_in_chunk_to_dict()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_candidate_overfetching_multiplier()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_debug_mode_exposes_trace_without_chain_of_thought()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_latency_metrics_tracked()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_metadata_filtering_passed_to_searches()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_pure_keyword_weight_ranks_keyword_first()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_rrf_scoring_and_deduplication_exact_math()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[AdvancedRetriever]] - code - src/mcp_rag_agent/retrieval/pipeline.py
- [[Comprehensive unit tests for advanced retrieval, RRF ranking, deduplication,…]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Production-grade hybrid retriever featuring over-fetching, RRF fusion,…]] - rationale - src/mcp_rag_agent/retrieval/pipeline.py
- [[Test suite for Reciprocal Rank Fusion, candidate merging, and deduplication.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Test suite for candidate oversampling and metadata filters.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Test suite for debug inspection mode and latency tracking.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[TestOverfetchingAndFiltering]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[TestRRFRankingAndDeduplication]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[TestRetrievalDebugAndObservability]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[TestRetrievedChunkSchemaCompliance]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[Verify RRF formula weight  (rrf_k + rank) and duplicate merging.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Verify all 9 mandatory fields are exposed on every chunk.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Verify filter_query is forwarded to both vector and text searches.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Verify retriever requests top_k  oversample_factor candidates.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[Verify semantic_weight=0.0 turns retrieval into pure keyword ranking.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[asyncio_8]] - code
- [[mcp_rag_agent_retrieval_preprocessor]] - concept
- [[test_advanced_retrieval.py]] - code - tests/unit_tests/test_advanced_retrieval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AdvancedRetriever
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_retrievalpipeline.py]]
- 4 edges to [[_COMMUNITY_benchmark_retrieval.py]]
- 3 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 3 edges to [[_COMMUNITY_RetrievedChunk]]
- 2 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_dot-retrieve]]
- 2 edges to [[_COMMUNITY_QueryPreprocessor]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_pytest]]

## Top bridge nodes
- [[AdvancedRetriever]] - degree 30, connects to 8 communities
- [[test_advanced_retrieval.py]] - degree 13, connects to 5 communities
- [[asyncio_8]] - degree 8, connects to 1 community