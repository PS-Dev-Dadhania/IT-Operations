---
source_file: "src/mcp_rag_agent/api/app.py"
type: "code"
community: "test_api.py"
location: "L28"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_apipy
---

# create_app()

## Connections
- [[dot-app_client()]] - `calls` [INFERRED]
- [[ChatService]] - `calls` [EXTRACTED]
- [[Config]] - `uses` [INFERRED]
- [[ConversationService]] - `calls` [EXTRACTED]
- [[CorrelationIdMiddleware]] - `uses` [INFERRED]
- [[Factory function to build and configure the FastAPI application. Args cfg…]] - `rationale_for` [EXTRACTED]
- [[FastAPI]] - `references` [EXTRACTED]
- [[RAGAgentRunner]] - `uses` [INFERRED]
- [[_build_test_client()]] - `calls` [INFERRED]
- [[api__init__.py]] - `imports` [EXTRACTED]
- [[app.py]] - `contains` [EXTRACTED]
- [[client()]] - `calls` [INFERRED]
- [[configure_langsmith_environment()]] - `calls` [EXTRACTED]
- [[create_rag_agent_instance()]] - `calls` [EXTRACTED]
- [[http_exception_handler()]] - `contains` [EXTRACTED]
- [[lifespan()]] - `indirect_call` [INFERRED]
- [[root_endpoint()]] - `contains` [EXTRACTED]
- [[test_chat_endpoint_with_structured_sources()]] - `calls` [INFERRED]
- [[test_chat_internal_error_handling()]] - `calls` [INFERRED]
- [[test_readiness_endpoint_connected()]] - `calls` [INFERRED]
- [[test_readiness_endpoint_disconnected()]] - `calls` [INFERRED]
- [[test_setup()]] - `calls` [INFERRED]
- [[unhandled_exception_handler()]] - `contains` [EXTRACTED]
- [[validation_exception_handler()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_apipy