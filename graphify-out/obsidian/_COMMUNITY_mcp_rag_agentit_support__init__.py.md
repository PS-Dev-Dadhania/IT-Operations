---
type: community
cohesion: 0.14
members: 29
---

# mcp_rag_agent/it_support/__init__.py

**Cohesion:** 0.14 - loosely connected
**Members:** 29 nodes

## Members
- [[An employee-reported problem; it is not a persisted ticket.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[BaseModel_13]] - code
- [[Device]] - code - src/mcp_rag_agent/it_support/models.py
- [[Enum_5]] - code
- [[Foundational incident shape; this phase deliberately has no incident store.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[Foundational ticket shape. Persistence and lifecycle logic are future work.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[ITIssue]] - code - src/mcp_rag_agent/it_support/models.py
- [[Incident]] - code - src/mcp_rag_agent/it_support/models.py
- [[Offline checks for Phase 13-A IT support contracts.]] - rationale - tests/unit_tests/it_support/test_models.py
- [[Priority]] - code - src/mcp_rag_agent/it_support/models.py
- [[SupportUser]] - code - src/mcp_rag_agent/it_support/models.py
- [[Ticket]] - code - src/mcp_rag_agent/it_support/models.py
- [[TicketStatus]] - code - src/mcp_rag_agent/it_support/models.py
- [[Typed, persistence-free contracts for the IT support domain.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[_utc_now()_6]] - code - src/mcp_rag_agent/it_support/models.py
- [[datetime_6]] - code
- [[it_supportmodels.py]] - code - src/mcp_rag_agent/it_support/models.py
- [[mcp_rag_agentit_support__init__.py]] - code - src/mcp_rag_agent/it_support/__init__.py
- [[parametrize_1]] - code
- [[str_4]] - code
- [[test_ids_and_timestamps_are_created_with_correct_types()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_incident_has_typed_status_and_severity()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_incident_rejects_invalid_enum_and_negative_affected_users()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_issue_accepts_typed_optional_context()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_issue_rejects_invalid_values()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_models.py]] - code - tests/unit_tests/it_support/test_models.py
- [[test_optional_user_and_device_fields_default_cleanly()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_required_fields_are_enforced()]] - code - tests/unit_tests/it_support/test_models.py
- [[test_ticket_has_foundational_fields_and_typed_status()]] - code - tests/unit_tests/it_support/test_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mcp_rag_agent/it_support/__init__py
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_IncidentRecord]]
- 11 edges to [[_COMMUNITY_ticketsmodels.py]]
- 9 edges to [[_COMMUNITY_mcp_servertools.py]]
- 8 edges to [[_COMMUNITY_ITCategory]]
- 8 edges to [[_COMMUNITY_intent.py]]
- 5 edges to [[_COMMUNITY_ServiceStatusRecord]]
- 5 edges to [[_COMMUNITY_DeviceRecord]]
- 4 edges to [[_COMMUNITY_pytest]]
- 4 edges to [[_COMMUNITY_runbooks__init__.py]]
- 3 edges to [[_COMMUNITY_Runbook]]
- 3 edges to [[_COMMUNITY_TicketService]]
- 3 edges to [[_COMMUNITY_usersstore.py]]
- 2 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 2 edges to [[_COMMUNITY_RunbookExecutor]]
- 2 edges to [[_COMMUNITY_UserContextRecord]]
- 2 edges to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_TicketRecord]]
- 1 edge to [[_COMMUNITY_test_incidents.py]]
- 1 edge to [[_COMMUNITY_MemoryIncidentStore]]
- 1 edge to [[_COMMUNITY_UserNotFoundError]]
- 1 edge to [[_COMMUNITY_IncidentStore]]
- 1 edge to [[_COMMUNITY_TicketStore]]
- 1 edge to [[_COMMUNITY_UserService]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]

## Top bridge nodes
- [[mcp_rag_agentit_support__init__.py]] - degree 58, connects to 19 communities
- [[it_supportmodels.py]] - degree 31, connects to 10 communities
- [[Priority]] - degree 21, connects to 6 communities
- [[test_models.py]] - degree 12, connects to 3 communities
- [[Enum_5]] - degree 5, connects to 2 communities