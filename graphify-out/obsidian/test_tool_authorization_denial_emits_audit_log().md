---
source_file: "tests/unit_tests/security/test_audit.py"
type: "code"
community: "test_tool_authorization_success_emits_audit_log"
location: "L109"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_tool_authorization_success_emits_audit_log
---

# test_tool_authorization_denial_emits_audit_log()

## Connections
- [[GetUserContextInput]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[Verify tool authorization rejection creates a DENIED audit record.]] - `rationale_for` [EXTRACTED]
- [[asyncio_15]] - `references` [EXTRACTED]
- [[get_user_context_typed()]] - `calls` [INFERRED]
- [[reset_it_services()]] - `calls` [INFERRED]
- [[set_audit_service()]] - `calls` [INFERRED]
- [[test_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_tool_authorization_success_emits_audit_log