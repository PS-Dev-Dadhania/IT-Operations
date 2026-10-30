---
type: community
cohesion: 0.16
members: 21
---

# DocumentIngestionPipeline

**Cohesion:** 0.16 - loosely connected
**Members:** 21 nodes

## Members
- [[dot-clear_indexes()]] - code - src/mcp_rag_agent/ingestion/pipeline.py
- [[dot-test_clear_indexes()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_duplicate_file_skipped_when_hash_matches()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_embedding_generation_failure_returns_failed_result()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_empty_file_returns_failed_result()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_new_file_ingested_cleanly()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_non_existent_file_returns_failed_result()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_reindex_flag_purges_old_chunks_and_reindexes()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_unsupported_file_type_in_directory_scan_is_ignored()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[Delete all documents and vectors from both collections. Returns Dictionary…]] - rationale - src/mcp_rag_agent/ingestion/pipeline.py
- [[DocumentIngestionPipeline]] - code - src/mcp_rag_agent/ingestion/pipeline.py
- [[End-to-end scalable pipeline for ingesting, chunking, embedding, and indexing…]] - rationale - src/mcp_rag_agent/ingestion/pipeline.py
- [[Test suite for failure handling and edge cases.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Test suite for hash-based deduplication and reindexing.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[TestDuplicateDetectionAndIncrementalIngestion]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[TestIngestionFailures]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[Unsupported files should be excluded from candidate files.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify identical content hash causes pipeline to skip file.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify new file without duplicate records is cleanly ingested.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify reindex=True deletes old records and re-ingests.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[asyncio_12]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DocumentIngestionPipeline
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_typing]]
- 7 edges to [[_COMMUNITY_index_documents_from_folder]]
- 6 edges to [[_COMMUNITY_ingestion__init__.py]]
- 2 edges to [[_COMMUNITY_ParsedDocument]]
- 2 edges to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 1 edge to [[_COMMUNITY_DocumentCleaner]]
- 1 edge to [[_COMMUNITY_MarkdownParser]]

## Top bridge nodes
- [[DocumentIngestionPipeline]] - degree 32, connects to 6 communities
- [[TestIngestionFailures]] - degree 9, connects to 2 communities
- [[TestDuplicateDetectionAndIncrementalIngestion]] - degree 7, connects to 2 communities
- [[dot-test_duplicate_file_skipped_when_hash_matches()]] - degree 5, connects to 1 community
- [[dot-clear_indexes()]] - degree 3, connects to 1 community