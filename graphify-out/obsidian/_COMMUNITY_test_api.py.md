---
type: community
cohesion: 0.05
members: 43
---

# test_api.py

**Cohesion:** 0.05 - loosely connected
**Members:** 43 nodes

## Members
- [[Factory function to build and configure the FastAPI application. Args cfg…]] - rationale - src/mcp_rag_agent/api/app.py
- [[FastAPI Production API Layer package for MCP RAG Agent.]] - rationale - src/mcp_rag_agent/api/__init__.py
- [[TestClient fixture initialized with mock runner.]] - rationale - tests/unit_tests/test_api.py
- [[Unit and integration tests for Phase 9 Production API Layer.]] - rationale - tests/unit_tests/test_api.py
- [[Verify DELETE apiv1conversations{thread_id} purges thread state.]] - rationale - tests/unit_tests/test_api.py
- [[Verify GET apiv1conversations lists active threads with metadata.]] - rationale - tests/unit_tests/test_api.py
- [[Verify GET apiv1conversations{thread_id} extracts clean dialogue, omitting…]] - rationale - tests/unit_tests/test_api.py
- [[Verify GET apiv1health liveness probe.]] - rationale - tests/unit_tests/test_api.py
- [[Verify GET apiv1ready returns 503 when database is unreachable.]] - rationale - tests/unit_tests/test_api.py
- [[Verify GET apiv1ready when database is connected and model configured.]] - rationale - tests/unit_tests/test_api.py
- [[Verify GET and DELETE on non-existent thread ID return 404.]] - rationale - tests/unit_tests/test_api.py
- [[Verify POST apiv1chat returns 422 for empty or missing message.]] - rationale - tests/unit_tests/test_api.py
- [[Verify POST apiv1chat returns structured Zero-CoT response.]] - rationale - tests/unit_tests/test_api.py
- [[Verify POST apiv1conversations and subsequent GET.]] - rationale - tests/unit_tests/test_api.py
- [[Verify Phase 10 enterprise web UI assets are properly served under ui.]] - rationale - tests/unit_tests/test_api.py
- [[Verify client-supplied X-Request-ID is honored across headers and response.]] - rationale - tests/unit_tests/test_api.py
- [[Verify root endpoint and OpenAPI schema documentation.]] - rationale - tests/unit_tests/test_api.py
- [[Verify unhandled exceptions during agent execution return structured 500 error.]] - rationale - tests/unit_tests/test_api.py
- [[api__init__.py]] - code - src/mcp_rag_agent/api/__init__.py
- [[client()]] - code - tests/unit_tests/test_api.py
- [[create_app()]] - code - src/mcp_rag_agent/api/app.py
- [[fixture_2]] - code
- [[http_exception_handler()]] - code - src/mcp_rag_agent/api/app.py
- [[mcp_rag_agent_api_services_chat_service]] - concept
- [[mcp_rag_agent_api_services_conversation_service]] - concept
- [[root_endpoint()]] - code - src/mcp_rag_agent/api/app.py
- [[test_api.py]] - code - tests/unit_tests/test_api.py
- [[test_chat_custom_request_id_header()]] - code - tests/unit_tests/test_api.py
- [[test_chat_endpoint_success()]] - code - tests/unit_tests/test_api.py
- [[test_chat_internal_error_handling()]] - code - tests/unit_tests/test_api.py
- [[test_chat_validation_error_empty_message()]] - code - tests/unit_tests/test_api.py
- [[test_conversation_not_found()]] - code - tests/unit_tests/test_api.py
- [[test_create_and_get_conversation()]] - code - tests/unit_tests/test_api.py
- [[test_delete_conversation()]] - code - tests/unit_tests/test_api.py
- [[test_get_conversation_history_with_turns()]] - code - tests/unit_tests/test_api.py
- [[test_health_endpoint()]] - code - tests/unit_tests/test_api.py
- [[test_list_conversations_endpoint()]] - code - tests/unit_tests/test_api.py
- [[test_readiness_endpoint_connected()]] - code - tests/unit_tests/test_api.py
- [[test_readiness_endpoint_disconnected()]] - code - tests/unit_tests/test_api.py
- [[test_root_and_openapi_docs()]] - code - tests/unit_tests/test_api.py
- [[test_static_ui_serving()]] - code - tests/unit_tests/test_api.py
- [[unhandled_exception_handler()]] - code - src/mcp_rag_agent/api/app.py
- [[validation_exception_handler()]] - code - src/mcp_rag_agent/api/app.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_apipy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_agentmodels.py]]
- 4 edges to [[_COMMUNITY_dot-run]]
- 4 edges to [[_COMMUNITY_unittest_mock]]
- 3 edges to [[_COMMUNITY_Config]]
- 3 edges to [[_COMMUNITY_test_admin_api.py]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_ConversationService]]
- 1 edge to [[_COMMUNITY_RAGAgentRunner]]
- 1 edge to [[_COMMUNITY_ChatService]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_TestAPIIntegration]]
- 1 edge to [[_COMMUNITY_datetime]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_test_observability.py]]

## Top bridge nodes
- [[create_app()]] - degree 24, connects to 11 communities
- [[test_api.py]] - degree 30, connects to 6 communities
- [[test_readiness_endpoint_connected()]] - degree 5, connects to 2 communities
- [[test_readiness_endpoint_disconnected()]] - degree 4, connects to 1 community
- [[api__init__.py]] - degree 3, connects to 1 community