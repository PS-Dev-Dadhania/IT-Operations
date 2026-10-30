# Config

> 53 nodes · cohesion 0.05

## Key Concepts

- **Config** (80 connections) — `src/mcp_rag_agent/core/config.py`
- **TestThreadIsolationAndPersistence** (11 connections) — `tests/unit_tests/test_session_memory.py`
- **TestAgentCreation** (9 connections) — `tests/unit_tests/test_agent_creation.py`
- **create_mcp_rag_agent()** (8 connections) — `src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py`
- **get_langchain_run_config()** (8 connections) — `src/mcp_rag_agent/observability/langsmith_integration.py`
- **is_langsmith_enabled()** (7 connections) — `src/mcp_rag_agent/observability/langsmith_integration.py`
- **TestLangSmithIntegration** (7 connections) — `tests/unit_tests/test_observability.py`
- **_load_mcp_tools_and_prompt()** (6 connections) — `src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py`
- **.test_create_rag_agent_instance_direct_mode()** (6 connections) — `tests/unit_tests/test_agent_creation.py`
- **.test_create_rag_agent_instance_mcp_mode()** (6 connections) — `tests/unit_tests/test_agent_creation.py`
- **.test_direct_mode_agent_creation_wires_checkpointer()** (6 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_mcp_mode_agent_creation_wires_checkpointer()** (6 connections) — `tests/unit_tests/test_session_memory.py`
- **.validate_all()** (5 connections) — `src/mcp_rag_agent/core/config.py`
- **.test_create_rag_agent_instance_raises_without_credentials()** (5 connections) — `tests/unit_tests/test_agent_creation.py`
- **get_mcp_connections()** (4 connections) — `src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py`
- **.__init__()** (4 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **.validate_database_config()** (4 connections) — `src/mcp_rag_agent/core/config.py`
- **.validate_llm_config()** (4 connections) — `src/mcp_rag_agent/core/config.py`
- **.test_configure_langsmith_environment()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_is_langsmith_enabled_false_when_unconfigured()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_is_langsmith_enabled_true_when_configured()** (4 connections) — `tests/unit_tests/test_observability.py`
- **asyncio** (3 connections)
- **.test_search_documents_tool_metadata()** (3 connections) — `tests/unit_tests/test_agent_creation.py`
- **.test_get_langchain_run_config()** (3 connections) — `tests/unit_tests/test_observability.py`
- **.test_no_import_time_side_effects()** (2 connections) — `tests/unit_tests/test_session_memory.py`
- *... and 28 more nodes in this community*

## Relationships

- [agent/models.py](agent-models.py.md) (18 shared connections)
- [get_checkpointer](get_checkpointer.md) (12 shared connections)
- [typing](typing.md) (10 shared connections)
- [tickets/models.py](tickets-models.py.md) (10 shared connections)
- [TestConfigValidation](TestConfigValidation.md) (8 shared connections)
- [ConfigurationError](ConfigurationError.md) (6 shared connections)
- [ConversationService](ConversationService.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (3 shared connections)
- [test_api.py](test_api.py.md) (3 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [RAGGuardrails](RAGGuardrails.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py`
- `src/mcp_rag_agent/api/services/chat_service.py`
- `src/mcp_rag_agent/core/config.py`
- `src/mcp_rag_agent/observability/langsmith_integration.py`
- `tests/unit_tests/test_agent_creation.py`
- `tests/unit_tests/test_observability.py`
- `tests/unit_tests/test_session_memory.py`

## Audit Trail

- EXTRACTED: 91 (54%)
- INFERRED: 76 (46%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*