---
source_file: "src/mcp_rag_agent/ingestion/pipeline.py"
type: "code"
community: "DocumentIngestionPipeline"
location: "L30"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/DocumentIngestionPipeline
---

# DocumentIngestionPipeline

## Connections
- [[dot-__init__()_3]] - `method` [EXTRACTED]
- [[dot-clear_indexes()]] - `method` [EXTRACTED]
- [[dot-compute_content_hash()]] - `method` [EXTRACTED]
- [[dot-ingest_directory()]] - `method` [EXTRACTED]
- [[dot-ingest_file()]] - `method` [EXTRACTED]
- [[dot-test_clear_indexes()]] - `calls` [INFERRED]
- [[dot-test_duplicate_file_skipped_when_hash_matches()]] - `calls` [INFERRED]
- [[dot-test_embedding_generation_failure_returns_failed_result()]] - `calls` [INFERRED]
- [[dot-test_empty_file_returns_failed_result()]] - `calls` [INFERRED]
- [[dot-test_new_file_ingested_cleanly()]] - `calls` [INFERRED]
- [[dot-test_non_existent_file_returns_failed_result()]] - `calls` [INFERRED]
- [[dot-test_reindex_flag_purges_old_chunks_and_reindexes()]] - `calls` [INFERRED]
- [[dot-test_unsupported_file_type_in_directory_scan_is_ignored()]] - `calls` [INFERRED]
- [[DocumentChunk]] - `uses` [INFERRED]
- [[DocumentChunker]] - `uses` [INFERRED]
- [[DocumentCleaner]] - `uses` [INFERRED]
- [[EmbeddingGenerator]] - `uses` [INFERRED]
- [[End-to-end scalable pipeline for ingesting, chunking, embedding, and indexing…]] - `rationale_for` [EXTRACTED]
- [[IngestionResult]] - `uses` [INFERRED]
- [[IngestionStatus]] - `uses` [INFERRED]
- [[MongoDBClient]] - `uses` [INFERRED]
- [[ParserRegistry]] - `uses` [INFERRED]
- [[PipelineSummary]] - `uses` [INFERRED]
- [[TestDuplicateDetectionAndIncrementalIngestion]] - `uses` [INFERRED]
- [[TestIngestionFailures]] - `uses` [INFERRED]
- [[UnsupportedFileTypeError]] - `uses` [INFERRED]
- [[_run_legacy_compatible_ingestion()]] - `uses` [INFERRED]
- [[index_documents.py]] - `imports` [EXTRACTED]
- [[index_documents_from_folder()]] - `calls` [EXTRACTED]
- [[ingestion__init__.py]] - `imports` [EXTRACTED]
- [[ingestionpipeline.py]] - `contains` [EXTRACTED]
- [[main()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/DocumentIngestionPipeline