---
type: community
cohesion: 0.07
members: 51
---

# agent/models.py

**Cohesion:** 0.07 - loosely connected
**Members:** 51 nodes

## Members
- [[dot-to_tool_string()_5]] - code - src/mcp_rag_agent/agent/models.py
- [[Agent module for production MCP RAG Agent.]] - rationale - src/mcp_rag_agent/agent/__init__.py
- [[AgentResponse]] - code - src/mcp_rag_agent/agent/models.py
- [[Any_28]] - code
- [[Any_29]] - code
- [[Any_30]] - code
- [[Application service for conversational chat execution with Zero-CoT guarantees.]] - rationale - src/mcp_rag_agent/api/services/chat_service.py
- [[Asynchronous wrapper to initialize checkpointer off the event loop thread.]] - rationale - src/mcp_rag_agent/core/checkpointer.py
- [[BaseTool_1]] - code
- [[Create LangChain StructuredTool for searching policy documents with strong…]] - rationale - src/mcp_rag_agent/agent/create_agent.py
- [[Data models for production agent architecture, typed tool schemas, and…]] - rationale - src/mcp_rag_agent/agent/models.py
- [[Execute typed search_policy_documents tool with robust error handling and…]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Explicit async factory to create a production RAG agent with structured runner.…]] - rationale - src/mcp_rag_agent/agent/create_agent.py
- [[Factory entry point for creating production RAG agents in Direct or MCP modes.]] - rationale - src/mcp_rag_agent/agent/create_agent.py
- [[FastAPI application factory for MCP RAG Agent Production API Layer.]] - rationale - src/mcp_rag_agent/api/app.py
- [[Format output into clear, grounded text representation for LLM context…]] - rationale - src/mcp_rag_agent/agent/models.py
- [[Input schema for the search_policy_documents retrieval tool.]] - rationale - src/mcp_rag_agent/agent/models.py
- [[Lazy import for create_agent symbols to break circular import cycle.…]] - rationale - src/mcp_rag_agent/agent/__init__.py
- [[Perform hybrid search on indexed documents using vector and text search.…]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Production Agent Runner coordinating explicit responsibilities, citation…]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Production response container produced by the RAG agent.]] - rationale - src/mcp_rag_agent/agent/models.py
- [[Returns a LangGraph compiled graph that - Uses ChatOpenAI as the LLM - Can…_1]] - rationale - src/mcp_rag_agent/agent/utils/rag_agent_creator.py
- [[Search stored company policy documents using hybrid semantic and keyword…]] - rationale - src/mcp_rag_agent/mcp_server/server.py
- [[SearchDocumentsInput]] - code - src/mcp_rag_agent/agent/models.py
- [[SearchDocumentsOutput]] - code - src/mcp_rag_agent/agent/models.py
- [[Set standard LangChainLangSmith environment variables if enabled. Returns…]] - rationale - src/mcp_rag_agent/observability/langsmith_integration.py
- [[Strongly typed output schema returned by the retrieval tool.]] - rationale - src/mcp_rag_agent/agent/models.py
- [[StructuredTool_2]] - code
- [[__getattr__()]] - code - src/mcp_rag_agent/agent/__init__.py
- [[_async_search()]] - code - src/mcp_rag_agent/agent/create_agent.py
- [[_sync_search_stub()]] - code - src/mcp_rag_agent/agent/create_agent.py
- [[agent__init__.py]] - code - src/mcp_rag_agent/agent/__init__.py
- [[agentmodels.py]] - code - src/mcp_rag_agent/agent/models.py
- [[app.py]] - code - src/mcp_rag_agent/api/app.py
- [[chat_service.py]] - code - src/mcp_rag_agent/api/services/chat_service.py
- [[configure_langsmith_environment()]] - code - src/mcp_rag_agent/observability/langsmith_integration.py
- [[create_agent.py]] - code - src/mcp_rag_agent/agent/create_agent.py
- [[create_rag_agent()]] - code - src/mcp_rag_agent/agent/utils/rag_agent_creator.py
- [[create_rag_agent_instance()]] - code - src/mcp_rag_agent/agent/create_agent.py
- [[create_search_documents_tool()]] - code - src/mcp_rag_agent/agent/create_agent.py
- [[demo()]] - code - src/mcp_rag_agent/agent/create_agent.py
- [[fastapi_exceptions]] - concept
- [[fastapi_middleware_cors]] - concept
- [[fastapi_responses]] - concept
- [[fastapi_staticfiles]] - concept
- [[get_checkpointer_async()]] - code - src/mcp_rag_agent/core/checkpointer.py
- [[lifespan()]] - code - src/mcp_rag_agent/api/app.py
- [[runner.py]] - code - src/mcp_rag_agent/agent/runner.py
- [[search_documents()_1]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[search_policy_documents()]] - code - src/mcp_rag_agent/mcp_server/server.py
- [[search_policy_documents_typed()]] - code - src/mcp_rag_agent/mcp_server/tools.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agent/modelspy
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_mcp_servertools.py]]
- 28 edges to [[_COMMUNITY_typing]]
- 18 edges to [[_COMMUNITY_Config]]
- 12 edges to [[_COMMUNITY_ObservabilityTracer]]
- 12 edges to [[_COMMUNITY_ViolationType]]
- 11 edges to [[_COMMUNITY_ChatService]]
- 11 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 9 edges to [[_COMMUNITY_RAGAgentRunner]]
- 6 edges to [[_COMMUNITY_dot-run]]
- 5 edges to [[_COMMUNITY_eval_runner.py]]
- 5 edges to [[_COMMUNITY_ConversationService]]
- 5 edges to [[_COMMUNITY_RetrievedChunkOutput]]
- 5 edges to [[_COMMUNITY_test_api.py]]
- 3 edges to [[_COMMUNITY_RAGGuardrails]]
- 3 edges to [[_COMMUNITY_TestMCPIntegration]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_get_checkpointer]]
- 2 edges to [[_COMMUNITY_RunbookExecutor]]
- 2 edges to [[_COMMUNITY_test_runbooks.py]]
- 2 edges to [[_COMMUNITY_TestDirectAndMCPParity]]
- 2 edges to [[_COMMUNITY_datetime]]
- 2 edges to [[_COMMUNITY_prompts__init__.py]]
- 2 edges to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_AnswerGenerator]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]

## Top bridge nodes
- [[runner.py]] - degree 32, connects to 12 communities
- [[create_rag_agent_instance()]] - degree 29, connects to 10 communities
- [[app.py]] - degree 29, connects to 10 communities
- [[agentmodels.py]] - degree 35, connects to 9 communities
- [[create_agent.py]] - degree 34, connects to 7 communities