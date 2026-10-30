---
type: community
cohesion: 0.13
members: 21
---

# RiskLevel

**Cohesion:** 0.13 - loosely connected
**Members:** 21 nodes

## Members
- [[dot-classify_risk()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-is_approval_required()]] - code - src/mcp_rag_agent/security/approval.py
- [[dot-request_approval()]] - code - src/mcp_rag_agent/security/approval.py
- [[Action risk classifications.]] - rationale - src/mcp_rag_agent/security/rbac.py
- [[Any_23]] - code
- [[Classify operational action into risk tiers.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Create a new human approval request for a high-risk operation.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Determine if an action strictly requires human approval before execution.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Deterministic enterprise risk classification and approval gate policy.]] - rationale - src/mcp_rag_agent/security/approval.py
- [[Enum_7]] - code
- [[RiskLevel]] - code - src/mcp_rag_agent/security/rbac.py
- [[RiskPolicy]] - code - src/mcp_rag_agent/security/approval.py
- [[Test creating and querying audit events.]] - rationale - tests/unit_tests/security/test_audit.py
- [[Verify AuditEvent structure and default properties.]] - rationale - tests/unit_tests/security/test_audit.py
- [[Verify approval gate decision based on risk level.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Verify deterministic risk classification.]] - rationale - tests/unit_tests/security/test_approval.py
- [[str_7]] - code
- [[test_audit_event_model()]] - code - tests/unit_tests/security/test_audit.py
- [[test_audit_log_event_and_query()]] - code - tests/unit_tests/security/test_audit.py
- [[test_is_approval_required_gate()]] - code - tests/unit_tests/security/test_approval.py
- [[test_risk_classification_tiers()]] - code - tests/unit_tests/security/test_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RiskLevel
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_approval.py]]
- 7 edges to [[_COMMUNITY_Role]]
- 6 edges to [[_COMMUNITY_SecuritySubject]]
- 5 edges to [[_COMMUNITY_audit.py]]
- 3 edges to [[_COMMUNITY_test_approval.py]]
- 2 edges to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[RiskLevel]] - degree 25, connects to 7 communities
- [[RiskPolicy]] - degree 9, connects to 3 communities
- [[test_audit_event_model()]] - degree 5, connects to 3 communities
- [[test_is_approval_required_gate()]] - degree 6, connects to 2 communities
- [[Enum_7]] - degree 4, connects to 2 communities