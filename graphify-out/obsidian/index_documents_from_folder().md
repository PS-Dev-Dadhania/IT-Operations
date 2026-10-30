---
source_file: "src/mcp_rag_agent/embeddings/index_documents.py"
type: "code"
community: "index_documents_from_folder"
location: "L23"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/index_documents_from_folder
---

# index_documents_from_folder()

## Connections
- [[dot-ingest_directory()]] - `calls` [INFERRED]
- [[dot-test_indexing_processes_text_files()]] - `calls` [INFERRED]
- [[dot-test_non_existent_folder_returns_gracefully()]] - `calls` [INFERRED]
- [[DocumentChunker]] - `calls` [EXTRACTED]
- [[DocumentCleaner]] - `calls` [EXTRACTED]
- [[DocumentIngestionPipeline]] - `calls` [EXTRACTED]
- [[EmbeddingGenerator]] - `calls` [EXTRACTED]
- [[Index all documents from a folder into MongoDB using the production pipeline.…]] - `rationale_for` [EXTRACTED]
- [[MagicMockWrapper]] - `calls` [EXTRACTED]
- [[MongoDBClient]] - `uses` [INFERRED]
- [[Path_6]] - `references` [EXTRACTED]
- [[PipelineSummary]] - `calls` [EXTRACTED]
- [[SemanticSearch]] - `uses` [INFERRED]
- [[_run_legacy_compatible_ingestion()]] - `calls` [EXTRACTED]
- [[index_documents.py]] - `contains` [EXTRACTED]
- [[main()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/index_documents_from_folder