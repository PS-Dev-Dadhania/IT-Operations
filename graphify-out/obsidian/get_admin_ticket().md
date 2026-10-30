---
source_file: "src/mcp_rag_agent/api/routes/admin.py"
type: "code"
community: "AdminAPIService"
location: "L66"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AdminAPIService
---

# get_admin_ticket()

## Connections
- [[dot-get_ticket()]] - `calls` [INFERRED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[Retrieve ticket details. Requires IT_ADMIN or SYSTEM_ADMIN role.]] - `rationale_for` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[TicketRecord]] - `uses` [INFERRED]
- [[admin.py]] - `contains` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[require_admin_role()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AdminAPIService