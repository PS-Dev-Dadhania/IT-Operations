---
type: community
cohesion: 0.10
members: 25
---

# get_checkpointer

**Cohesion:** 0.10 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-test_checkpointer_initialization_with_mongodb()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_connection_failure_gracefully_degrades_to_memory()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_conversation_persistence_across_instances()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_feature_flag_disabled_returns_none()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_get_checkpointer_async_wrapper()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_missing_database_url_degrades_to_memory()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_missing_database_url_returns_none_if_no_fallback()]] - code - tests/unit_tests/test_session_memory.py
- [[dot-test_thread_isolation()]] - code - tests/unit_tests/test_session_memory.py
- [[BaseCheckpointSaver]] - code
- [[Ensure turn on thread_A does not leak into thread_B.]] - rationale - tests/unit_tests/test_session_memory.py
- [[Factory to construct a conversation checkpointer according to configuration. -…]] - rationale - src/mcp_rag_agent/core/checkpointer.py
- [[Simulate process restart state saved on thread_id is available to a new…]] - rationale - tests/unit_tests/test_session_memory.py
- [[Test suite for corecheckpointer.py factory and fallback logic.]] - rationale - tests/unit_tests/test_session_memory.py
- [[TestSessionMemoryCheckpointer]] - code - tests/unit_tests/test_session_memory.py
- [[Verify get_checkpointer_async executes asynchronously without blocking.]] - rationale - tests/unit_tests/test_session_memory.py
- [[When FEATURE_FLAG_SESSION_MEMORY_ENABLED=false, get_checkpointer returns None.]] - rationale - tests/unit_tests/test_session_memory.py
- [[When MongoDB connection succeeds, initializes MongoDBSaver with configured…]] - rationale - tests/unit_tests/test_session_memory.py
- [[When MongoDB ping times out or fails, catches exception and degrades to…]] - rationale - tests/unit_tests/test_session_memory.py
- [[When db_url or db_name is empty, degrades gracefully to MemorySaver.]] - rationale - tests/unit_tests/test_session_memory.py
- [[When fallback_on_error=False, returns None if configuration is missing.]] - rationale - tests/unit_tests/test_session_memory.py
- [[asyncio_7]] - code
- [[fake_ainvoke()]] - code - tests/unit_tests/test_session_memory.py
- [[fake_ainvoke()_1]] - code - tests/unit_tests/test_session_memory.py
- [[get_checkpointer()]] - code - src/mcp_rag_agent/core/checkpointer.py
- [[make_agent_graph()]] - code - tests/unit_tests/test_session_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_checkpointer
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Config]]
- 3 edges to [[_COMMUNITY_agentmodels.py]]
- 2 edges to [[_COMMUNITY_RAGAgentRunner]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 2 edges to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_AnswerGenerator]]
- 1 edge to [[_COMMUNITY_RunbookExecutor]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_typing]]

## Top bridge nodes
- [[get_checkpointer()]] - degree 13, connects to 6 communities
- [[asyncio_7]] - degree 7, connects to 3 communities
- [[TestSessionMemoryCheckpointer]] - degree 9, connects to 2 communities
- [[dot-test_checkpointer_initialization_with_mongodb()]] - degree 5, connects to 2 communities
- [[dot-test_connection_failure_gracefully_degrades_to_memory()]] - degree 5, connects to 2 communities