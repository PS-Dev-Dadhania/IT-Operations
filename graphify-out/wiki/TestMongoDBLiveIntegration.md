# TestMongoDBLiveIntegration

> 11 nodes · cohesion 0.20

## Key Concepts

- **TestMongoDBLiveIntegration** (8 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **.test_live_mongodb_client_wrapper()** (3 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **fixture** (2 connections)
- **.mongo_uri()** (2 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **.test_db_name()** (2 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **.test_live_document_crud()** (2 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **.test_live_ping()** (2 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **Live integration test suite for MongoDB operations.** (1 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **Verify successful ping command to live MongoDB database.** (1 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **Verify CRUD operations against a live database with cleanup.** (1 connections) — `tests/integration_tests/test_mongodb_integration.py`
- **Verify MongoDBClient wrapper connects and queries properly.** (1 connections) — `tests/integration_tests/test_mongodb_integration.py`

## Relationships

- [typing](typing.md) (2 shared connections)
- [test_mongodb_integration.py](test_mongodb_integration.py.md) (1 shared connections)

## Source Files

- `tests/integration_tests/test_mongodb_integration.py`

## Audit Trail

- EXTRACTED: 12 (86%)
- INFERRED: 2 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*