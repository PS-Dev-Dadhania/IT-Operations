# test_approval.py

> 24 nodes · cohesion 0.11

## Key Concepts

- **test_approval.py** (19 connections) — `tests/unit_tests/security/test_approval.py`
- **ApprovalStatus** (9 connections) — `src/mcp_rag_agent/security/approval.py`
- **test_expired_approval_cannot_be_approved_or_executed()** (6 connections) — `tests/unit_tests/security/test_approval.py`
- **test_execute_approved_action_workflow()** (5 connections) — `tests/unit_tests/security/test_approval.py`
- **test_separation_of_duties_requester_cannot_approve_own_action()** (5 connections) — `tests/unit_tests/security/test_approval.py`
- **admin_subject()** (4 connections) — `tests/unit_tests/security/test_approval.py`
- **approval_service()** (4 connections) — `tests/unit_tests/security/test_approval.py`
- **it_support_subject()** (4 connections) — `tests/unit_tests/security/test_approval.py`
- **fixture** (4 connections)
- **requester_subject()** (4 connections) — `tests/unit_tests/security/test_approval.py`
- **test_request_approval_creation()** (4 connections) — `tests/unit_tests/security/test_approval.py`
- **test_approval_by_authorized_admin()** (3 connections) — `tests/unit_tests/security/test_approval.py`
- **test_reject_approval_request()** (3 connections) — `tests/unit_tests/security/test_approval.py`
- **Enum** (2 connections)
- **test_list_pending_requests()** (2 connections) — `tests/unit_tests/security/test_approval.py`
- **str** (1 connections)
- **Unit tests for Human-in-the-Loop (HITL) approval workflows, risk…** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Test authorized human admin approval.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Separation of duties: An AI agent or requester cannot approve their own high-…** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Test admin rejection of approval request.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Test full workflow: Request -> Approve -> Execute.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Expired requests cannot be approved or executed.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Test listing pending requests with and without user_id filter.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Test creating a pending approval request.** (1 connections) — `tests/unit_tests/security/test_approval.py`

## Relationships

- [approval.py](approval.py.md) (7 shared connections)
- [SecuritySubject](SecuritySubject.md) (5 shared connections)
- [pytest](pytest.md) (5 shared connections)
- [Role](Role.md) (4 shared connections)
- [RiskLevel](RiskLevel.md) (3 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (2 shared connections)
- [datetime](datetime.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/security/approval.py`
- `tests/unit_tests/security/test_approval.py`

## Audit Trail

- EXTRACTED: 38 (67%)
- INFERRED: 19 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*