---
source_file: "src/mcp_rag_agent/api/routes/admin.py"
type: "code"
community: "AdminAPIService"
location: "L90"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AdminAPIService
---

# list_admin_incidents()

## Connections
- [[dot-list_incidents()]] - `calls` [INFERRED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[IncidentRecord]] - `uses` [INFERRED]
- [[Retrieve active and historical incidents. Requires IT_ADMIN or SYSTEM_ADMIN…]] - `rationale_for` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[admin.py]] - `contains` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[require_admin_role()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AdminAPIService