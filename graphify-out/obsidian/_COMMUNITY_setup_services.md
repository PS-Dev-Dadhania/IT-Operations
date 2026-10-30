---
type: community
cohesion: 0.13
members: 18
---

# setup_services

**Cohesion:** 0.13 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-__init__()_43]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-get()_19]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-teardown_method()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-teardown_method()_1]] - code - tests/unit_tests/test_tools_and_retriever.py
- [[Clean up retriever singleton after each test.]] - rationale - tests/unit_tests/test_tools_and_retriever.py
- [[MemoryUserStore_2]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[Reset the cached retriever, IT services, and MongoDB client instances.]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Set or override the DeviceService instance.]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Set or override the TicketService instance.]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Set or override the UserService instance.]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[fixture_7]] - code
- [[fixture_8]] - code
- [[reset_retriever()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[set_device_service()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[set_ticket_service()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[set_user_service()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[setup_services()]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[setup_services()_1]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/setup_services
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_mcp_servertools.py]]
- 6 edges to [[_COMMUNITY_DeviceRecord]]
- 4 edges to [[_COMMUNITY_usersstore.py]]
- 4 edges to [[_COMMUNITY_UserContextRecord]]
- 3 edges to [[_COMMUNITY_UserNotFoundError]]
- 3 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 2 edges to [[_COMMUNITY_TicketRecord]]
- 2 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 2 edges to [[_COMMUNITY_TicketService]]
- 2 edges to [[_COMMUNITY_UserService]]
- 2 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 1 edge to [[_COMMUNITY_ConfigurationError]]
- 1 edge to [[_COMMUNITY_TestTypedToolInterface]]

## Top bridge nodes
- [[setup_services()]] - degree 18, connects to 10 communities
- [[setup_services()_1]] - degree 18, connects to 9 communities
- [[MemoryUserStore_2]] - degree 6, connects to 3 communities
- [[reset_retriever()]] - degree 7, connects to 2 communities
- [[set_device_service()]] - degree 6, connects to 2 communities