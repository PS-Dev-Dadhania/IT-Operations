# Config

> God node · 80 connections · `src/mcp_rag_agent/core/config.py`

**Community:** [Config](Config.md)

## Connections by Relation

### calls
- .test_create_rag_agent_instance_direct_mode() `INFERRED`
- .test_create_rag_agent_instance_mcp_mode() `INFERRED`
- .test_direct_mode_agent_creation_wires_checkpointer() `INFERRED`
- .test_mcp_mode_agent_creation_wires_checkpointer() `INFERRED`
- .app_client() `INFERRED`
- .test_create_rag_agent_instance_raises_without_credentials() `INFERRED`
- .test_checkpointer_initialization_with_mongodb() `INFERRED`
- .test_connection_failure_gracefully_degrades_to_memory() `INFERRED`
- .test_get_checkpointer_async_wrapper() `INFERRED`
- .test_configure_langsmith_environment() `INFERRED`
- .test_is_langsmith_enabled_false_when_unconfigured() `INFERRED`
- .test_is_langsmith_enabled_true_when_configured() `INFERRED`
- .test_feature_flag_disabled_returns_none() `INFERRED`
- .test_missing_database_url_degrades_to_memory() `INFERRED`
- .test_missing_database_url_returns_none_if_no_fallback() `INFERRED`
- .test_get_hybrid_search_raises_on_unconfigured_credentials() `INFERRED`
- .test_default_embedding_dimension() `INFERRED`
- .test_import_without_credentials_does_not_raise_keyerror() `INFERRED`
- .test_session_memory_config_defaults() `INFERRED`
- .test_validate_all_passes_when_configured() `INFERRED`
- *…and 3 more `calls` connection(s) not listed (lowest-degree first to go)*

### contains
- config.py `EXTRACTED`

### imports
- [mcp_server/tools.py](mcp_server-tools.py.md) `EXTRACTED`
- [dependencies.py](dependencies.py.md) `EXTRACTED`
- create_agent.py `EXTRACTED`
- app.py `EXTRACTED`
- manager.py `EXTRACTED`
- conversation_service.py `EXTRACTED`
- chat_service.py `EXTRACTED`
- routes/it_tickets.py `EXTRACTED`
- mcp_rag_agent_creator.py `EXTRACTED`
- routes/health.py `EXTRACTED`
- checkpointer.py `EXTRACTED`
- rag_agent_creator.py `EXTRACTED`
- langsmith_integration.py `EXTRACTED`

### inherits
- BaseSettings `EXTRACTED`

### method
- .validate_all() `EXTRACTED`
- .validate_database_config() `EXTRACTED`
- .validate_llm_config() `EXTRACTED`

### rationale_for
- Configuration settings for the MCP RAG Agent. `EXTRACTED`

### references
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- create_rag_agent_instance() `INFERRED`
- [ConversationService](ConversationService.md) `INFERRED`
- create_app() `INFERRED`
- [ChatService](ChatService.md) `INFERRED`
- test_setup() `INFERRED`
- [RAGGuardrails](RAGGuardrails.md) `INFERRED`
- get_checkpointer() `INFERRED`
- get_mongo_client() `INFERRED`
- configure_langsmith_environment() `INFERRED`
- [TestConfigValidation](TestConfigValidation.md) `INFERRED`
- TestThreadIsolationAndPersistence `INFERRED`
- patch_ticket() `INFERRED`
- get_checkpointer_async() `INFERRED`
- readiness_check() `INFERRED`
- create_ticket() `INFERRED`
- TestAgentCreation `INFERRED`
- TestSessionMemoryCheckpointer `INFERRED`
- get_advanced_retriever() `INFERRED`
- get_hybrid_search() `INFERRED`
- get_langchain_run_config() `INFERRED`
- *…and 15 more `uses` connection(s) not listed (lowest-degree first to go)*

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*