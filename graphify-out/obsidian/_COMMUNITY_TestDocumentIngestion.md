---
type: community
cohesion: 0.25
members: 9
---

# TestDocumentIngestion

**Cohesion:** 0.25 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-test_default_ingested_directory_resolved_as_path()]] - code - tests/unit_tests/test_ingestion.py
- [[dot-test_indexing_processes_text_files()]] - code - tests/unit_tests/test_ingestion.py
- [[dot-test_non_existent_folder_returns_gracefully()]] - code - tests/unit_tests/test_ingestion.py
- [[Test suite for document ingestion.]] - rationale - tests/unit_tests/test_ingestion.py
- [[TestDocumentIngestion]] - code - tests/unit_tests/test_ingestion.py
- [[Verify indexing reads text files and stores in both documents and vectors…]] - rationale - tests/unit_tests/test_ingestion.py
- [[Verify ingested doc directory resolves to valid Path object.]] - rationale - tests/unit_tests/test_ingestion.py
- [[Verify non-existent folder does not crash and returns early.]] - rationale - tests/unit_tests/test_ingestion.py
- [[asyncio_18]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDocumentIngestion
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_index_documents_from_folder]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[TestDocumentIngestion]] - degree 5, connects to 1 community
- [[dot-test_indexing_processes_text_files()]] - degree 4, connects to 1 community
- [[dot-test_non_existent_folder_returns_gracefully()]] - degree 4, connects to 1 community