---
type: community
cohesion: 0.23
members: 12
---

# DocumentCleaner

**Cohesion:** 0.23 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-__init__()_52]] - code - src/mcp_rag_agent/ingestion/chunker.py
- [[dot-clean()]] - code - src/mcp_rag_agent/ingestion/cleaner.py
- [[dot-test_clean_handles_empty_or_whitespace_string()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_clean_normalizes_crlf_and_excessive_newlines()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_clean_normalizes_unicode_nfkc()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_clean_removes_null_bytes_and_control_characters()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[Clean and normalize a text string. Args text Raw input string from document…]] - rationale - src/mcp_rag_agent/ingestion/cleaner.py
- [[DocumentCleaner]] - code - src/mcp_rag_agent/ingestion/cleaner.py
- [[Initialize DocumentChunker. Args chunk_size Maximum character length per…]] - rationale - src/mcp_rag_agent/ingestion/chunker.py
- [[Sanitizes and normalizes extracted text from documents.]] - rationale - src/mcp_rag_agent/ingestion/cleaner.py
- [[Test suite for DocumentCleaner.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[TestDocumentCleaner]] - code - tests/unit_tests/test_ingestion_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DocumentCleaner
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_ParsedDocument]]
- 1 edge to [[_COMMUNITY_DocumentIngestionPipeline]]
- 1 edge to [[_COMMUNITY_index_documents_from_folder]]
- 1 edge to [[_COMMUNITY_ingestion__init__.py]]
- 1 edge to [[_COMMUNITY_test_ingestion_pipeline.py]]

## Top bridge nodes
- [[DocumentCleaner]] - degree 18, connects to 5 communities
- [[TestDocumentCleaner]] - degree 7, connects to 1 community
- [[dot-__init__()_52]] - degree 3, connects to 1 community