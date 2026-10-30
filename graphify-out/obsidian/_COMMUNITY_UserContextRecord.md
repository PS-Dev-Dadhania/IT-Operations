---
type: community
cohesion: 0.37
members: 13
---

# UserContextRecord

**Cohesion:** 0.37 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-_collection()_6]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[dot-_to_record()_4]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[dot-create()_16]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[dot-get()_23]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[dot-list()_9]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[dot-update_fields()_9]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[dot-upsert()_5]] - code - src/mcp_rag_agent/it_support/users/store.py
- [[Any_33]] - code
- [[BaseModel_22]] - code
- [[Persistence store for enterprise user context with in-memory fallback.]] - rationale - src/mcp_rag_agent/it_support/users/store.py
- [[Pydantic model representing an enterprise employee  support user.]] - rationale - src/mcp_rag_agent/it_support/users/models.py
- [[UserContextRecord]] - code - src/mcp_rag_agent/it_support/users/models.py
- [[UserStore]] - code - src/mcp_rag_agent/it_support/users/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/UserContextRecord
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_UserNotFoundError]]
- 10 edges to [[_COMMUNITY_usersstore.py]]
- 7 edges to [[_COMMUNITY_UserService]]
- 4 edges to [[_COMMUNITY_setup_services]]
- 2 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_test_tool_authorization_success_emits_audit_log]]
- 1 edge to [[_COMMUNITY_ServiceStatusChecker]]

## Top bridge nodes
- [[UserContextRecord]] - degree 34, connects to 6 communities
- [[UserStore]] - degree 20, connects to 6 communities
- [[dot-get()_23]] - degree 6, connects to 1 community
- [[dot-_to_record()_4]] - degree 6, connects to 1 community
- [[dot-update_fields()_9]] - degree 6, connects to 1 community