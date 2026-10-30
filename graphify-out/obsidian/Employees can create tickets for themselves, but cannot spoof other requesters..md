---
source_file: "tests/unit_tests/security/test_authorization.py"
type: "rationale"
community: "Role"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Role
---

# Employees can create tickets for themselves, but cannot spoof other requesters.

## Connections
- [[test_can_execute_tool_create_ticket()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Role