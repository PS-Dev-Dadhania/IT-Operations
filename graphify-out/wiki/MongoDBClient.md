# MongoDBClient

> God node · 72 connections · `src/mcp_rag_agent/mongodb/client.py`

**Community:** [typing](typing.md)

## Connections by Relation

### calls
- main() `EXTRACTED`
- main() `EXTRACTED`
- get_admin_service() `EXTRACTED`
- main() `EXTRACTED`
- get_mongo_client() `EXTRACTED`
- get_it_ticket_service() `EXTRACTED`
- main() `EXTRACTED`
- .test_connect_records_database_error_on_failure() `INFERRED`
- .test_vector_search_records_telemetry_in_tracer() `INFERRED`
- .client() `INFERRED`
- .test_live_mongodb_client_wrapper() `INFERRED`

### contains
- client.py `EXTRACTED`

### imports
- [mcp_server/tools.py](mcp_server-tools.py.md) `EXTRACTED`
- [dependencies.py](dependencies.py.md) `EXTRACTED`
- index_documents.py `EXTRACTED`
- ingestion/pipeline.py `EXTRACTED`
- [retrieval/pipeline.py](retrieval-pipeline.py.md) `EXTRACTED`
- [approval.py](approval.py.md) `EXTRACTED`
- [audit.py](audit.py.md) `EXTRACTED`
- tickets/store.py `EXTRACTED`
- incidents/store.py `EXTRACTED`
- [users/store.py](users-store.py.md) `EXTRACTED`
- services/store.py `EXTRACTED`
- devices/store.py `EXTRACTED`
- semantic_search.py `EXTRACTED`
- mcp_rag_agent/mongodb/__init__.py `EXTRACTED`
- hybrid_search.py `EXTRACTED`

### method
- .get_collection() `EXTRACTED`
- .connect() `EXTRACTED`
- .create_collection() `EXTRACTED`
- .vector_search() `EXTRACTED`
- .text_search() `EXTRACTED`
- .db() `EXTRACTED`
- .collection_exists() `EXTRACTED`
- .delete_documents() `EXTRACTED`
- .disconnect() `EXTRACTED`
- .hybrid_search() `EXTRACTED`
- .list_collections() `EXTRACTED`
- .insert_document() `EXTRACTED`
- .insert_documents() `EXTRACTED`
- .find_documents() `EXTRACTED`
- .create_text_search_index() `EXTRACTED`
- .create_vector_search_index() `EXTRACTED`
- .__init__() `EXTRACTED`

### rationale_for
- MongoDB client wrapper for semantic search operations. `EXTRACTED`

### references
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) `INFERRED`
- [AdvancedRetriever](AdvancedRetriever.md) `INFERRED`
- [TestMongoDBClient](TestMongoDBClient.md) `INFERRED`
- index_documents_from_folder() `INFERRED`
- HybridSearch `INFERRED`
- SemanticSearch `INFERRED`
- get_audit_service() `INFERRED`
- get_service_status_checker() `INFERRED`
- get_ticket_service() `INFERRED`
- seed_it_operations_data() `INFERRED`
- get_device_service() `INFERRED`
- get_incident_service() `INFERRED`
- get_user_service() `INFERRED`
- [TestMongoDBLiveIntegration](TestMongoDBLiveIntegration.md) `INFERRED`
- get_approval_service() `INFERRED`
- TestMongoDBClientTelemetry `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*