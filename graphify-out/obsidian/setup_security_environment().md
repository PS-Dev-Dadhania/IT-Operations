---
source_file: "tests/unit_tests/security/test_security_regression.py"
type: "code"
community: "test_tool_authorization_success_emits_audit_log"
location: "L113"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_tool_authorization_success_emits_audit_log
---

# setup_security_environment()

## Connections
- [[ApprovalService]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[AuditService]] - `uses` [INFERRED]
- [[AuditStore]] - `uses` [INFERRED]
- [[Ensure clean services and memory stores for regression testing.]] - `rationale_for` [EXTRACTED]
- [[fixture_10]] - `references` [EXTRACTED]
- [[reset_it_services()]] - `calls` [INFERRED]
- [[set_approval_service()]] - `calls` [INFERRED]
- [[set_audit_service()]] - `calls` [INFERRED]
- [[test_security_regression.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_tool_authorization_success_emits_audit_log