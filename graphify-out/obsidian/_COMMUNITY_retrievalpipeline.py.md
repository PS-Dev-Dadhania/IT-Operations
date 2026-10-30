---
type: community
cohesion: 0.11
members: 31
---

# retrieval/pipeline.py

**Cohesion:** 0.11 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-__init__()_27]] - code - src/mcp_rag_agent/retrieval/pipeline.py
- [[dot-__init__()_28]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-_get_model()]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-name()]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-name()_1]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-name()_2]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[dot-rerank()]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[ABC_1]] - code
- [[Abstract base class for chunk rerankers.]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Advanced Retrieval Subsystem for MCP RAG Agent. Provides production-grade query…]] - rationale - src/mcp_rag_agent/retrieval/__init__.py
- [[Advanced hybrid retrieval pipeline combining vector search, keyword search,…]] - rationale - src/mcp_rag_agent/retrieval/pipeline.py
- [[Any_13]] - code
- [[BaseReranker]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[Cross-Encoder reranker evaluating full cross-attention between query and chunk…]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[CrossEncoderReranker]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[Data models for advanced hybrid retrieval, ranking, and observability.]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[Default pass-through reranker that preserves RRF fusion ordering.]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Extensible reranking abstraction supporting NoOp, Cross-Encoder, and LLM…]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Factory to instantiate the configured reranker. Args reranker_type One of…]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Initialize AdvancedRetriever. Args mongo_client Connected MongoDBClient…]] - rationale - src/mcp_rag_agent/retrieval/pipeline.py
- [[Initialize CrossEncoderReranker. Args model_name Model identifier (e.g.…]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Lazy loader for sentence_transformers CrossEncoder.]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[Name of the reranker implementation.]] - rationale - src/mcp_rag_agent/retrieval/reranker.py
- [[NoOpReranker]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[RetrievalDebugInfo]] - code - src/mcp_rag_agent/retrieval/models.py
- [[Transparent inspection trace for retrieval debugging (no chain-of-thought).]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[get_reranker()]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[reranker.py]] - code - src/mcp_rag_agent/retrieval/reranker.py
- [[retrieval__init__.py]] - code - src/mcp_rag_agent/retrieval/__init__.py
- [[retrievalmodels.py]] - code - src/mcp_rag_agent/retrieval/models.py
- [[retrievalpipeline.py]] - code - src/mcp_rag_agent/retrieval/pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/retrieval/pipelinepy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_RetrievedChunk]]
- 13 edges to [[_COMMUNITY_typing]]
- 9 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 6 edges to [[_COMMUNITY_QueryPreprocessor]]
- 5 edges to [[_COMMUNITY_AdvancedRetriever]]
- 1 edge to [[_COMMUNITY_dot-retrieve]]
- 1 edge to [[_COMMUNITY_benchmark_retrieval.py]]
- 1 edge to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[retrievalpipeline.py]] - degree 23, connects to 7 communities
- [[retrieval__init__.py]] - degree 18, connects to 4 communities
- [[retrievalmodels.py]] - degree 11, connects to 4 communities
- [[RetrievalDebugInfo]] - degree 7, connects to 3 communities
- [[dot-__init__()_27]] - degree 7, connects to 3 communities