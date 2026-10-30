---
type: community
cohesion: 0.10
members: 34
---

# approval.py

**Cohesion:** 0.10 - loosely connected
**Members:** 34 nodes

## Members
- [[dot-__init__()_17]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-__init__()_18]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-_collection()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-approve()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-create()_8]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-execute_approved_action()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-get()_8]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-get_request()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-list_pending()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-list_pending()_1]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-reject()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-update()]] - code - src/mcp_rag_agent/security/approval.py
- [[An AI-proposed high-risk action with no prior human approval is strictly…]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[ApprovalNotFoundError]] - code - src/mcp_rag_agent/security/approval.py
- [[ApprovalRequest]] - code - src/mcp_rag_agent/security/approval.py
- [[ApprovalService]] - code - src/mcp_rag_agent/security/approval.py
- [[ApprovalStore]] - code - src/mcp_rag_agent/security/approval.py
- [[Approve a pending request by an authorized human administrator. Enforces -…]] - rationale - src/mcp_rag_agent/security/approval.py
- [[BaseModel_10]] - code
- [[Domain service managing human-in-the-loop approval workflows.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Human-in-the-Loop (HITL) approval models, risk policies, store, and approval…]] - rationale - src/mcp_rag_agent/security/approval.py
- [[InvalidApprovalStateError]] - code - src/mcp_rag_agent/security/approval.py
- [[KeyError_1]] - code
- [[List all pending approval requests.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[MongoDB persistence adapter for Human Approval requests.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Pydantic model representing an enterprise Human Approval request.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Reject a pending request.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Retrieve an existing approval request.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[ValueError_1]] - code
- [[Verify approved status and transition to EXECUTED upon operation execution.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[_utc_now()_3]] - code - src/mcp_rag_agent/security/approval.py
- [[approval.py]] - code - src/mcp_rag_agent/security/approval.py
- [[datetime_3]] - code
- [[test_unapproved_high_risk_action_blocked()]] - code - tests/unit_tests/security/test_security_regression.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/approvalpy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_SecuritySubject]]
- 8 edges to [[_COMMUNITY_RiskLevel]]
- 7 edges to [[_COMMUNITY_test_approval.py]]
- 4 edges to [[_COMMUNITY_mcp_servertools.py]]
- 3 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[approval.py]] - degree 23, connects to 8 communities
- [[ApprovalService]] - degree 18, connects to 5 communities
- [[test_unapproved_high_risk_action_blocked()]] - degree 9, connects to 5 communities
- [[ApprovalStore]] - degree 15, connects to 4 communities
- [[ApprovalRequest]] - degree 15, connects to 3 communities