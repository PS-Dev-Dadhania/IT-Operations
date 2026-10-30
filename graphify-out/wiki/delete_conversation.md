# delete_conversation

> 5 nodes · cohesion 0.40

## Key Concepts

- **delete_conversation()** (6 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **.delete_thread()** (4 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`
- **delete** (1 connections)
- **Purges conversation checkpoints or raises 404 if not found.** (1 connections) — `src/mcp_rag_agent/api/routes/conversations.py`
- **Purge thread state from checkpointer and active registry.** (1 connections) — `src/mcp_rag_agent/api/services/conversation_service.py`

## Relationships

- [ConversationService](ConversationService.md) (4 shared connections)
- [datetime](datetime.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/routes/conversations.py`
- `src/mcp_rag_agent/api/services/conversation_service.py`

## Audit Trail

- EXTRACTED: 6 (67%)
- INFERRED: 3 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*