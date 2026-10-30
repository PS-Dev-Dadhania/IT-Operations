# ConfigurationError

> 25 nodes · cohesion 0.09

## Key Concepts

- **ConfigurationError** (13 connections) — `src/mcp_rag_agent/core/config.py`
- **get_hybrid_search()** (8 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **TestToolsAndRetriever** (8 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **main()** (7 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **set_hybrid_search()** (5 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **.generate()** (4 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **.generate_batch()** (4 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **.test_get_hybrid_search_raises_on_unconfigured_credentials()** (4 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **.test_search_documents_invokes_searcher()** (4 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **.test_set_hybrid_search_mock()** (4 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **.dimensions()** (3 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **.model()** (2 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **ValueError** (1 connections)
- **Raised when required configuration settings are missing or invalid.** (1 connections) — `src/mcp_rag_agent/core/config.py`
- **Main function to demonstrate EmbeddingGenerator usage.** (1 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **Get the embedding dimensions.** (1 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **Generate embedding for a single text. Args: text: Text to generate embedding…** (1 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **Generate embeddings for multiple texts. Args: texts: List of texts to generate…** (1 connections) — `src/mcp_rag_agent/embeddings/embedding_generator.py`
- **Set or override the HybridSearch instance (for testing and dependency…** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Get or lazily initialize the shared HybridSearch engine (legacy compatibility).** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **asyncio** (1 connections)
- **Test suite for tools.py lazy initialization and execution.** (1 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **Verify get_hybrid_search raises ConfigurationError if required config is…** (1 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **Verify set_hybrid_search allows injecting a mock searcher.** (1 connections) — `tests/unit_tests/test_tools_and_retriever.py`
- **Verify search_documents invokes the underlying hybrid search engine.** (1 connections) — `tests/unit_tests/test_tools_and_retriever.py`

## Relationships

- [typing](typing.md) (12 shared connections)
- [Config](Config.md) (6 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (3 shared connections)
- [TestConfigValidation](TestConfigValidation.md) (1 shared connections)
- [TestEmbeddingGenerator](TestEmbeddingGenerator.md) (1 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [setup_services](setup_services.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/core/config.py`
- `src/mcp_rag_agent/embeddings/embedding_generator.py`
- `src/mcp_rag_agent/mcp_server/tools.py`
- `tests/unit_tests/test_tools_and_retriever.py`

## Audit Trail

- EXTRACTED: 35 (67%)
- INFERRED: 17 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*