---
source_file: "src/mcp_rag_agent/mcp_server/tools.py"
type: "code"
community: "mcp_server/tools.py"
location: "L565"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/mcp_server/toolspy
---

# get_user_context_typed()

## Connections
- [[Any_3]] - `references` [EXTRACTED]
- [[Execute typed get_user_context MCP tool with privacy masking, authorization,…]] - `rationale_for` [EXTRACTED]
- [[GetUserContextInput]] - `uses` [INFERRED]
- [[GetUserContextOutput]] - `calls` [EXTRACTED]
- [[UserNotFoundError]] - `uses` [INFERRED]
- [[_async_call()_4]] - `calls` [EXTRACTED]
- [[create_user_context_tool()]] - `calls` [EXTRACTED]
- [[get_audit_service()]] - `calls` [EXTRACTED]
- [[get_authorization_service()]] - `calls` [EXTRACTED]
- [[get_current_subject()]] - `calls` [EXTRACTED]
- [[get_current_tracer()]] - `calls` [EXTRACTED]
- [[get_request_id()]] - `calls` [EXTRACTED]
- [[get_user_context()]] - `calls` [EXTRACTED]
- [[get_user_service()]] - `calls` [EXTRACTED]
- [[it_supporttools.py]] - `imports` [EXTRACTED]
- [[mask_sensitive()]] - `calls` [EXTRACTED]
- [[mcp_servertools.py]] - `contains` [EXTRACTED]
- [[server.py]] - `imports` [EXTRACTED]
- [[test_get_user_context_not_found()]] - `calls` [INFERRED]
- [[test_get_user_context_success()]] - `calls` [INFERRED]
- [[test_tool_authorization_denial_emits_audit_log()]] - `calls` [INFERRED]
- [[test_tool_authorization_success_emits_audit_log()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/mcp_server/toolspy