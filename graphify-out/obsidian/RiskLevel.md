---
source_file: "src/mcp_rag_agent/security/rbac.py"
type: "code"
community: "RiskLevel"
location: "L44"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RiskLevel
---

# RiskLevel

## Connections
- [[dot-classify_risk()]] - `references` [EXTRACTED]
- [[dot-is_approval_required()]] - `references` [EXTRACTED]
- [[dot-log_event()]] - `references` [EXTRACTED]
- [[dot-request_approval()]] - `references` [EXTRACTED]
- [[Action risk classifications.]] - `rationale_for` [EXTRACTED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[ApprovalService]] - `uses` [INFERRED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[AuditService]] - `uses` [INFERRED]
- [[Enum_7]] - `inherits` [EXTRACTED]
- [[RiskPolicy]] - `uses` [INFERRED]
- [[_get_default_seed_audits()]] - `uses` [INFERRED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[audit.py]] - `imports` [EXTRACTED]
- [[mcp_rag_agentsecurity__init__.py]] - `imports` [EXTRACTED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[str_7]] - `inherits` [EXTRACTED]
- [[test_audit_event_model()]] - `uses` [INFERRED]
- [[test_audit_log_event_and_query()]] - `uses` [INFERRED]
- [[test_is_approval_required_gate()]] - `uses` [INFERRED]
- [[test_request_approval_creation()]] - `uses` [INFERRED]
- [[test_risk_classification_tiers()]] - `uses` [INFERRED]
- [[test_risk_level_enum()]] - `uses` [INFERRED]
- [[test_setup()]] - `uses` [INFERRED]
- [[test_unapproved_high_risk_action_blocked()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/RiskLevel