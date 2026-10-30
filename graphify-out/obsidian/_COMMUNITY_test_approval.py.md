---
type: community
cohesion: 0.11
members: 24
---

# test_approval.py

**Cohesion:** 0.11 - loosely connected
**Members:** 24 nodes

## Members
- [[ApprovalStatus]] - code - src/mcp_rag_agent/security/approval.py
- [[Enum_6]] - code
- [[Expired requests cannot be approved or executed.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Separation of duties An AI agent or requester cannot approve their own high-…]] - rationale - tests/unit_tests/security/test_approval.py
- [[Test admin rejection of approval request.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Test authorized human admin approval.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Test creating a pending approval request.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Test full workflow Request - Approve - Execute.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Test listing pending requests with and without user_id filter.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Unit tests for Human-in-the-Loop (HITL) approval workflows, risk…]] - rationale - tests/unit_tests/security/test_approval.py
- [[admin_subject()]] - code - tests/unit_tests/security/test_approval.py
- [[approval_service()]] - code - tests/unit_tests/security/test_approval.py
- [[fixture_6]] - code
- [[it_support_subject()_1]] - code - tests/unit_tests/security/test_approval.py
- [[requester_subject()]] - code - tests/unit_tests/security/test_approval.py
- [[str_6]] - code
- [[test_approval.py]] - code - tests/unit_tests/security/test_approval.py
- [[test_approval_by_authorized_admin()]] - code - tests/unit_tests/security/test_approval.py
- [[test_execute_approved_action_workflow()]] - code - tests/unit_tests/security/test_approval.py
- [[test_expired_approval_cannot_be_approved_or_executed()]] - code - tests/unit_tests/security/test_approval.py
- [[test_list_pending_requests()]] - code - tests/unit_tests/security/test_approval.py
- [[test_reject_approval_request()]] - code - tests/unit_tests/security/test_approval.py
- [[test_request_approval_creation()]] - code - tests/unit_tests/security/test_approval.py
- [[test_separation_of_duties_requester_cannot_approve_own_action()]] - code - tests/unit_tests/security/test_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_approvalpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_approval.py]]
- 5 edges to [[_COMMUNITY_SecuritySubject]]
- 5 edges to [[_COMMUNITY_pytest]]
- 4 edges to [[_COMMUNITY_Role]]
- 3 edges to [[_COMMUNITY_RiskLevel]]
- 2 edges to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_datetime]]

## Top bridge nodes
- [[test_approval.py]] - degree 19, connects to 4 communities
- [[test_separation_of_duties_requester_cannot_approve_own_action()]] - degree 5, connects to 3 communities
- [[ApprovalStatus]] - degree 9, connects to 2 communities
- [[test_expired_approval_cannot_be_approved_or_executed()]] - degree 6, connects to 2 communities
- [[test_execute_approved_action_workflow()]] - degree 5, connects to 2 communities