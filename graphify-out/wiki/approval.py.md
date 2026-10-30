# approval.py

> 34 nodes · cohesion 0.10

## Key Concepts

- **approval.py** (23 connections) — `src/mcp_rag_agent/security/approval.py`
- **ApprovalService** (18 connections) — `src/mcp_rag_agent/security/approval.py`
- **ApprovalRequest** (15 connections) — `src/mcp_rag_agent/security/approval.py`
- **ApprovalStore** (15 connections) — `src/mcp_rag_agent/security/approval.py`
- **InvalidApprovalStateError** (9 connections) — `src/mcp_rag_agent/security/approval.py`
- **test_unapproved_high_risk_action_blocked()** (9 connections) — `tests/unit_tests/security/test_security_regression.py`
- **.approve()** (7 connections) — `src/mcp_rag_agent/security/approval.py`
- **.reject()** (7 connections) — `src/mcp_rag_agent/security/approval.py`
- **._collection()** (6 connections) — `src/mcp_rag_agent/security/approval.py`
- **ApprovalNotFoundError** (5 connections) — `src/mcp_rag_agent/security/approval.py`
- **.execute_approved_action()** (5 connections) — `src/mcp_rag_agent/security/approval.py`
- **_utc_now()** (5 connections) — `src/mcp_rag_agent/security/approval.py`
- **.get()** (4 connections) — `src/mcp_rag_agent/security/approval.py`
- **.update()** (4 connections) — `src/mcp_rag_agent/security/approval.py`
- **.get_request()** (3 connections) — `src/mcp_rag_agent/security/approval.py`
- **.list_pending()** (3 connections) — `src/mcp_rag_agent/security/approval.py`
- **.create()** (3 connections) — `src/mcp_rag_agent/security/approval.py`
- **.list_pending()** (3 connections) — `src/mcp_rag_agent/security/approval.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/security/approval.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/security/approval.py`
- **datetime** (2 connections)
- **BaseModel** (1 connections)
- **KeyError** (1 connections)
- **ValueError** (1 connections)
- **Human-in-the-Loop (HITL) approval models, risk policies, store, and approval…** (1 connections) — `src/mcp_rag_agent/security/approval.py`
- *... and 9 more nodes in this community*

## Relationships

- [SecuritySubject](SecuritySubject.md) (18 shared connections)
- [RiskLevel](RiskLevel.md) (8 shared connections)
- [test_approval.py](test_approval.py.md) (7 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (4 shared connections)
- [typing](typing.md) (3 shared connections)
- [Role](Role.md) (2 shared connections)
- [test_tool_authorization_success_emits_audit_log](test_tool_authorization_success_emits_audit_log.md) (2 shared connections)
- [audit.py](audit.py.md) (1 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (1 shared connections)
- [pydantic](pydantic.md) (1 shared connections)
- [pytest](pytest.md) (1 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/security/approval.py`
- `tests/unit_tests/security/test_security_regression.py`

## Audit Trail

- EXTRACTED: 89 (84%)
- INFERRED: 17 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*