---
type: community
cohesion: 0.14
members: 21
---

# UserNotFoundError

**Cohesion:** 0.14 - loosely connected
**Members:** 21 nodes

## Members
- [[dot-__init__()_38]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-__init__()_39]] - code - tests/unit_tests/it_support/test_users.py
- [[dot-create()_12]] - code - tests/unit_tests/it_support/test_users.py
- [[dot-get()_16]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-get()_17]] - code - tests/unit_tests/it_support/test_users.py
- [[dot-list()_7]] - code - tests/unit_tests/it_support/test_users.py
- [[dot-update_fields()_6]] - code - tests/unit_tests/it_support/test_users.py
- [[dot-upsert()_4]] - code - tests/unit_tests/it_support/test_users.py
- [[In-memory test double for UserStore.]] - rationale - tests/unit_tests/it_support/test_users.py
- [[KeyError_4]] - code
- [[MemoryUserStore]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[MemoryUserStore_1]] - code - tests/unit_tests/it_support/test_users.py
- [[Raised when a requested user cannot be found.]] - rationale - src/mcp_rag_agent/it_support/users/store.py
- [[Unit tests for user context models, store, and domain service.]] - rationale - tests/unit_tests/it_support/test_users.py
- [[UserNotFoundError]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[_sample_user()]] - code - tests/unit_tests/it_support/test_users.py
- [[test_user_service_invalid_id_raises_value_error()]] - code - tests/unit_tests/it_support/test_users.py
- [[test_user_service_missing_user_raises_not_found()]] - code - tests/unit_tests/it_support/test_users.py
- [[test_user_service_valid_lookup()]] - code - tests/unit_tests/it_support/test_users.py
- [[test_user_store_mongodb_adapter()]] - code - tests/unit_tests/it_support/test_users.py
- [[test_users.py]] - code - tests/unit_tests/it_support/test_users.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserNotFoundError
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_UserContextRecord]]
- 7 edges to [[_COMMUNITY_usersstore.py]]
- 4 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 4 edges to [[_COMMUNITY_pytest]]
- 3 edges to [[_COMMUNITY_setup_services]]
- 3 edges to [[_COMMUNITY_UserService]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[UserNotFoundError]] - degree 20, connects to 5 communities
- [[test_users.py]] - degree 13, connects to 4 communities
- [[MemoryUserStore]] - degree 6, connects to 3 communities
- [[_sample_user()]] - degree 7, connects to 2 communities
- [[test_user_service_missing_user_raises_not_found()]] - degree 5, connects to 2 communities