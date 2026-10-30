---
type: community
cohesion: 0.08
members: 46
---

# TicketRecord

**Cohesion:** 0.08 - loosely connected
**Members:** 46 nodes

## Members
- [[dot-__init__()_6]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-__init__()_7]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-__init__()_8]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-__init__()_9]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[dot-__init__()_10]] - code - tests/unit_tests/it_support/test_tickets.py
- [[dot-__init__()_11]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-add_comment()]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-create()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-create()_1]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-create()_2]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-create()_3]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[dot-create()_4]] - code - tests/unit_tests/it_support/test_tickets.py
- [[dot-create()_5]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-find_unresolved_duplicate()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-find_unresolved_duplicate()_1]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-find_unresolved_duplicate()_2]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-find_unresolved_duplicate()_3]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[dot-find_unresolved_duplicate()_4]] - code - tests/unit_tests/it_support/test_tickets.py
- [[dot-find_unresolved_duplicate()_5]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-get()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-get()_1]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-get()_2]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-get()_3]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[dot-get()_4]] - code - tests/unit_tests/it_support/test_tickets.py
- [[dot-get()_5]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-list()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-list()_1]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[dot-list()_2]] - code - tests/unit_tests/it_support/test_tickets.py
- [[dot-list()_3]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-list_tickets()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-update_fields()]] - code - tests/unit_tests/api/test_admin_api.py
- [[dot-update_fields()_1]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-update_fields()_2]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[dot-update_fields()_3]] - code - tests/unit_tests/it_support/test_tickets.py
- [[dot-update_fields()_4]] - code - tests/unit_tests/security/test_security_regression.py
- [[In-memory ticket store double for regression tests.]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[KeyError]] - code
- [[MemoryTicketStore]] - code - tests/unit_tests/api/test_admin_api.py
- [[MemoryTicketStore_1]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[MemoryTicketStore_2]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[MemoryTicketStore_3]] - code - tests/unit_tests/it_support/test_ticket_api.py
- [[MemoryTicketStore_4]] - code - tests/unit_tests/it_support/test_tickets.py
- [[MemoryTicketStore_5]] - code - tests/unit_tests/security/test_security_regression.py
- [[TicketNotFoundError]] - code - src/mcp_rag_agent/it_support/tickets/store.py
- [[TicketRecord]] - code - src/mcp_rag_agent/it_support/tickets/models.py
- [[test_ticket_comments_and_service_methods()]] - code - tests/unit_tests/it_support/test_tickets.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TicketRecord
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_ticketsmodels.py]]
- 17 edges to [[_COMMUNITY_TicketStore]]
- 13 edges to [[_COMMUNITY_TicketService]]
- 11 edges to [[_COMMUNITY_pytest]]
- 5 edges to [[_COMMUNITY_AdminAPIService]]
- 4 edges to [[_COMMUNITY_test_admin_api.py]]
- 2 edges to [[_COMMUNITY_dependencies.py]]
- 2 edges to [[_COMMUNITY_IncidentRecord]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_setup_services]]
- 2 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_Role]]

## Top bridge nodes
- [[TicketRecord]] - degree 79, connects to 8 communities
- [[TicketNotFoundError]] - degree 20, connects to 4 communities
- [[test_ticket_comments_and_service_methods()]] - degree 7, connects to 4 communities
- [[MemoryTicketStore_2]] - degree 11, connects to 3 communities
- [[MemoryTicketStore_5]] - degree 11, connects to 3 communities