---
type: community
cohesion: 0.17
members: 12
---

# UserService

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-__init__()_54]] - code - src/mcp_rag_agent/it_support/users/service.py
- [[dot-create_user()]] - code - src/mcp_rag_agent/it_support/users/service.py
- [[dot-get_user_context()]] - code - src/mcp_rag_agent/it_support/users/service.py
- [[dot-list_users()]] - code - src/mcp_rag_agent/it_support/users/service.py
- [[dot-upsert_user()]] - code - src/mcp_rag_agent/it_support/users/service.py
- [[Any_34]] - code
- [[Create or register a user record.]] - rationale - src/mcp_rag_agent/it_support/users/service.py
- [[Domain service managing user context lookups and updates.]] - rationale - src/mcp_rag_agent/it_support/users/service.py
- [[List users matching optional filter criteria.]] - rationale - src/mcp_rag_agent/it_support/users/service.py
- [[Retrieve user context by user_id with validation. Args user_id Unique…]] - rationale - src/mcp_rag_agent/it_support/users/service.py
- [[Upsert a user record (idempotent seeding).]] - rationale - src/mcp_rag_agent/it_support/users/service.py
- [[UserService]] - code - src/mcp_rag_agent/it_support/users/service.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserService
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_UserContextRecord]]
- 3 edges to [[_COMMUNITY_UserNotFoundError]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_usersstore.py]]
- 2 edges to [[_COMMUNITY_setup_services]]
- 1 edge to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 1 edge to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]

## Top bridge nodes
- [[UserService]] - degree 19, connects to 7 communities
- [[dot-list_users()]] - degree 4, connects to 1 community
- [[dot-create_user()]] - degree 3, connects to 1 community
- [[dot-get_user_context()]] - degree 3, connects to 1 community
- [[dot-upsert_user()]] - degree 3, connects to 1 community