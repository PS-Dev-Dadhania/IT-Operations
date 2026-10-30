# RiskLevel

> 21 nodes · cohesion 0.13

## Key Concepts

- **RiskLevel** (25 connections) — `src/mcp_rag_agent/security/rbac.py`
- **RiskPolicy** (9 connections) — `src/mcp_rag_agent/security/approval.py`
- **.request_approval()** (6 connections) — `src/mcp_rag_agent/security/approval.py`
- **.classify_risk()** (6 connections) — `src/mcp_rag_agent/security/approval.py`
- **test_is_approval_required_gate()** (6 connections) — `tests/unit_tests/security/test_approval.py`
- **.is_approval_required()** (5 connections) — `src/mcp_rag_agent/security/approval.py`
- **test_risk_classification_tiers()** (5 connections) — `tests/unit_tests/security/test_approval.py`
- **test_audit_event_model()** (5 connections) — `tests/unit_tests/security/test_audit.py`
- **Enum** (4 connections)
- **test_audit_log_event_and_query()** (4 connections) — `tests/unit_tests/security/test_audit.py`
- **Any** (3 connections)
- **str** (3 connections)
- **Determine if an action strictly requires human approval before execution.** (1 connections) — `src/mcp_rag_agent/security/approval.py`
- **Create a new human approval request for a high-risk operation.** (1 connections) — `src/mcp_rag_agent/security/approval.py`
- **Deterministic enterprise risk classification and approval gate policy.** (1 connections) — `src/mcp_rag_agent/security/approval.py`
- **Classify operational action into risk tiers.** (1 connections) — `src/mcp_rag_agent/security/approval.py`
- **Action risk classifications.** (1 connections) — `src/mcp_rag_agent/security/rbac.py`
- **Verify deterministic risk classification.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Verify approval gate decision based on risk level.** (1 connections) — `tests/unit_tests/security/test_approval.py`
- **Verify AuditEvent structure and default properties.** (1 connections) — `tests/unit_tests/security/test_audit.py`
- **Test creating and querying audit events.** (1 connections) — `tests/unit_tests/security/test_audit.py`

## Relationships

- [approval.py](approval.py.md) (8 shared connections)
- [Role](Role.md) (7 shared connections)
- [SecuritySubject](SecuritySubject.md) (6 shared connections)
- [audit.py](audit.py.md) (5 shared connections)
- [test_approval.py](test_approval.py.md) (3 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (2 shared connections)
- [dependencies.py](dependencies.py.md) (1 shared connections)
- [IncidentRecord](IncidentRecord.md) (1 shared connections)
- [pydantic](pydantic.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/security/approval.py`
- `src/mcp_rag_agent/security/rbac.py`
- `tests/unit_tests/security/test_approval.py`
- `tests/unit_tests/security/test_audit.py`

## Audit Trail

- EXTRACTED: 41 (66%)
- INFERRED: 21 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*