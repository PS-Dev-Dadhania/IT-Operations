---
type: community
cohesion: 0.12
members: 20
---

# RetrievedChunk

**Cohesion:** 0.12 - loosely connected
**Members:** 20 nodes

## Members
- [[dot-__init__()_41]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-name()_3]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-rerank()_1]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-rerank()_2]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-rerank()_3]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-test_cross_encoder_reranks_and_updates_scores()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_factory_returns_expected_instances()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-to_dict()]] - code - src/mcp_rag_agent/retrieval/models.py
- [[Any_24]] - code
- [[Convert chunk into standard dictionary representation.]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[Initialize LLMReranker. Args model_name Model identifier. score_fn Optional…]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[LLM-based reranker that scores relevance using prompt evaluation.]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[LLMReranker]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[Represents a final retrieved chunk with ranking provenance and metadata.]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[Rerank candidate chunks according to deep cross-relevance with the query. Args…]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[RetrievedChunk]] - code - src/mcp_rag_agent/retrieval/models.py
- [[Return top_k candidates directly without altering order or scores.]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Test suite for NoOp, Cross-Encoder, and LLM rerankers.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[TestRerankerAbstraction]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[Verify cross encoder alters chunk ordering based on scoring.]] - rationale - tests/unit_tests/test_advanced_retrieval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RetrievedChunk
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_retrievalpipeline.py]]
- 4 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 3 edges to [[_COMMUNITY_AdvancedRetriever]]
- 1 edge to [[_COMMUNITY_dot-retrieve]]

## Top bridge nodes
- [[RetrievedChunk]] - degree 22, connects to 4 communities
- [[TestRerankerAbstraction]] - degree 8, connects to 2 communities
- [[dot-test_cross_encoder_reranks_and_updates_scores()]] - degree 5, connects to 2 communities
- [[LLMReranker]] - degree 10, connects to 1 community
- [[dot-rerank()_1]] - degree 3, connects to 1 community