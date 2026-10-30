---
source_file: "src/mcp_rag_agent/api/routes/admin.py"
type: "code"
community: "get_admin_evaluation"
location: "L122"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/get_admin_evaluation
---

# get_admin_evaluation()

## Connections
- [[dot-get_evaluation_summary()]] - `calls` [INFERRED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[AdminEvaluationSummary]] - `uses` [INFERRED]
- [[Retrieve latest evaluation benchmark metrics. Requires IT_ADMIN or SYSTEM_ADMIN…]] - `rationale_for` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[admin.py]] - `contains` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[require_admin_role()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/get_admin_evaluation