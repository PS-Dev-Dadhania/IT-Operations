# get_checkpointer

> 25 nodes · cohesion 0.10

## Key Concepts

- **get_checkpointer()** (13 connections) — `src/mcp_rag_agent/core/checkpointer.py`
- **TestSessionMemoryCheckpointer** (9 connections) — `tests/unit_tests/test_session_memory.py`
- **asyncio** (7 connections)
- **.test_checkpointer_initialization_with_mongodb()** (5 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_connection_failure_gracefully_degrades_to_memory()** (5 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_get_checkpointer_async_wrapper()** (5 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_conversation_persistence_across_instances()** (5 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_thread_isolation()** (5 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_feature_flag_disabled_returns_none()** (4 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_missing_database_url_degrades_to_memory()** (4 connections) — `tests/unit_tests/test_session_memory.py`
- **.test_missing_database_url_returns_none_if_no_fallback()** (4 connections) — `tests/unit_tests/test_session_memory.py`
- **make_agent_graph()** (3 connections) — `tests/unit_tests/test_session_memory.py`
- **BaseCheckpointSaver** (2 connections)
- **fake_ainvoke()** (2 connections) — `tests/unit_tests/test_session_memory.py`
- **Factory to construct a conversation checkpointer according to configuration. -…** (1 connections) — `src/mcp_rag_agent/core/checkpointer.py`
- **Verify get_checkpointer_async executes asynchronously without blocking.** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **Ensure turn on thread_A does not leak into thread_B.** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **Simulate process restart: state saved on thread_id is available to a new…** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **Test suite for core/checkpointer.py factory and fallback logic.** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **When FEATURE_FLAG_SESSION_MEMORY_ENABLED=false, get_checkpointer returns None.** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **When db_url or db_name is empty, degrades gracefully to MemorySaver.** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **When fallback_on_error=False, returns None if configuration is missing.** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **When MongoDB connection succeeds, initializes MongoDBSaver with configured…** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **When MongoDB ping times out or fails, catches exception and degrades to…** (1 connections) — `tests/unit_tests/test_session_memory.py`
- **fake_ainvoke()** (1 connections) — `tests/unit_tests/test_session_memory.py`

## Relationships

- [Config](Config.md) (12 shared connections)
- [agent/models.py](agent-models.py.md) (3 shared connections)
- [unittest_mock](unittest_mock.md) (2 shared connections)
- [tickets/models.py](tickets-models.py.md) (2 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (2 shared connections)
- [audit.py](audit.py.md) (1 shared connections)
- [RunbookExecutor](RunbookExecutor.md) (1 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (1 shared connections)
- [typing](typing.md) (1 shared connections)
- [AnswerGenerator](AnswerGenerator.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/core/checkpointer.py`
- `tests/unit_tests/test_session_memory.py`

## Audit Trail

- EXTRACTED: 34 (62%)
- INFERRED: 21 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*