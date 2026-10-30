---
type: community
cohesion: 0.05
members: 45
---

# TestMongoDBClient

**Cohesion:** 0.05 - loosely connected
**Members:** 45 nodes

## Members
- [[dot-client()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-mock_mongo_client()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_collection_exists_false()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_collection_exists_true()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_connect()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_connect_idempotent()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_create_collection()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_create_vector_search_index()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_db_property_auto_connects()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_db_property_returns_existing()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_delete_documents()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_disconnect()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_disconnect_when_not_connected()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_find_documents()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_get_collection()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_init()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_insert_document()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_insert_documents()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_list_collections()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_vector_search()]] - code - tests/unit_tests/mongodb/test_client.py
- [[dot-test_vector_search_with_filter()]] - code - tests/unit_tests/mongodb/test_client.py
- [[Create MongoDBClient instance with mocked dependencies.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Create a mocked MongoClient.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test checking if collection exists (false case).]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test checking if collection exists (true case).]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test client initialization.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test connecting to MongoDB.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test creating a collection.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test creating a vector search index.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test deleting documents.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test disconnect when not connected does nothing.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test disconnecting from MongoDB.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test finding documents.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test getting a collection.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test inserting a single document.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test inserting multiple documents.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test listing collections.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test suite for MongoDBClient class.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test that connect is idempotent.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test that db property auto-connects if not connected.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test that db property returns existing connection.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test vector search with filter query.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[Test vector similarity search.]] - rationale - tests/unit_tests/mongodb/test_client.py
- [[TestMongoDBClient]] - code - tests/unit_tests/mongodb/test_client.py
- [[fixture_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMongoDBClient
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_test_mongodb_integration.py]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]

## Top bridge nodes
- [[TestMongoDBClient]] - degree 24, connects to 2 communities
- [[dot-client()]] - degree 4, connects to 1 community
- [[dot-mock_mongo_client()]] - degree 4, connects to 1 community