---
type: community
cohesion: 0.10
members: 38
---

# ConversationService

**Cohesion:** 0.10 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_13]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[dot-create_thread()]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[dot-get_history()]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[dot-list_threads()]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[dot-set_runner()]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[Any_6]] - code
- [[Application service for managing conversation threads and session state.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[Application services layer for MCP RAG Agent.]] - rationale - src/mcp_rag_agent/api/services/__init__.py
- [[BaseModel_5]] - code
- [[ChatMessageItem]] - code - src/mcp_rag_agent/api/schemas/conversation.py
- [[Clean representation of a dialogue turn (Zero-CoT safe).]] - rationale - src/mcp_rag_agent/api/schemas/conversation.py
- [[ConversationHistoryResponse]] - code - src/mcp_rag_agent/api/schemas/conversation.py
- [[ConversationService]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[ConversationThreadResponse]] - code - src/mcp_rag_agent/api/schemas/conversation.py
- [[Create a new isolated conversation thread with tracked metadata.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[CreateConversationRequest]] - code - src/mcp_rag_agent/api/schemas/conversation.py
- [[Delegates thread creation to ConversationService.]] - rationale - src/mcp_rag_agent/api/routes/conversations.py
- [[DeleteConversationResponse]] - code - src/mcp_rag_agent/api/schemas/conversation.py
- [[Dynamically attach or update the agent runner.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[List all active conversation threads ordered by creation time descending.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[Orchestrates conversation thread lifecycles and dialogue history.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[Public schema exports for API models.]] - rationale - src/mcp_rag_agent/api/schemas/__init__.py
- [[Pydantic schemas for apiv1conversations endpoints.]] - rationale - src/mcp_rag_agent/api/schemas/conversation.py
- [[Request model for creating a new isolated conversation thread.]] - rationale - src/mcp_rag_agent/api/schemas/conversation.py
- [[Response model containing conversation dialogue history.]] - rationale - src/mcp_rag_agent/api/schemas/conversation.py
- [[Response model for conversation deletion.]] - rationale - src/mcp_rag_agent/api/schemas/conversation.py
- [[Response model representing an active conversation thread.]] - rationale - src/mcp_rag_agent/api/schemas/conversation.py
- [[Retrieve clean dialogue history for a thread, enforcing Zero-CoT output.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[Retrieves all tracked conversation threads.]] - rationale - src/mcp_rag_agent/api/routes/conversations.py
- [[Retrieves conversation history or raises 404 if not found.]] - rationale - src/mcp_rag_agent/api/routes/conversations.py
- [[apiservices__init__.py]] - code - src/mcp_rag_agent/api/services/__init__.py
- [[conversation.py]] - code - src/mcp_rag_agent/api/schemas/conversation.py
- [[conversation_service.py]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[create_conversation()]] - code - src/mcp_rag_agent/api/routes/conversations.py
- [[get_conversation_history()]] - code - src/mcp_rag_agent/api/routes/conversations.py
- [[list_conversations()]] - code - src/mcp_rag_agent/api/routes/conversations.py
- [[post_1]] - code
- [[schemas__init__.py]] - code - src/mcp_rag_agent/api/schemas/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConversationService
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_datetime]]
- 6 edges to [[_COMMUNITY_ChatService]]
- 6 edges to [[_COMMUNITY_typing]]
- 5 edges to [[_COMMUNITY_agentmodels.py]]
- 4 edges to [[_COMMUNITY_delete_conversation]]
- 4 edges to [[_COMMUNITY_RAGAgentRunner]]
- 3 edges to [[_COMMUNITY_ticketsmodels.py]]
- 3 edges to [[_COMMUNITY_dependencies.py]]
- 3 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_AdminAPIService]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]

## Top bridge nodes
- [[ConversationService]] - degree 26, connects to 7 communities
- [[conversation_service.py]] - degree 22, connects to 7 communities
- [[schemas__init__.py]] - degree 17, connects to 3 communities
- [[conversation.py]] - degree 12, connects to 3 communities
- [[apiservices__init__.py]] - degree 7, connects to 3 communities