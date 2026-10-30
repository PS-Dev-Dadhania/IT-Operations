---
source_file: "src/mcp_rag_agent/api/routes/admin.py"
type: "code"
community: "AdminAPIService"
location: "L136"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AdminAPIService
---

# get_admin_audit_logs()

## Connections
- [[dot-get_audit_logs()]] - `calls` [INFERRED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[Retrieve sanitized security audit logs. Requires VIEW_AUDIT_LOGS permission.]] - `rationale_for` [EXTRACTED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[admin.py]] - `contains` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[require_audit_permission()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AdminAPIService