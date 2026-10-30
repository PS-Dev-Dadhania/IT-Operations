---
source_file: "src/mcp_rag_agent/api/dependencies.py"
type: "code"
community: "dependencies.py"
location: "L152"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/dependenciespy
---

# require_admin_role()

## Connections
- [[RBAC dependency requiring IT_ADMIN or SYSTEM_ADMIN role.]] - `rationale_for` [EXTRACTED]
- [[Request_1]] - `references` [EXTRACTED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[admin.py]] - `imports` [EXTRACTED]
- [[dependencies.py]] - `contains` [EXTRACTED]
- [[get_admin_evaluation()]] - `calls` [EXTRACTED]
- [[get_admin_metrics()]] - `calls` [EXTRACTED]
- [[get_admin_ticket()]] - `calls` [EXTRACTED]
- [[get_current_security_subject()]] - `calls` [EXTRACTED]
- [[list_admin_incidents()]] - `calls` [EXTRACTED]
- [[list_admin_tickets()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/dependenciespy