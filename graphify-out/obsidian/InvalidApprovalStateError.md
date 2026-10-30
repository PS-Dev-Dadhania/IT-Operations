---
source_file: "src/mcp_rag_agent/security/approval.py"
type: "code"
community: "approval.py"
location: "L113"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/approvalpy
---

# InvalidApprovalStateError

## Connections
- [[dot-approve()]] - `calls` [EXTRACTED]
- [[dot-execute_approved_action()]] - `calls` [EXTRACTED]
- [[dot-reject()]] - `calls` [EXTRACTED]
- [[ValueError_1]] - `inherits` [EXTRACTED]
- [[approval.py]] - `contains` [EXTRACTED]
- [[mcp_rag_agentsecurity__init__.py]] - `imports` [EXTRACTED]
- [[test_execute_approved_action_workflow()]] - `uses` [INFERRED]
- [[test_expired_approval_cannot_be_approved_or_executed()]] - `uses` [INFERRED]
- [[test_unapproved_high_risk_action_blocked()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/approvalpy