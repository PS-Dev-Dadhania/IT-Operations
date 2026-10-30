---
source_file: "tests/unit_tests/security/test_audit.py"
type: "code"
community: "test_tool_authorization_success_emits_audit_log"
location: "L134"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_tool_authorization_success_emits_audit_log
---

# test_tool_authorization_success_emits_audit_log()

## Connections
- [[GetUserContextInput]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[UserContextRecord]] - `uses` [INFERRED]
- [[UserService]] - `uses` [INFERRED]
- [[Verify authorized tool execution creates an AUTHORIZED audit record.]] - `rationale_for` [EXTRACTED]
- [[__init__()]] - `contains` [EXTRACTED]
- [[asyncio_15]] - `references` [EXTRACTED]
- [[create()]] - `contains` [EXTRACTED]
- [[get()]] - `contains` [EXTRACTED]
- [[get_user_context_typed()]] - `calls` [INFERRED]
- [[reset_it_services()]] - `calls` [INFERRED]
- [[set_audit_service()]] - `calls` [INFERRED]
- [[set_user_service()]] - `calls` [INFERRED]
- [[test_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_tool_authorization_success_emits_audit_log