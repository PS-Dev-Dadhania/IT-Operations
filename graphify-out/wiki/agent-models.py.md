# agent/models.py

> 51 nodes · cohesion 0.07

## Key Concepts

- **agent/models.py** (35 connections) — `src/mcp_rag_agent/agent/models.py`
- **create_agent.py** (34 connections) — `src/mcp_rag_agent/agent/create_agent.py`
- **runner.py** (32 connections) — `src/mcp_rag_agent/agent/runner.py`
- **create_rag_agent_instance()** (29 connections) — `src/mcp_rag_agent/agent/create_agent.py`
- **app.py** (29 connections) — `src/mcp_rag_agent/api/app.py`
- **search_policy_documents_typed()** (26 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **SearchDocumentsInput** (22 connections) — `src/mcp_rag_agent/agent/models.py`
- **chat_service.py** (21 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **AgentResponse** (14 connections) — `src/mcp_rag_agent/agent/models.py`
- **create_search_documents_tool()** (12 connections) — `src/mcp_rag_agent/agent/create_agent.py`
- **agent/__init__.py** (12 connections) — `src/mcp_rag_agent/agent/__init__.py`
- **SearchDocumentsOutput** (11 connections) — `src/mcp_rag_agent/agent/models.py`
- **configure_langsmith_environment()** (11 connections) — `src/mcp_rag_agent/observability/langsmith_integration.py`
- **get_checkpointer_async()** (9 connections) — `src/mcp_rag_agent/core/checkpointer.py`
- **create_rag_agent()** (7 connections) — `src/mcp_rag_agent/agent/utils/rag_agent_creator.py`
- **search_policy_documents()** (7 connections) — `src/mcp_rag_agent/mcp_server/server.py`
- **search_documents()** (6 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **_async_search()** (5 connections) — `src/mcp_rag_agent/agent/create_agent.py`
- **lifespan()** (5 connections) — `src/mcp_rag_agent/api/app.py`
- **__getattr__()** (3 connections) — `src/mcp_rag_agent/agent/__init__.py`
- **.to_tool_string()** (3 connections) — `src/mcp_rag_agent/agent/models.py`
- **_sync_search_stub()** (2 connections) — `src/mcp_rag_agent/agent/create_agent.py`
- **demo()** (2 connections) — `src/mcp_rag_agent/agent/create_agent.py`
- **fastapi_exceptions** (1 connections)
- **fastapi_middleware_cors** (1 connections)
- *... and 26 more nodes in this community*

## Relationships

- [mcp_server/tools.py](mcp_server-tools.py.md) (36 shared connections)
- [typing](typing.md) (28 shared connections)
- [Config](Config.md) (18 shared connections)
- [ViolationType](ViolationType.md) (12 shared connections)
- [ObservabilityTracer](ObservabilityTracer.md) (12 shared connections)
- [ChatService](ChatService.md) (11 shared connections)
- [TestTypedToolInterface](TestTypedToolInterface.md) (11 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (9 shared connections)
- [.run](run.md) (6 shared connections)
- [test_api.py](test_api.py.md) (5 shared connections)
- [eval_runner.py](eval_runner.py.md) (5 shared connections)
- [RetrievedChunkOutput](RetrievedChunkOutput.md) (5 shared connections)

## Source Files

- `src/mcp_rag_agent/agent/__init__.py`
- `src/mcp_rag_agent/agent/create_agent.py`
- `src/mcp_rag_agent/agent/models.py`
- `src/mcp_rag_agent/agent/runner.py`
- `src/mcp_rag_agent/agent/utils/rag_agent_creator.py`
- `src/mcp_rag_agent/api/app.py`
- `src/mcp_rag_agent/api/services/chat_service.py`
- `src/mcp_rag_agent/core/checkpointer.py`
- `src/mcp_rag_agent/mcp_server/server.py`
- `src/mcp_rag_agent/mcp_server/tools.py`
- `src/mcp_rag_agent/observability/langsmith_integration.py`

## Audit Trail

- EXTRACTED: 229 (82%)
- INFERRED: 50 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*