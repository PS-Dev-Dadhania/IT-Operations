# retrieval/pipeline.py

> 31 nodes · cohesion 0.11

## Key Concepts

- **retrieval/pipeline.py** (23 connections) — `src/mcp_rag_agent/retrieval/pipeline.py`
- **retrieval/__init__.py** (18 connections) — `src/mcp_rag_agent/retrieval/__init__.py`
- **BaseReranker** (14 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **reranker.py** (13 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **CrossEncoderReranker** (12 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **retrieval/models.py** (11 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **get_reranker()** (11 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **NoOpReranker** (10 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **RetrievalDebugInfo** (7 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **.__init__()** (7 connections) — `src/mcp_rag_agent/retrieval/pipeline.py`
- **._get_model()** (4 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.rerank()** (3 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.name()** (2 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **ABC** (2 connections)
- **Any** (2 connections)
- **Advanced Retrieval Subsystem for MCP RAG Agent. Provides production-grade query…** (1 connections) — `src/mcp_rag_agent/retrieval/__init__.py`
- **Data models for advanced hybrid retrieval, ranking, and observability.** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **Transparent inspection trace for retrieval debugging (no chain-of-thought).** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **Advanced hybrid retrieval pipeline combining vector search, keyword search,…** (1 connections) — `src/mcp_rag_agent/retrieval/pipeline.py`
- **Initialize AdvancedRetriever. Args: mongo_client: Connected MongoDBClient…** (1 connections) — `src/mcp_rag_agent/retrieval/pipeline.py`
- **.name()** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **.name()** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **Extensible reranking abstraction supporting NoOp, Cross-Encoder, and LLM…** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- **Abstract base class for chunk rerankers.** (1 connections) — `src/mcp_rag_agent/retrieval/reranker.py`
- *... and 6 more nodes in this community*

## Relationships

- [RetrievedChunk](RetrievedChunk.md) (18 shared connections)
- [typing](typing.md) (13 shared connections)
- [TestTypedToolInterface](TestTypedToolInterface.md) (9 shared connections)
- [QueryPreprocessor](QueryPreprocessor.md) (6 shared connections)
- [AdvancedRetriever](AdvancedRetriever.md) (5 shared connections)
- [pydantic](pydantic.md) (1 shared connections)
- [.retrieve](retrieve.md) (1 shared connections)
- [middleware.py](middleware.py.md) (1 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (1 shared connections)
- [benchmark_retrieval.py](benchmark_retrieval.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/retrieval/__init__.py`
- `src/mcp_rag_agent/retrieval/models.py`
- `src/mcp_rag_agent/retrieval/pipeline.py`
- `src/mcp_rag_agent/retrieval/reranker.py`

## Audit Trail

- EXTRACTED: 96 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*