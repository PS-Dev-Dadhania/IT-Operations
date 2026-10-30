---
source_file: "src/mcp_rag_agent/security/rbac.py"
type: "code"
community: "Role"
location: "L11"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Role
---

# Role

## Connections
- [[dot-is_approval_required()]] - `references` [EXTRACTED]
- [[dot-log_event()]] - `references` [EXTRACTED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[AuditService]] - `uses` [INFERRED]
- [[Authoritative enterprise roles for IT Support Copilot.]] - `rationale_for` [EXTRACTED]
- [[AuthorizationService]] - `uses` [INFERRED]
- [[Enum_7]] - `inherits` [EXTRACTED]
- [[RiskPolicy]] - `uses` [INFERRED]
- [[_get_default_seed_audits()]] - `uses` [INFERRED]
- [[admin_subject()]] - `uses` [INFERRED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[audit.py]] - `imports` [EXTRACTED]
- [[authorization.py]] - `imports` [EXTRACTED]
- [[dependencies.py]] - `imports` [EXTRACTED]
- [[employee_subject()]] - `uses` [INFERRED]
- [[get_current_security_subject()]] - `calls` [EXTRACTED]
- [[get_role_permissions()]] - `references` [EXTRACTED]
- [[has_permission()]] - `references` [EXTRACTED]
- [[it_admin_subject()]] - `uses` [INFERRED]
- [[it_support_subject()_1]] - `uses` [INFERRED]
- [[it_support_subject()]] - `uses` [INFERRED]
- [[mcp_rag_agentsecurity__init__.py]] - `imports` [EXTRACTED]
- [[mcp_servertools.py]] - `imports` [EXTRACTED]
- [[other_employee_subject()]] - `uses` [INFERRED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[requester_subject()]] - `uses` [INFERRED]
- [[require_admin_role()]] - `uses` [INFERRED]
- [[security_analyst_subject()]] - `uses` [INFERRED]
- [[str_7]] - `inherits` [EXTRACTED]
- [[test_audit_event_model()]] - `uses` [INFERRED]
- [[test_audit_log_event_and_query()]] - `uses` [INFERRED]
- [[test_cross_user_device_access_blocked()]] - `uses` [INFERRED]
- [[test_cross_user_ticket_isolation_regression()]] - `uses` [INFERRED]
- [[test_employee_attempting_admin_operations_denied()]] - `uses` [INFERRED]
- [[test_employee_role_permissions()]] - `uses` [INFERRED]
- [[test_get_role_permissions_is_copy()]] - `uses` [INFERRED]
- [[test_has_permission_helper()]] - `uses` [INFERRED]
- [[test_is_approval_required_gate()]] - `uses` [INFERRED]
- [[test_it_admin_role_permissions()]] - `uses` [INFERRED]
- [[test_it_support_role_permissions()]] - `uses` [INFERRED]
- [[test_retrieval_confidential_security_docs_filtered_for_employee()]] - `uses` [INFERRED]
- [[test_role_enum_values()]] - `uses` [INFERRED]
- [[test_security_analyst_role_permissions()]] - `uses` [INFERRED]
- [[test_security_subject_validation()]] - `uses` [INFERRED]
- [[test_separation_of_duties_requester_cannot_approve_own_action()]] - `uses` [INFERRED]
- [[test_setup()]] - `uses` [INFERRED]
- [[test_subject_contextvars_tracking()]] - `uses` [INFERRED]
- [[test_system_admin_role_permissions()]] - `uses` [INFERRED]
- [[test_tool_authorization_denial_emits_audit_log()]] - `uses` [INFERRED]
- [[test_tool_authorization_success_emits_audit_log()]] - `uses` [INFERRED]
- [[test_unapproved_high_risk_action_blocked()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/Role