---
type: community
cohesion: 0.14
members: 25
---

# ChatService

**Cohesion:** 0.14 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-execute_chat()]] - code - src/mcp_rag_agent/api/services/chat_service.py
- [[dot-get_runner()]] - code - src/mcp_rag_agent/api/services/chat_service.py
- [[Application service orchestrating RAGAgentRunner and enforcing Zero-CoT API…]] - rationale - src/mcp_rag_agent/api/services/chat_service.py
- [[BaseModel_16]] - code
- [[ChatRequest]] - code - src/mcp_rag_agent/api/schemas/chat.py
- [[ChatResponse]] - code - src/mcp_rag_agent/api/schemas/chat.py
- [[ChatResponseMetadata]] - code - src/mcp_rag_agent/api/schemas/chat.py
- [[ChatService]] - code - src/mcp_rag_agent/api/services/chat_service.py
- [[Conversational RAG chat endpoint.]] - rationale - src/mcp_rag_agent/api/routes/chat.py
- [[Delegates query execution to ChatService.]] - rationale - src/mcp_rag_agent/api/routes/chat.py
- [[Dependency provider for ChatService, retrieving from app.state.]] - rationale - src/mcp_rag_agent/api/dependencies.py
- [[Detailed source document and chunk information for citation inspection.]] - rationale - src/mcp_rag_agent/api/schemas/chat.py
- [[Execute chat request through the agent runner and map to Zero-CoT response.…]] - rationale - src/mcp_rag_agent/api/services/chat_service.py
- [[Lazily initialize or return the shared RAGAgentRunner.]] - rationale - src/mcp_rag_agent/api/services/chat_service.py
- [[Operational latency and grounding metadata (Zero-CoT safe).]] - rationale - src/mcp_rag_agent/api/schemas/chat.py
- [[Pydantic schemas for apiv1chat endpoint.]] - rationale - src/mcp_rag_agent/api/schemas/chat.py
- [[Request]] - code
- [[Request model for conversational chat endpoint.]] - rationale - src/mcp_rag_agent/api/schemas/chat.py
- [[Response model for conversational chat endpoint.]] - rationale - src/mcp_rag_agent/api/schemas/chat.py
- [[SourceDocument]] - code - src/mcp_rag_agent/api/schemas/chat.py
- [[chat_endpoint()]] - code - src/mcp_rag_agent/api/routes/chat.py
- [[get_chat_service()]] - code - src/mcp_rag_agent/api/dependencies.py
- [[post_2]] - code
- [[routeschat.py]] - code - src/mcp_rag_agent/api/routes/chat.py
- [[schemaschat.py]] - code - src/mcp_rag_agent/api/schemas/chat.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ChatService
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_agentmodels.py]]
- 6 edges to [[_COMMUNITY_ConversationService]]
- 4 edges to [[_COMMUNITY_dependencies.py]]
- 3 edges to [[_COMMUNITY_RAGAgentRunner]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_datetime]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[ChatService]] - degree 21, connects to 6 communities
- [[routeschat.py]] - degree 12, connects to 4 communities
- [[schemaschat.py]] - degree 10, connects to 4 communities
- [[ChatRequest]] - degree 9, connects to 2 communities
- [[ChatResponse]] - degree 9, connects to 2 communities