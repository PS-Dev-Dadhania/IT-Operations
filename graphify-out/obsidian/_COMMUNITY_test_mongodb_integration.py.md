---
type: community
cohesion: 0.18
members: 11
---

# test_mongodb_integration.py

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[Check whether a reachable MongoDB instance is configured.]] - rationale - tests/integration_tests/test_mongodb_integration.py
- [[Integration tests for live MongoDB connectivity, document operations, and…]] - rationale - tests/integration_tests/test_mongodb_integration.py
- [[Unit tests for MongoDB client.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[bson]] - concept
- [[is_mongodb_available()]] - code - tests/integration_tests/test_mongodb_integration.py
- [[mcp_rag_agent_mongodb_client]] - concept
- [[pymongo_collection]] - concept
- [[pymongo_database]] - concept
- [[pymongo_results]] - concept
- [[test_client.py]] - code - tests/unit_tests/mongodb/test_client.py
- [[test_mongodb_integration.py]] - code - tests/integration_tests/test_mongodb_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_mongodb_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_pytest]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_TestMongoDBClient]]
- 1 edge to [[_COMMUNITY_TestMongoDBLiveIntegration]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_test_observability.py]]

## Top bridge nodes
- [[test_mongodb_integration.py]] - degree 9, connects to 5 communities
- [[test_client.py]] - degree 9, connects to 3 communities
- [[mcp_rag_agent_mongodb_client]] - degree 4, connects to 2 communities
- [[pymongo_collection]] - degree 2, connects to 1 community
- [[pymongo_database]] - degree 2, connects to 1 community