# ChatService

> 25 nodes · cohesion 0.14

## Key Concepts

- **ChatService** (21 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **routes/chat.py** (12 connections) — `src/mcp_rag_agent/api/routes/chat.py`
- **schemas/chat.py** (10 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **ChatRequest** (9 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **ChatResponse** (9 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **chat_endpoint()** (8 connections) — `src/mcp_rag_agent/api/routes/chat.py`
- **.execute_chat()** (8 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **ChatResponseMetadata** (7 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **SourceDocument** (7 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **get_chat_service()** (5 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **.get_runner()** (5 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **BaseModel** (4 connections)
- **Dependency provider for ChatService, retrieving from app.state.** (1 connections) — `src/mcp_rag_agent/api/dependencies.py`
- **post** (1 connections)
- **Request** (1 connections)
- **Conversational RAG chat endpoint.** (1 connections) — `src/mcp_rag_agent/api/routes/chat.py`
- **Delegates query execution to ChatService.** (1 connections) — `src/mcp_rag_agent/api/routes/chat.py`
- **Pydantic schemas for /api/v1/chat endpoint.** (1 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **Operational latency and grounding metadata (Zero-CoT safe).** (1 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **Detailed source document and chunk information for citation inspection.** (1 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **Response model for conversational chat endpoint.** (1 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **Request model for conversational chat endpoint.** (1 connections) — `src/mcp_rag_agent/api/schemas/chat.py`
- **Application service orchestrating RAGAgentRunner and enforcing Zero-CoT API…** (1 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **Lazily initialize or return the shared RAGAgentRunner.** (1 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **Execute chat request through the agent runner and map to Zero-CoT response.…** (1 connections) — `src/mcp_rag_agent/api/services/chat_service.py`

## Relationships

- [agent/models.py](agent-models.py.md) (11 shared connections)
- [ConversationService](ConversationService.md) (6 shared connections)
- [dependencies.py](dependencies.py.md) (4 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (3 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [typing](typing.md) (2 shared connections)
- [Config](Config.md) (2 shared connections)
- [pydantic](pydantic.md) (1 shared connections)
- [test_api.py](test_api.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/dependencies.py`
- `src/mcp_rag_agent/api/routes/chat.py`
- `src/mcp_rag_agent/api/schemas/chat.py`
- `src/mcp_rag_agent/api/services/chat_service.py`

## Audit Trail

- EXTRACTED: 64 (85%)
- INFERRED: 11 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*