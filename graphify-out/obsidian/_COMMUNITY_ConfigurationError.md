---
type: community
cohesion: 0.09
members: 25
---

# ConfigurationError

**Cohesion:** 0.09 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-dimensions()]] - code - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[dot-generate()]] - code - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[dot-generate_batch()]] - code - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[dot-model()]] - code - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[dot-test_get_hybrid_search_raises_on_unconfigured_credentials()]] - code - tests/unit_tests/test_tools_and_retriever.py
- [[dot-test_search_documents_invokes_searcher()]] - code - tests/unit_tests/test_tools_and_retriever.py
- [[dot-test_set_hybrid_search_mock()]] - code - tests/unit_tests/test_tools_and_retriever.py
- [[ConfigurationError]] - code - src/mcp_rag_agent/core/config.py
- [[Generate embedding for a single text. Args text Text to generate embedding…]] - rationale - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[Generate embeddings for multiple texts. Args texts List of texts to generate…]] - rationale - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[Get or lazily initialize the shared HybridSearch engine (legacy compatibility).]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Get the embedding dimensions.]] - rationale - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[Main function to demonstrate EmbeddingGenerator usage.]] - rationale - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[Raised when required configuration settings are missing or invalid.]] - rationale - src/mcp_rag_agent/core/config.py
- [[Set or override the HybridSearch instance (for testing and dependency…]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Test suite for tools.py lazy initialization and execution.]] - rationale - tests/unit_tests/test_tools_and_retriever.py
- [[TestToolsAndRetriever]] - code - tests/unit_tests/test_tools_and_retriever.py
- [[ValueError_2]] - code
- [[Verify get_hybrid_search raises ConfigurationError if required config is…]] - rationale - tests/unit_tests/test_tools_and_retriever.py
- [[Verify search_documents invokes the underlying hybrid search engine.]] - rationale - tests/unit_tests/test_tools_and_retriever.py
- [[Verify set_hybrid_search allows injecting a mock searcher.]] - rationale - tests/unit_tests/test_tools_and_retriever.py
- [[asyncio_9]] - code
- [[get_hybrid_search()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[main()_8]] - code - src/mcp_rag_agent/embeddings/embedding_generator.py
- [[set_hybrid_search()]] - code - src/mcp_rag_agent/mcp_server/tools.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConfigurationError
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_typing]]
- 6 edges to [[_COMMUNITY_Config]]
- 3 edges to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_TestConfigValidation]]
- 1 edge to [[_COMMUNITY_TestEmbeddingGenerator]]
- 1 edge to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_setup_services]]

## Top bridge nodes
- [[ConfigurationError]] - degree 13, connects to 4 communities
- [[get_hybrid_search()]] - degree 8, connects to 3 communities
- [[TestToolsAndRetriever]] - degree 8, connects to 3 communities
- [[set_hybrid_search()]] - degree 5, connects to 2 communities
- [[main()_8]] - degree 7, connects to 1 community