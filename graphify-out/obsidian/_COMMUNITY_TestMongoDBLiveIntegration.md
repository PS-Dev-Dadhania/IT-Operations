---
type: community
cohesion: 0.20
members: 11
---

# TestMongoDBLiveIntegration

**Cohesion:** 0.20 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-mongo_uri()]] - code - tests/integration_tests/test_mongodb_integration.py
- [[dot-test_db_name()]] - code - tests/integration_tests/test_mongodb_integration.py
- [[dot-test_live_document_crud()]] - code - tests/integration_tests/test_mongodb_integration.py
- [[dot-test_live_mongodb_client_wrapper()]] - code - tests/integration_tests/test_mongodb_integration.py
- [[dot-test_live_ping()]] - code - tests/integration_tests/test_mongodb_integration.py
- [[Live integration test suite for MongoDB operations.]] - rationale - tests/integration_tests/test_mongodb_integration.py
- [[TestMongoDBLiveIntegration]] - code - tests/integration_tests/test_mongodb_integration.py
- [[Verify CRUD operations against a live database with cleanup.]] - rationale - tests/integration_tests/test_mongodb_integration.py
- [[Verify MongoDBClient wrapper connects and queries properly.]] - rationale - tests/integration_tests/test_mongodb_integration.py
- [[Verify successful ping command to live MongoDB database.]] - rationale - tests/integration_tests/test_mongodb_integration.py
- [[fixture_11]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMongoDBLiveIntegration
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_test_mongodb_integration.py]]

## Top bridge nodes
- [[TestMongoDBLiveIntegration]] - degree 8, connects to 2 communities
- [[dot-test_live_mongodb_client_wrapper()]] - degree 3, connects to 1 community