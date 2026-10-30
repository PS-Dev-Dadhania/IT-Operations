---
source_file: "src/mcp_rag_agent/mcp_server/tools.py"
type: "code"
community: "mcp_server/tools.py"
location: "L696"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/mcp_server/toolspy
---

# get_device_info_typed()

## Connections
- [[Any_3]] - `references` [EXTRACTED]
- [[DeviceNotFoundError]] - `uses` [INFERRED]
- [[Execute typed get_device_info MCP tool with privacy masking, authorization, and…]] - `rationale_for` [EXTRACTED]
- [[GetDeviceInfoInput]] - `uses` [INFERRED]
- [[GetDeviceInfoOutput]] - `calls` [EXTRACTED]
- [[_async_call()]] - `calls` [EXTRACTED]
- [[create_device_info_tool()]] - `calls` [EXTRACTED]
- [[get_audit_service()]] - `calls` [EXTRACTED]
- [[get_authorization_service()]] - `calls` [EXTRACTED]
- [[get_current_subject()]] - `calls` [EXTRACTED]
- [[get_current_tracer()]] - `calls` [EXTRACTED]
- [[get_device_info()]] - `calls` [EXTRACTED]
- [[get_device_service()]] - `calls` [EXTRACTED]
- [[get_request_id()]] - `calls` [EXTRACTED]
- [[it_supporttools.py]] - `imports` [EXTRACTED]
- [[mask_sensitive()]] - `calls` [EXTRACTED]
- [[mcp_servertools.py]] - `contains` [EXTRACTED]
- [[server.py]] - `imports` [EXTRACTED]
- [[test_cross_user_device_access_blocked()]] - `calls` [INFERRED]
- [[test_get_device_info_by_device_id_and_user_id()]] - `calls` [INFERRED]
- [[test_get_device_info_missing_args()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/mcp_server/toolspy