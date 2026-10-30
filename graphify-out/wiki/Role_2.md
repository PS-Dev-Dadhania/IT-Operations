# Role

> God node · 51 connections · `src/mcp_rag_agent/security/rbac.py`

**Community:** [Role](Role.md)

## Connections by Relation

### calls
- get_current_security_subject() `EXTRACTED`

### contains
- rbac.py `EXTRACTED`

### imports
- [mcp_server/tools.py](mcp_server-tools.py.md) `EXTRACTED`
- [dependencies.py](dependencies.py.md) `EXTRACTED`
- mcp_rag_agent/security/__init__.py `EXTRACTED`
- [approval.py](approval.py.md) `EXTRACTED`
- [audit.py](audit.py.md) `EXTRACTED`
- authorization.py `EXTRACTED`

### inherits
- Enum `EXTRACTED`
- str `EXTRACTED`

### rationale_for
- Authoritative enterprise roles for IT Support Copilot. `EXTRACTED`

### references
- has_permission() `EXTRACTED`
- get_role_permissions() `EXTRACTED`
- .log_event() `EXTRACTED`
- .is_approval_required() `EXTRACTED`

### uses
- test_setup() `INFERRED`
- AuditEvent `INFERRED`
- AuditService `INFERRED`
- AuthorizationService `INFERRED`
- test_tool_authorization_success_emits_audit_log() `INFERRED`
- require_admin_role() `INFERRED`
- test_cross_user_device_access_blocked() `INFERRED`
- test_cross_user_ticket_isolation_regression() `INFERRED`
- test_retrieval_confidential_security_docs_filtered_for_employee() `INFERRED`
- RiskPolicy `INFERRED`
- test_tool_authorization_denial_emits_audit_log() `INFERRED`
- test_unapproved_high_risk_action_blocked() `INFERRED`
- test_subject_contextvars_tracking() `INFERRED`
- _get_default_seed_audits() `INFERRED`
- test_is_approval_required_gate() `INFERRED`
- test_employee_attempting_admin_operations_denied() `INFERRED`
- test_separation_of_duties_requester_cannot_approve_own_action() `INFERRED`
- test_audit_event_model() `INFERRED`
- test_employee_role_permissions() `INFERRED`
- test_get_role_permissions_is_copy() `INFERRED`
- *…and 16 more `uses` connection(s) not listed (lowest-degree first to go)*

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*