---
type: community
cohesion: 0.14
members: 15
---

# TicketService

**Cohesion:** 0.14 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-__init__()_46]] - code - src/mcp_rag_agent/api/services/it_ticket_service.py
- [[dot-__init__()_47]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-__init__()_48]] - code - src/mcp_rag_agent/it_support/tickets/store.py
- [[dot-add_comment()_1]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-assign_team()]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-get_ticket()_1]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-list_tickets()_2]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-transition_status()]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[dot-update_fields()_7]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[Enum_9]] - code
- [[TicketLifecycleStatus]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[TicketService]] - code - src/mcp_rag_agent/it_support/tickets/service.py
- [[Update non-lifecycle fields after the API schema has restricted them.]] - rationale - src/mcp_rag_agent/it_support/tickets/service.py
- [[_get_default_seed_tickets()]] - code - src/mcp_rag_agent/it_support/tickets/store.py
- [[str_9]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TicketService
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_ticketsmodels.py]]
- 13 edges to [[_COMMUNITY_TicketRecord]]
- 7 edges to [[_COMMUNITY_pytest]]
- 5 edges to [[_COMMUNITY_dependencies.py]]
- 5 edges to [[_COMMUNITY_TicketStore]]
- 4 edges to [[_COMMUNITY_mcp_servertools.py]]
- 3 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 3 edges to [[_COMMUNITY_AdminAPIService]]
- 2 edges to [[_COMMUNITY_IncidentRecord]]
- 2 edges to [[_COMMUNITY_setup_services]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_ITCategory]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_Role]]

## Top bridge nodes
- [[TicketService]] - degree 38, connects to 12 communities
- [[TicketLifecycleStatus]] - degree 24, connects to 9 communities
- [[_get_default_seed_tickets()]] - degree 6, connects to 4 communities
- [[dot-transition_status()]] - degree 4, connects to 2 communities
- [[dot-add_comment()_1]] - degree 3, connects to 2 communities