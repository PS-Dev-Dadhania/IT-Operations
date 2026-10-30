# TestMongoDBClient

> 45 nodes · cohesion 0.05

## Key Concepts

- **TestMongoDBClient** (24 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.client()** (4 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.mock_mongo_client()** (4 connections) — `tests/unit_tests/mongodb/test_client.py`
- **fixture** (2 connections)
- **.test_collection_exists_false()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_collection_exists_true()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_connect()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_connect_idempotent()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_create_collection()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_create_vector_search_index()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_db_property_auto_connects()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_db_property_returns_existing()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_delete_documents()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_disconnect()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_disconnect_when_not_connected()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_find_documents()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_get_collection()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_init()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_insert_document()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_insert_documents()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_list_collections()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_vector_search()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **.test_vector_search_with_filter()** (2 connections) — `tests/unit_tests/mongodb/test_client.py`
- **Test listing collections.** (1 connections) — `tests/unit_tests/mongodb/test_client.py`
- **Test creating a collection.** (1 connections) — `tests/unit_tests/mongodb/test_client.py`
- *... and 20 more nodes in this community*

## Relationships

- [typing](typing.md) (2 shared connections)
- [test_mongodb_integration.py](test_mongodb_integration.py.md) (1 shared connections)
- [tickets/models.py](tickets-models.py.md) (1 shared connections)

## Source Files

- `tests/unit_tests/mongodb/test_client.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*