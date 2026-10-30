---
type: community
cohesion: 0.12
members: 38
---

# tickets/models.py

**Cohesion:** 0.12 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-create()_6]] - code - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[dot-create_ticket()]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-get()_6]] - code - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[dot-patch()]] - code - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[dot-test_legacy_agent_attribute_issues_deprecation_warning()]] - code - tests/unit_tests/test_agent_creation.py
- [[API-facing ticket service that keeps routes free of persistence logic.]] - rationale - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[BaseModel_4]] - code
- [[IT ticket endpoints; lifecycle decisions are delegated to domain services.]] - rationale - src/mcp_rag_agent/api/routes/it_tickets.py
- [[ITTicketAPIService]] - code - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[InvalidTicketTransitionError]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[MongoDB persistence adapter for tickets with in-memory fallback support.]] - rationale - src/mcp_rag_agent/it_support/tickets/store.py
- [[Only fields permitted by the ticket API; status uses a validated transition.]] - rationale - src/mcp_rag_agent/it_support/tickets/models.py
- [[Persisted ticket contracts and deterministic lifecycle definitions.]] - rationale - src/mcp_rag_agent/it_support/tickets/models.py
- [[Public request and response schemas for IT ticket endpoints.]] - rationale - src/mcp_rag_agent/api/schemas/it_tickets.py
- [[Response]] - code
- [[Ticket persistence and lifecycle domain.]] - rationale - src/mcp_rag_agent/it_support/tickets/__init__.py
- [[Ticket use cases, including duplicate detection and lifecycle enforcement.]] - rationale - src/mcp_rag_agent/it_support/tickets/service.py
- [[TicketComment]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[TicketCreate]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[TicketOperationResult]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[TicketPatch]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[ValueError]] - code
- [[Verify accessing mcp_rag_agent.agent.agent issues a DeprecationWarning.]] - rationale - tests/unit_tests/test_agent_creation.py
- [[_ensure_enabled()]] - code - src/mcp_rag_agent/api/routes/it_tickets.py
- [[_utc_now()]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[create_ticket()_1]] - code - src/mcp_rag_agent/api/routes/it_tickets.py
- [[datetime]] - code
- [[get_ticket()]] - code - src/mcp_rag_agent/api/routes/it_tickets.py
- [[it_ticket_service.py]] - code - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[patch]] - code
- [[patch_ticket()]] - code - src/mcp_rag_agent/api/routes/it_tickets.py
- [[post]] - code
- [[routesit_tickets.py]] - code - src/mcp_rag_agent/api/routes/it_tickets.py
- [[schemasit_tickets.py]] - code - src/mcp_rag_agent/api/schemas/it_tickets.py
- [[tickets__init__.py]] - code - src/mcp_rag_agent/it_support/tickets/__init__.py
- [[ticketsmodels.py]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[ticketsservice.py]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[ticketsstore.py]] - code - src/mcp_rag_agent/it_support/tickets/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/tickets/modelspy
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_TicketRecord]]
- 17 edges to [[_COMMUNITY_TicketService]]
- 11 edges to [[_COMMUNITY_dependencies.py]]
- 11 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 10 edges to [[_COMMUNITY_Config]]
- 6 edges to [[_COMMUNITY_mcp_servertools.py]]
- 5 edges to [[_COMMUNITY_TicketStore]]
- 3 edges to [[_COMMUNITY_typing]]
- 3 edges to [[_COMMUNITY_ConversationService]]
- 3 edges to [[_COMMUNITY_pytest]]
- 3 edges to [[_COMMUNITY_ITCategory]]
- 3 edges to [[_COMMUNITY_datetime]]
- 2 edges to [[_COMMUNITY_get_checkpointer]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_Role]]
- 1 edge to [[_COMMUNITY_TestMongoDBClient]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_eval_runner.py]]
- 1 edge to [[_COMMUNITY_AdminAPIService]]
- 1 edge to [[_COMMUNITY_AnswerGenerator]]
- 1 edge to [[_COMMUNITY_ObservabilityTracer]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_audit.py]]

## Top bridge nodes
- [[ticketsstore.py]] - degree 19, connects to 9 communities
- [[dot-patch()]] - degree 17, connects to 8 communities
- [[ticketsmodels.py]] - degree 22, connects to 7 communities
- [[TicketCreate]] - degree 19, connects to 7 communities
- [[TicketComment]] - degree 14, connects to 6 communities