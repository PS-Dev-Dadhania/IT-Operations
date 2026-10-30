---
source_file: "src/mcp_rag_agent/api/routes/admin.py"
type: "code"
community: "get_admin_evaluation"
location: "L108"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/get_admin_evaluation
---

# get_admin_metrics()

## Connections
- [[dot-get_metrics()]] - `calls` [INFERRED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[OperationalKPIs]] - `uses` [INFERRED]
- [[Retrieve operational KPIs. Requires IT_ADMIN or SYSTEM_ADMIN role.]] - `rationale_for` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[admin.py]] - `contains` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[require_admin_role()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/get_admin_evaluation