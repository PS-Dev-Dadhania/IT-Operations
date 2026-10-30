---
type: community
cohesion: 0.28
members: 13
---

# pytest

**Cohesion:** 0.28 - loosely connected
**Members:** 13 nodes

## Members
- [[IT Support  Employee roles lack APPROVE_HIGH_RISK_ACTION permission.]] - rationale - tests/unit_tests/security/test_approval.py
- [[Ticket store and lifecycle tests with mocked MongoDB.]] - rationale - tests/unit_tests/it_support/test_tickets.py
- [[_request()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[pytest]] - concept
- [[test_create_and_duplicate_detection()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_escalation_is_allowed_only_from_open_or_in_progress()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_invalid_lifecycle_transition_is_rejected()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_lifecycle_allows_only_deterministic_transitions()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_mongodb_failure_is_not_silenced()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_ticket_store_crud_uses_shared_mongodb_client()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_ticket_store_queries_and_not_found_handling()]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_tickets.py]] - code - tests/unit_tests/it_support/test_tickets.py
- [[test_unauthorized_role_cannot_approve()]] - code - tests/unit_tests/security/test_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/pytest
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_TicketRecord]]
- 9 edges to [[_COMMUNITY_unittest_mock]]
- 7 edges to [[_COMMUNITY_TicketService]]
- 7 edges to [[_COMMUNITY_test_admin_api.py]]
- 5 edges to [[_COMMUNITY_test_approval.py]]
- 4 edges to [[_COMMUNITY_DeviceRecord]]
- 4 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 4 edges to [[_COMMUNITY_UserNotFoundError]]
- 3 edges to [[_COMMUNITY_ticketsmodels.py]]
- 3 edges to [[_COMMUNITY_TicketStore]]
- 2 edges to [[_COMMUNITY_ITCategory]]
- 2 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 2 edges to [[_COMMUNITY_pydantic]]
- 2 edges to [[_COMMUNITY_test_it_evaluation.py]]
- 2 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 2 edges to [[_COMMUNITY_test_mongodb_integration.py]]
- 1 edge to [[_COMMUNITY_approval.py]]
- 1 edge to [[_COMMUNITY_compute_it_metrics]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_Role]]
- 1 edge to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 1 edge to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 1 edge to [[_COMMUNITY_test_runbooks.py]]
- 1 edge to [[_COMMUNITY_AnswerGenerator]]
- 1 edge to [[_COMMUNITY_AdvancedRetriever]]
- 1 edge to [[_COMMUNITY_TestAPIIntegration]]
- 1 edge to [[_COMMUNITY_test_observability.py]]

## Top bridge nodes
- [[pytest]] - degree 55, connects to 24 communities
- [[test_tickets.py]] - degree 17, connects to 3 communities
- [[_request()]] - degree 11, connects to 3 communities
- [[test_invalid_lifecycle_transition_is_rejected()]] - degree 7, connects to 3 communities
- [[test_ticket_store_queries_and_not_found_handling()]] - degree 7, connects to 3 communities