---
source_file: "tests/unit_tests/security/test_security_regression.py"
type: "code"
community: "approval.py"
location: "L199"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/approvalpy
---

# test_unapproved_high_risk_action_blocked()

## Connections
- [[An AI-proposed high-risk action with no prior human approval is strictly…]] - `rationale_for` [EXTRACTED]
- [[ApprovalService]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[InvalidApprovalStateError]] - `uses` [INFERRED]
- [[RiskLevel]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[pytest]] - `calls` [EXTRACTED]
- [[test_security_regression.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/approvalpy