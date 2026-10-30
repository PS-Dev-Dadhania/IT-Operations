---
source_file: "tests/unit_tests/security/test_security_regression.py"
type: "code"
community: "Role"
location: "L130"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Role
---

# test_cross_user_ticket_isolation_regression()

## Connections
- [[MemoryTicketStore_5]] - `calls` [EXTRACTED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[TicketCreate]] - `uses` [INFERRED]
- [[TicketService]] - `uses` [INFERRED]
- [[UpdateTicketToolInput]] - `uses` [INFERRED]
- [[User A (EMP-1001) attempting to accessupdate User B's (EMP-1002) ticket is…]] - `rationale_for` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]
- [[set_ticket_service()]] - `calls` [INFERRED]
- [[test_security_regression.py]] - `contains` [EXTRACTED]
- [[update_ticket_typed()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Role