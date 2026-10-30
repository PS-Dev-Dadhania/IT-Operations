---
source_file: "src/mcp_rag_agent/mcp_server/tools.py"
type: "code"
community: "mcp_server/tools.py"
location: "L1098"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/mcp_server/toolspy
---

# update_ticket_typed()

## Connections
- [[Any_3]] - `references` [EXTRACTED]
- [[Execute typed update_ticket MCP tool by delegating to Phase 13-B TicketService.]] - `rationale_for` [EXTRACTED]
- [[InvalidTicketTransitionError]] - `uses` [INFERRED]
- [[TicketComment]] - `calls` [EXTRACTED]
- [[TicketLifecycleStatus]] - `calls` [EXTRACTED]
- [[TicketNotFoundError]] - `uses` [INFERRED]
- [[UpdateTicketToolInput]] - `uses` [INFERRED]
- [[UpdateTicketToolOutput]] - `calls` [EXTRACTED]
- [[_async_call()_3]] - `calls` [EXTRACTED]
- [[create_update_ticket_tool()]] - `calls` [EXTRACTED]
- [[get_audit_service()]] - `calls` [EXTRACTED]
- [[get_authorization_service()]] - `calls` [EXTRACTED]
- [[get_current_subject()]] - `calls` [EXTRACTED]
- [[get_current_tracer()]] - `calls` [EXTRACTED]
- [[get_request_id()]] - `calls` [EXTRACTED]
- [[get_ticket_service()]] - `calls` [EXTRACTED]
- [[it_supporttools.py]] - `imports` [EXTRACTED]
- [[mask_sensitive()]] - `calls` [EXTRACTED]
- [[mcp_servertools.py]] - `contains` [EXTRACTED]
- [[server.py]] - `imports` [EXTRACTED]
- [[test_cross_user_ticket_isolation_regression()]] - `calls` [INFERRED]
- [[test_update_ticket_lifecycle_comment_and_team()]] - `calls` [INFERRED]
- [[update_ticket()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/mcp_server/toolspy