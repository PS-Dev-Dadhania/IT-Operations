# ConversationService

> 38 nodes · cohesion 0.10

## Key Concepts

- **ConversationService** (26 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **conversation_service.py** (22 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **schemas/__init__.py** (17 connections) — `src/mcp_rag_agent/api/schemas/__init__.py`
- **conversation.py** (12 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **ConversationThreadResponse** (11 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **ConversationHistoryResponse** (9 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **CreateConversationRequest** (9 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **DeleteConversationResponse** (9 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **create_conversation()** (7 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **ChatMessageItem** (7 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **api/services/__init__.py** (7 connections) — `src/mcp_rag_agent/api/services/__init__.py`
- **get_conversation_history()** (6 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **list_conversations()** (6 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **BaseModel** (5 connections)
- **.create_thread()** (5 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **.get_history()** (5 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **.__init__()** (4 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **.list_threads()** (4 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **.set_runner()** (3 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **post** (1 connections)
- **Delegates thread creation to ConversationService.** (1 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **Retrieves all tracked conversation threads.** (1 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **Retrieves conversation history or raises 404 if not found.** (1 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **Pydantic schemas for /api/v1/conversations endpoints.** (1 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- **Request model for creating a new isolated conversation thread.** (1 connections) — `src/mcp_rag_agent/api/schemas/conversation.py`
- *... and 13 more nodes in this community*

## Relationships

- [datetime](datetime.md) (16 shared connections)
- [typing](typing.md) (6 shared connections)
- [ChatService](ChatService.md) (6 shared connections)
- [agent/models.py](agent-models.py.md) (5 shared connections)
- [delete_conversation](delete_conversation.md) (4 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (4 shared connections)
- [tickets/models.py](tickets-models.py.md) (3 shared connections)
- [Config](Config.md) (3 shared connections)
- [dependencies.py](dependencies.py.md) (3 shared connections)
- [AdminAPIService](AdminAPIService.md) (2 shared connections)
- [pydantic](pydantic.md) (1 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/routes/conversations.py`
- `src/mcp_rag_agent/api/schemas/__init__.py`
- `src/mcp_rag_agent/api/schemas/conversation.py`
- `src/mcp_rag_agent/api/services/__init__.py`
- `src/mcp_rag_agent/api/services/conversation_service.py`

## Audit Trail

- EXTRACTED: 105 (85%)
- INFERRED: 19 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*