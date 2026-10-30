---
source_file: "src/mcp_rag_agent/api/routes/admin.py"
type: "code"
community: "AdminAPIService"
location: "L31"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AdminAPIService
---

# list_admin_tickets()

## Connections
- [[dot-list_tickets()_1]] - `calls` [INFERRED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[Retrieve filtered tickets. Requires IT_ADMIN or SYSTEM_ADMIN role.]] - `rationale_for` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[TicketRecord]] - `uses` [INFERRED]
- [[admin.py]] - `contains` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[require_admin_role()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AdminAPIService