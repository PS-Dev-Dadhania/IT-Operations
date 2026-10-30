---
type: community
cohesion: 0.40
members: 5
---

# delete_conversation

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-delete_thread()]] - code - src/mcp_rag_agent/api/services/conversation_service.py
- [[Purge thread state from checkpointer and active registry.]] - rationale - src/mcp_rag_agent/api/services/conversation_service.py
- [[Purges conversation checkpoints or raises 404 if not found.]] - rationale - src/mcp_rag_agent/api/routes/conversations.py
- [[delete]] - code
- [[delete_conversation()]] - code - src/mcp_rag_agent/api/routes/conversations.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/delete_conversation
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ConversationService]]
- 1 edge to [[_COMMUNITY_datetime]]

## Top bridge nodes
- [[delete_conversation()]] - degree 6, connects to 2 communities
- [[dot-delete_thread()]] - degree 4, connects to 1 community