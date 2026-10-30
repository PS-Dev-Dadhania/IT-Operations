# SecuritySubject

> God node · 49 connections · `src/mcp_rag_agent/security/rbac.py`

**Community:** [SecuritySubject](SecuritySubject.md)

## Connections by Relation

### calls
- get_current_security_subject() `EXTRACTED`

### contains
- rbac.py `EXTRACTED`

### imports
- [dependencies.py](dependencies.py.md) `EXTRACTED`
- admin.py `EXTRACTED`
- mcp_rag_agent/security/__init__.py `EXTRACTED`
- [approval.py](approval.py.md) `EXTRACTED`
- authorization.py `EXTRACTED`

### inherits
- BaseModel `EXTRACTED`

### rationale_for
- Represents an authenticated caller/subject in the system. `EXTRACTED`

### references
- get_current_subject() `EXTRACTED`
- .can() `EXTRACTED`
- .can_execute_tool() `EXTRACTED`
- .can_access_device() `EXTRACTED`
- .can_access_user() `EXTRACTED`
- .approve() `EXTRACTED`
- .reject() `EXTRACTED`
- .can_access_ticket() `EXTRACTED`
- set_current_subject() `EXTRACTED`
- with_security_subject() `EXTRACTED`
- .execute_approved_action() `EXTRACTED`
- .filter_documents_for_subject() `EXTRACTED`

### uses
- ApprovalService `INFERRED`
- AuthorizationService `INFERRED`
- test_tool_authorization_success_emits_audit_log() `INFERRED`
- require_admin_role() `INFERRED`
- test_cross_user_device_access_blocked() `INFERRED`
- test_cross_user_ticket_isolation_regression() `INFERRED`
- test_retrieval_confidential_security_docs_filtered_for_employee() `INFERRED`
- require_audit_permission() `INFERRED`
- test_tool_authorization_denial_emits_audit_log() `INFERRED`
- test_unapproved_high_risk_action_blocked() `INFERRED`
- get_admin_audit_logs() `INFERRED`
- get_admin_evaluation() `INFERRED`
- get_admin_metrics() `INFERRED`
- get_admin_ticket() `INFERRED`
- list_admin_incidents() `INFERRED`
- list_admin_tickets() `INFERRED`
- test_subject_contextvars_tracking() `INFERRED`
- test_employee_attempting_admin_operations_denied() `INFERRED`
- test_separation_of_duties_requester_cannot_approve_own_action() `INFERRED`
- test_security_subject_validation() `INFERRED`
- *…and 8 more `uses` connection(s) not listed (lowest-degree first to go)*

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*