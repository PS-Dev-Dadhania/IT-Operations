---
source_file: "src/mcp_rag_agent/security/rbac.py"
type: "code"
community: "SecuritySubject"
location: "L53"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SecuritySubject
---

# SecuritySubject

## Connections
- [[dot-approve()]] - `references` [EXTRACTED]
- [[dot-can()]] - `references` [EXTRACTED]
- [[dot-can_access_device()]] - `references` [EXTRACTED]
- [[dot-can_access_ticket()]] - `references` [EXTRACTED]
- [[dot-can_access_user()]] - `references` [EXTRACTED]
- [[dot-can_execute_tool()]] - `references` [EXTRACTED]
- [[dot-execute_approved_action()]] - `references` [EXTRACTED]
- [[dot-filter_documents_for_subject()]] - `references` [EXTRACTED]
- [[dot-reject()]] - `references` [EXTRACTED]
- [[ApprovalService]] - `uses` [INFERRED]
- [[AuthorizationService]] - `uses` [INFERRED]
- [[BaseModel_25]] - `inherits` [EXTRACTED]
- [[Represents an authenticated callersubject in the system.]] - `rationale_for` [EXTRACTED]
- [[admin.py]] - `imports` [EXTRACTED]
- [[admin_subject()]] - `uses` [INFERRED]
- [[approval.py]] - `imports` [EXTRACTED]
- [[authorization.py]] - `imports` [EXTRACTED]
- [[dependencies.py]] - `imports` [EXTRACTED]
- [[employee_subject()]] - `uses` [INFERRED]
- [[get_admin_audit_logs()]] - `uses` [INFERRED]
- [[get_admin_evaluation()]] - `uses` [INFERRED]
- [[get_admin_metrics()]] - `uses` [INFERRED]
- [[get_admin_ticket()]] - `uses` [INFERRED]
- [[get_current_security_subject()]] - `calls` [EXTRACTED]
- [[get_current_subject()]] - `references` [EXTRACTED]
- [[it_admin_subject()]] - `uses` [INFERRED]
- [[it_support_subject()_1]] - `uses` [INFERRED]
- [[it_support_subject()]] - `uses` [INFERRED]
- [[list_admin_incidents()]] - `uses` [INFERRED]
- [[list_admin_tickets()]] - `uses` [INFERRED]
- [[mcp_rag_agentsecurity__init__.py]] - `imports` [EXTRACTED]
- [[other_employee_subject()]] - `uses` [INFERRED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[requester_subject()]] - `uses` [INFERRED]
- [[require_admin_role()]] - `uses` [INFERRED]
- [[require_audit_permission()]] - `uses` [INFERRED]
- [[security_analyst_subject()]] - `uses` [INFERRED]
- [[set_current_subject()]] - `references` [EXTRACTED]
- [[test_cross_user_device_access_blocked()]] - `uses` [INFERRED]
- [[test_cross_user_ticket_isolation_regression()]] - `uses` [INFERRED]
- [[test_employee_attempting_admin_operations_denied()]] - `uses` [INFERRED]
- [[test_retrieval_confidential_security_docs_filtered_for_employee()]] - `uses` [INFERRED]
- [[test_security_subject_validation()]] - `uses` [INFERRED]
- [[test_separation_of_duties_requester_cannot_approve_own_action()]] - `uses` [INFERRED]
- [[test_subject_contextvars_tracking()]] - `uses` [INFERRED]
- [[test_tool_authorization_denial_emits_audit_log()]] - `uses` [INFERRED]
- [[test_tool_authorization_success_emits_audit_log()]] - `uses` [INFERRED]
- [[test_unapproved_high_risk_action_blocked()]] - `uses` [INFERRED]
- [[with_security_subject()]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SecuritySubject