---
type: community
cohesion: 0.08
members: 38
---

# unittest_mock

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[Check if a valid non-dummy OpenAI API key is present.]] - rationale - tests/integration_tests/test_mcp_integration.py
- [[Demonstrate the performance difference between stateless and memory-backed…]] - rationale - scripts/compare_memory_evaluation.py
- [[Evaluation comparison script Pre-Memory (Stateless) vs Post-Memory (Persistent…]] - rationale - scripts/compare_memory_evaluation.py
- [[Integration tests for FastMCP server endpoints and tool registry.]] - rationale - tests/integration_tests/test_mcp_integration.py
- [[Unit tests for EmbeddingGenerator consistency and validation.]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[Unit tests for MCP server tools and lazy retriever initialization.]] - rationale - tests/unit_tests/test_tools_and_retriever.py
- [[Unit tests for Phase 4 Production Agent Architecture. Tests typed tool…]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Unit tests for Phase 5 Persistent Conversation Memory.]] - rationale - tests/unit_tests/test_session_memory.py
- [[Unit tests for agent creation factories and execution modes.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[Unit tests for configuration validation and error handling.]] - rationale - tests/unit_tests/test_config.py
- [[Unit tests for document ingestion and cross-platform path resolution.]] - rationale - tests/unit_tests/test_ingestion.py
- [[compare_memory_evaluation.py]] - code - scripts/compare_memory_evaluation.py
- [[is_live_openai_configured()]] - code - tests/integration_tests/test_mcp_integration.py
- [[langgraph_checkpoint_memory]] - concept
- [[mcp_rag_agent_agent]] - concept
- [[mcp_rag_agent_agent_create_agent]] - concept
- [[mcp_rag_agent_agent_models]] - concept
- [[mcp_rag_agent_agent_runner]] - concept
- [[mcp_rag_agent_core_checkpointer]] - concept
- [[mcp_rag_agent_core_config]] - concept
- [[mcp_rag_agent_embeddings_embedding_generator]] - concept
- [[mcp_rag_agent_embeddings_index_documents]] - concept
- [[mcp_rag_agent_mcp_server_server]] - concept
- [[mcp_rag_agent_mcp_server_tools]] - concept
- [[mcp_rag_agent_retrieval_models]] - concept
- [[memory_aware_invoke()]] - code - scripts/compare_memory_evaluation.py
- [[pymongo_errors]] - concept
- [[run_multi_turn_comparison()]] - code - scripts/compare_memory_evaluation.py
- [[test_agent_architecture.py]] - code - tests/unit_tests/test_agent_architecture.py
- [[test_agent_creation.py]] - code - tests/unit_tests/test_agent_creation.py
- [[test_config.py]] - code - tests/unit_tests/test_config.py
- [[test_embedding_generator.py]] - code - tests/unit_tests/test_embedding_generator.py
- [[test_ingestion.py]] - code - tests/unit_tests/test_ingestion.py
- [[test_mcp_integration.py]] - code - tests/integration_tests/test_mcp_integration.py
- [[test_session_memory.py]] - code - tests/unit_tests/test_session_memory.py
- [[test_tools_and_retriever.py]] - code - tests/unit_tests/test_tools_and_retriever.py
- [[unittest_mock]] - concept
- [[warnings]] - concept

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/unittest_mock
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_admin_api.py]]
- 9 edges to [[_COMMUNITY_pytest]]
- 7 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 5 edges to [[_COMMUNITY_typing]]
- 4 edges to [[_COMMUNITY_AnswerGenerator]]
- 4 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 4 edges to [[_COMMUNITY_test_api.py]]
- 4 edges to [[_COMMUNITY_eval_runner.py]]
- 4 edges to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 4 edges to [[_COMMUNITY_test_observability.py]]
- 2 edges to [[_COMMUNITY_RAGAgentRunner]]
- 2 edges to [[_COMMUNITY_get_checkpointer]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_test_it_evaluation.py]]
- 2 edges to [[_COMMUNITY_AdvancedRetriever]]
- 2 edges to [[_COMMUNITY_ITCategory]]
- 2 edges to [[_COMMUNITY_benchmark_retrieval.py]]
- 2 edges to [[_COMMUNITY_test_mongodb_integration.py]]
- 1 edge to [[_COMMUNITY_ConfigurationError]]
- 1 edge to [[_COMMUNITY_TestTypedToolInterface]]
- 1 edge to [[_COMMUNITY_TestConfigValidation]]
- 1 edge to [[_COMMUNITY_TestMCPIntegration]]
- 1 edge to [[_COMMUNITY_TestEmbeddingGenerator]]
- 1 edge to [[_COMMUNITY_TestDocumentIngestion]]
- 1 edge to [[_COMMUNITY_TestDirectAndMCPParity]]
- 1 edge to [[_COMMUNITY_Role]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_DeviceRecord]]
- 1 edge to [[_COMMUNITY_ServiceStatusChecker]]
- 1 edge to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 1 edge to [[_COMMUNITY_test_runbooks.py]]
- 1 edge to [[_COMMUNITY_UserNotFoundError]]
- 1 edge to [[_COMMUNITY_TestAPIIntegration]]
- 1 edge to [[_COMMUNITY_test_incidents.py]]
- 1 edge to [[_COMMUNITY_metrics_evaluator.py]]

## Top bridge nodes
- [[unittest_mock]] - degree 26, connects to 17 communities
- [[mcp_rag_agent_core_config]] - degree 20, connects to 10 communities
- [[mcp_rag_agent_agent_models]] - degree 12, connects to 7 communities
- [[test_agent_architecture.py]] - degree 15, connects to 6 communities
- [[test_session_memory.py]] - degree 16, connects to 5 communities