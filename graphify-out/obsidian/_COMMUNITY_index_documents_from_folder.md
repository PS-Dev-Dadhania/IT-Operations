---
type: community
cohesion: 0.14
members: 19
---

# index_documents_from_folder

**Cohesion:** 0.14 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-compute_content_hash()]] - code - src/mcp_rag_agent/ingestion/pipeline.py
- [[dot-generate()_1]] - code - src/mcp_rag_agent/embeddings/index_documents.py
- [[dot-generate_batch()_1]] - code - src/mcp_rag_agent/embeddings/index_documents.py
- [[dot-ingest_directory()]] - code - src/mcp_rag_agent/ingestion/pipeline.py
- [[dot-ingest_file()]] - code - src/mcp_rag_agent/ingestion/pipeline.py
- [[Aggregate summary of an ingestion run across multiple documents.]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[Any_25]] - code
- [[Compute SHA-256 hash of file content. Args file_path Path to the target file.…]] - rationale - src/mcp_rag_agent/ingestion/pipeline.py
- [[Fallback generator for mock tests when real EmbeddingGenerator is absent.]] - rationale - src/mcp_rag_agent/embeddings/index_documents.py
- [[Helper for mock-based tests asserting on semantic_search.index_document.]] - rationale - src/mcp_rag_agent/embeddings/index_documents.py
- [[Index all documents from a folder into MongoDB using the production pipeline.…]] - rationale - src/mcp_rag_agent/embeddings/index_documents.py
- [[MagicMockWrapper]] - code - src/mcp_rag_agent/embeddings/index_documents.py
- [[Path_6]] - code
- [[Path_7]] - code
- [[PipelineSummary]] - code - src/mcp_rag_agent/ingestion/models.py
- [[Process, chunk, embed, and store a single document. Args file_path Path to…]] - rationale - src/mcp_rag_agent/ingestion/pipeline.py
- [[Scan directory recursively and ingest all supported documents. Args…]] - rationale - src/mcp_rag_agent/ingestion/pipeline.py
- [[_run_legacy_compatible_ingestion()]] - code - src/mcp_rag_agent/embeddings/index_documents.py
- [[index_documents_from_folder()]] - code - src/mcp_rag_agent/embeddings/index_documents.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/index_documents_from_folder
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_typing]]
- 7 edges to [[_COMMUNITY_DocumentIngestionPipeline]]
- 5 edges to [[_COMMUNITY_ingestion__init__.py]]
- 2 edges to [[_COMMUNITY_ParsedDocument]]
- 2 edges to [[_COMMUNITY_TestDocumentIngestion]]
- 1 edge to [[_COMMUNITY_DocumentCleaner]]

## Top bridge nodes
- [[index_documents_from_folder()]] - degree 16, connects to 5 communities
- [[PipelineSummary]] - degree 10, connects to 4 communities
- [[_run_legacy_compatible_ingestion()]] - degree 10, connects to 3 communities
- [[dot-ingest_file()]] - degree 6, connects to 2 communities
- [[dot-compute_content_hash()]] - degree 6, connects to 1 community