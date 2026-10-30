---
type: community
cohesion: 0.21
members: 18
---

# users/store.py

**Cohesion:** 0.21 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-__init__()_42]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[Enum_8]] - code
- [[MongoDB persistence adapter for users with in-memory fallback support.]] - rationale - src/mcp_rag_agent/it_support/users/store.py
- [[Public user context exports for IT support operations.]] - rationale - src/mcp_rag_agent/it_support/users/__init__.py
- [[SupportTier]] - code - src/mcp_rag_agent/it_support/users/models.py
- [[User domain models and typed schemas for IT support operations.]] - rationale - src/mcp_rag_agent/it_support/users/models.py
- [[User domain service for fetching and managing user context.]] - rationale - src/mcp_rag_agent/it_support/users/service.py
- [[UserStatus]] - code - src/mcp_rag_agent/it_support/users/models.py
- [[_get_default_seed_users()]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[_utc_now()_8]] - code - src/mcp_rag_agent/it_support/users/models.py
- [[datetime_8]] - code
- [[get_seed_users()]] - code - scripts/seed_it_operations_data.py
- [[str_8]] - code
- [[test_user_model_instantiation_and_validation()]] - code - tests/unit_tests/it_support/test_users.py
- [[users__init__.py]] - code - src/mcp_rag_agent/it_support/users/__init__.py
- [[usersmodels.py]] - code - src/mcp_rag_agent/it_support/users/models.py
- [[usersservice.py]] - code - src/mcp_rag_agent/it_support/users/service.py
- [[usersstore.py]] - code - src/mcp_rag_agent/it_support/users/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/users/storepy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_UserContextRecord]]
- 7 edges to [[_COMMUNITY_UserNotFoundError]]
- 5 edges to [[_COMMUNITY_typing]]
- 4 edges to [[_COMMUNITY_setup_services]]
- 3 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 2 edges to [[_COMMUNITY_UserService]]
- 1 edge to [[_COMMUNITY_ServiceStatusChecker]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_datetime]]

## Top bridge nodes
- [[usersstore.py]] - degree 14, connects to 5 communities
- [[usersmodels.py]] - degree 13, connects to 4 communities
- [[users__init__.py]] - degree 11, connects to 4 communities
- [[usersservice.py]] - degree 9, connects to 4 communities
- [[SupportTier]] - degree 12, connects to 3 communities