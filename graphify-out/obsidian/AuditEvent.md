---
source_file: "src/mcp_rag_agent/security/audit.py"
type: "code"
community: "audit.py"
location: "L49"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/auditpy
---

# AuditEvent

## Connections
- [[dot-__init__()_31]] - `references` [EXTRACTED]
- [[dot-get_audit_logs()]] - `references` [EXTRACTED]
- [[dot-insert()]] - `references` [EXTRACTED]
- [[dot-log_event()]] - `calls` [EXTRACTED]
- [[dot-query()]] - `references` [EXTRACTED]
- [[dot-query_events()]] - `references` [EXTRACTED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[BaseModel_14]] - `inherits` [EXTRACTED]
- [[Pydantic model representing an immutable security audit event.]] - `rationale_for` [EXTRACTED]
- [[RiskLevel]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[_get_default_seed_audits()]] - `calls` [EXTRACTED]
- [[admin.py]] - `imports` [EXTRACTED]
- [[admin_service.py]] - `imports` [EXTRACTED]
- [[audit.py]] - `contains` [EXTRACTED]
- [[get_admin_audit_logs()]] - `uses` [INFERRED]
- [[mcp_rag_agentsecurity__init__.py]] - `imports` [EXTRACTED]
- [[test_audit_event_model()]] - `uses` [INFERRED]
- [[test_setup()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/auditpy