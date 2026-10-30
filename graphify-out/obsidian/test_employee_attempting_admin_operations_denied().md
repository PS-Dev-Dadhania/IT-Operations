---
source_file: "tests/unit_tests/security/test_security_regression.py"
type: "code"
community: "SecuritySubject"
location: "L168"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SecuritySubject
---

# test_employee_attempting_admin_operations_denied()

## Connections
- [[AuthorizationService]] - `uses` [INFERRED]
- [[Employee attempting admin-only operations is strictly DENIED.]] - `rationale_for` [EXTRACTED]
- [[Permission]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[test_security_regression.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SecuritySubject