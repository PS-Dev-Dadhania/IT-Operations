---
type: community
cohesion: 0.05
members: 53
---

# Config

**Cohesion:** 0.05 - loosely connected
**Members:** 53 nodes

## Members
- [[- Connects to your MCP server via MultiServerMCPClient - Loads all MCP tools as…]] - rationale - src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py
- [[dot-__init__()_36]] - code - src/mcp_rag_agent/api/services/chat_service.py
- [[dot-test_configure_langsmith_environment()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_create_rag_agent_instance_direct_mode()]] - code - tests/unit_tests/test_agent_creation.py
- [[dot-test_create_rag_agent_instance_mcp_mode()]] - code - tests/unit_tests/test_agent_creation.py
- [[dot-test_create_rag_agent_instance_raises_without_credentials()]] - code - tests/unit_tests/test_agent_creation.py
- [[dot-test_direct_mode_agent_creation_wires_checkpointer()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_get_langchain_run_config()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_is_langsmith_enabled_false_when_unconfigured()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_is_langsmith_enabled_true_when_configured()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_mcp_mode_agent_creation_wires_checkpointer()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_no_import_time_side_effects()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_search_documents_tool_metadata()]] - code - tests/unit_tests/test_agent_creation.py
- [[dot-validate_all()]] - code - src/mcp_rag_agent/core/config.py
- [[dot-validate_database_config()]] - code - src/mcp_rag_agent/core/config.py
- [[dot-validate_llm_config()]] - code - src/mcp_rag_agent/core/config.py
- [[Any_20]] - code
- [[Any_21]] - code
- [[Any_22]] - code
- [[BaseSettings]] - code
- [[BaseTool]] - code
- [[Build LangChain execution config containing metadata, thread ID, and run tags.…]] - rationale - src/mcp_rag_agent/observability/langsmith_integration.py
- [[Build MCP connection configuration dictionary supporting stdio or network SSE…]] - rationale - src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py
- [[Check if LangSmith tracing is actively enabled with a valid API key.]] - rationale - src/mcp_rag_agent/observability/langsmith_integration.py
- [[Config]] - code - src/mcp_rag_agent/core/config.py
- [[Configuration settings for the MCP RAG Agent.]] - rationale - src/mcp_rag_agent/core/config.py
- [[Ensure checkpointer module import causes no network calls or event loop side…]] - rationale - tests/unit_tests/test_session_memory.py
- [[Returns a LangGraph compiled graph that - Uses ChatOpenAI as the LLM - Can…]] - rationale - src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py
- [[Test LangSmith configuration, environment variables, and run config generation.]] - rationale - tests/unit_tests/test_observability.py
- [[Test suite for agent creation in Direct and MCP modes.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[Test suite for thread isolation and multi-turn state persistence.]] - rationale - tests/unit_tests/test_session_memory.py
- [[TestAgentCreation]] - code - tests/unit_tests/test_agent_creation.py
- [[TestLangSmithIntegration]] - code - tests/unit_tests/test_observability.py
- [[TestThreadIsolationAndPersistence]] - code - tests/unit_tests/test_session_memory.py
- [[Validate LLM configuration settings. Raises ConfigurationError if invalid.]] - rationale - src/mcp_rag_agent/core/config.py
- [[Validate all required configurations.]] - rationale - src/mcp_rag_agent/core/config.py
- [[Validate database configuration settings. Raises ConfigurationError if invalid.]] - rationale - src/mcp_rag_agent/core/config.py
- [[Verify Direct mode agent receives checkpointer.]] - rationale - tests/unit_tests/test_session_memory.py
- [[Verify LangSmith is reported as disabled when tracing flag is false or key is…]] - rationale - tests/unit_tests/test_observability.py
- [[Verify LangSmith reports true when both flag and key are provided.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify MCP mode agent receives checkpointer.]] - rationale - tests/unit_tests/test_session_memory.py
- [[Verify environment variables are set when LangSmith is enabled.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify factory in MCP mode delegates to create_mcp_rag_agent.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[Verify factory in direct mode creates an agent with StructuredTool.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[Verify factory raises ConfigurationError when credentials are missing.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[Verify run config contains required metadata, tags, and run_name.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify the structured tool has the expected name and schema.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[_load_mcp_tools_and_prompt()]] - code - src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py
- [[asyncio_11]] - code
- [[create_mcp_rag_agent()]] - code - src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py
- [[get_langchain_run_config()]] - code - src/mcp_rag_agent/observability/langsmith_integration.py
- [[get_mcp_connections()]] - code - src/mcp_rag_agent/agent/utils/mcp_rag_agent_creator.py
- [[is_langsmith_enabled()]] - code - src/mcp_rag_agent/observability/langsmith_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Config
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_agentmodels.py]]
- 12 edges to [[_COMMUNITY_get_checkpointer]]
- 10 edges to [[_COMMUNITY_typing]]
- 10 edges to [[_COMMUNITY_ticketsmodels.py]]
- 8 edges to [[_COMMUNITY_TestConfigValidation]]
- 6 edges to [[_COMMUNITY_ConfigurationError]]
- 3 edges to [[_COMMUNITY_ConversationService]]
- 3 edges to [[_COMMUNITY_mcp_servertools.py]]
- 3 edges to [[_COMMUNITY_test_api.py]]
- 2 edges to [[_COMMUNITY_RAGAgentRunner]]
- 2 edges to [[_COMMUNITY_AnswerGenerator]]
- 2 edges to [[_COMMUNITY_ChatService]]
- 2 edges to [[_COMMUNITY_RAGGuardrails]]
- 2 edges to [[_COMMUNITY_dependencies.py]]
- 2 edges to [[_COMMUNITY_datetime]]
- 2 edges to [[_COMMUNITY_TestAPIIntegration]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 2 edges to [[_COMMUNITY_ObservabilityTracer]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_test_observability.py]]
- 1 edge to [[_COMMUNITY_dot-run]]

## Top bridge nodes
- [[Config]] - degree 80, connects to 18 communities
- [[TestThreadIsolationAndPersistence]] - degree 11, connects to 4 communities
- [[get_langchain_run_config()]] - degree 8, connects to 4 communities
- [[TestAgentCreation]] - degree 9, connects to 3 communities
- [[is_langsmith_enabled()]] - degree 7, connects to 3 communities