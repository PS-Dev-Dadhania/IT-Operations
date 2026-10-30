---
type: community
cohesion: 0.10
members: 21
---

# pydantic

**Cohesion:** 0.10 - loosely connected
**Members:** 21 nodes

## Members
- [[Test SecuritySubject Pydantic validation.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Test helper function has_permission.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Unit tests for Role-Based Access Control (RBAC) definitions and permission…]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify IT Admin permissions.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify Security Analyst permissions.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify System Admin has full elevated operational permissions.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify all 5 enterprise roles are defined as strongly typed enums.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify modifying returned permissions does not alter the master matrix.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify risk classification tiers.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[Verify standard granular permissions are defined.]] - rationale - tests/unit_tests/security/test_rbac.py
- [[pydantic]] - concept
- [[test_get_role_permissions_is_copy()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_has_permission_helper()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_it_admin_role_permissions()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_permission_enum_values()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_rbac.py]] - code - tests/unit_tests/security/test_rbac.py
- [[test_risk_level_enum()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_role_enum_values()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_security_analyst_role_permissions()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_security_subject_validation()]] - code - tests/unit_tests/security/test_rbac.py
- [[test_system_admin_role_permissions()]] - code - tests/unit_tests/security/test_rbac.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/pydantic
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_SecuritySubject]]
- 7 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_pytest]]
- 2 edges to [[_COMMUNITY_runbooks__init__.py]]
- 2 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_RiskLevel]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]
- 1 edge to [[_COMMUNITY_eval_runner.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_ConversationService]]
- 1 edge to [[_COMMUNITY_ObservabilityTracer]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_IncidentRecord]]
- 1 edge to [[_COMMUNITY_approval.py]]
- 1 edge to [[_COMMUNITY_ServiceStatusRecord]]
- 1 edge to [[_COMMUNITY_DeviceRecord]]
- 1 edge to [[_COMMUNITY_ingestion__init__.py]]
- 1 edge to [[_COMMUNITY_retrievalpipeline.py]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_ChatService]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_datetime]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_operational.py]]
- 1 edge to [[_COMMUNITY_test_it_evaluation.py]]
- 1 edge to [[_COMMUNITY_usersstore.py]]
- 1 edge to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_compute_it_metrics]]

## Top bridge nodes
- [[pydantic]] - degree 29, connects to 25 communities
- [[test_rbac.py]] - degree 16, connects to 3 communities
- [[test_security_subject_validation()]] - degree 5, connects to 3 communities
- [[test_get_role_permissions_is_copy()]] - degree 5, connects to 2 communities
- [[test_has_permission_helper()]] - degree 5, connects to 2 communities