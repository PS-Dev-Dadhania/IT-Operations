# DocumentIngestionPipeline

> 21 nodes · cohesion 0.16

## Key Concepts

- **DocumentIngestionPipeline** (32 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **TestIngestionFailures** (9 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **asyncio** (7 connections)
- **TestDuplicateDetectionAndIncrementalIngestion** (7 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_duplicate_file_skipped_when_hash_matches()** (5 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_new_file_ingested_cleanly()** (4 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_reindex_flag_purges_old_chunks_and_reindexes()** (4 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_unsupported_file_type_in_directory_scan_is_ignored()** (4 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.clear_indexes()** (3 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **.test_embedding_generation_failure_returns_failed_result()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_empty_file_returns_failed_result()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_non_existent_file_returns_failed_result()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_clear_indexes()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **End-to-end scalable pipeline for ingesting, chunking, embedding, and indexing…** (1 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **Delete all documents and vectors from both collections. Returns: Dictionary…** (1 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **Test suite for hash-based deduplication and reindexing.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify identical content hash causes pipeline to skip file.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify reindex=True deletes old records and re-ingests.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify new file without duplicate records is cleanly ingested.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Test suite for failure handling and edge cases.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Unsupported files should be excluded from candidate files.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`

## Relationships

- [index_documents_from_folder](index_documents_from_folder.md) (7 shared connections)
- [typing](typing.md) (7 shared connections)
- [ingestion/__init__.py](ingestion-__init__.py.md) (6 shared connections)
- [ParsedDocument](ParsedDocument.md) (2 shared connections)
- [test_ingestion_pipeline.py](test_ingestion_pipeline.py.md) (2 shared connections)
- [DocumentCleaner](DocumentCleaner.md) (1 shared connections)
- [MarkdownParser](MarkdownParser.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/ingestion/pipeline.py`
- `tests/unit_tests/test_ingestion_pipeline.py`

## Audit Trail

- EXTRACTED: 36 (60%)
- INFERRED: 24 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*