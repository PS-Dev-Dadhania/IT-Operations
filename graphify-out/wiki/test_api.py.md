# test_api.py

> 43 nodes · cohesion 0.05

## Key Concepts

- **test_api.py** (30 connections) — `tests/unit_tests/test_api.py`
- **create_app()** (24 connections) — `src/mcp_rag_agent/api/app.py`
- **test_readiness_endpoint_connected()** (5 connections) — `tests/unit_tests/test_api.py`
- **client()** (4 connections) — `tests/unit_tests/test_api.py`
- **test_readiness_endpoint_disconnected()** (4 connections) — `tests/unit_tests/test_api.py`
- **api/__init__.py** (3 connections) — `src/mcp_rag_agent/api/__init__.py`
- **test_chat_internal_error_handling()** (3 connections) — `tests/unit_tests/test_api.py`
- **fixture** (2 connections)
- **test_chat_custom_request_id_header()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_chat_endpoint_success()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_chat_validation_error_empty_message()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_conversation_not_found()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_create_and_get_conversation()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_delete_conversation()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_get_conversation_history_with_turns()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_health_endpoint()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_list_conversations_endpoint()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_root_and_openapi_docs()** (2 connections) — `tests/unit_tests/test_api.py`
- **test_static_ui_serving()** (2 connections) — `tests/unit_tests/test_api.py`
- **mcp_rag_agent_api_services_chat_service** (1 connections)
- **mcp_rag_agent_api_services_conversation_service** (1 connections)
- **http_exception_handler()** (1 connections) — `src/mcp_rag_agent/api/app.py`
- **root_endpoint()** (1 connections) — `src/mcp_rag_agent/api/app.py`
- **unhandled_exception_handler()** (1 connections) — `src/mcp_rag_agent/api/app.py`
- **validation_exception_handler()** (1 connections) — `src/mcp_rag_agent/api/app.py`
- *... and 18 more nodes in this community*

## Relationships

- [agent/models.py](agent-models.py.md) (5 shared connections)
- [.run](run.md) (4 shared connections)
- [unittest_mock](unittest_mock.md) (4 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (3 shared connections)
- [Config](Config.md) (3 shared connections)
- [typing](typing.md) (2 shared connections)
- [ConversationService](ConversationService.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [datetime](datetime.md) (1 shared connections)
- [TestAPIIntegration](TestAPIIntegration.md) (1 shared connections)
- [IncidentRecord](IncidentRecord.md) (1 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/__init__.py`
- `src/mcp_rag_agent/api/app.py`
- `tests/unit_tests/test_api.py`

## Audit Trail

- EXTRACTED: 61 (80%)
- INFERRED: 15 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*