---
source_file: "src/mcp_rag_agent/api/dependencies.py"
type: "code"
community: "dependencies.py"
location: "L170"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/dependenciespy
---

# require_audit_permission()

## Connections
- [[Permission]] - `uses` [INFERRED]
- [[RBAC dependency requiring VIEW_AUDIT_LOGS permission.]] - `rationale_for` [EXTRACTED]
- [[Request_1]] - `references` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[admin.py]] - `imports` [EXTRACTED]
- [[dependencies.py]] - `contains` [EXTRACTED]
- [[get_admin_audit_logs()]] - `calls` [EXTRACTED]
- [[get_current_security_subject()]] - `calls` [EXTRACTED]
- [[has_permission()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/dependenciespy