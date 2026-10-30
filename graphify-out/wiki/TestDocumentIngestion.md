# TestDocumentIngestion

> 9 nodes · cohesion 0.25

## Key Concepts

- **TestDocumentIngestion** (5 connections) — `tests/unit_tests/test_ingestion.py`
- **.test_indexing_processes_text_files()** (4 connections) — `tests/unit_tests/test_ingestion.py`
- **.test_non_existent_folder_returns_gracefully()** (4 connections) — `tests/unit_tests/test_ingestion.py`
- **asyncio** (2 connections)
- **.test_default_ingested_directory_resolved_as_path()** (2 connections) — `tests/unit_tests/test_ingestion.py`
- **Test suite for document ingestion.** (1 connections) — `tests/unit_tests/test_ingestion.py`
- **Verify non-existent folder does not crash and returns early.** (1 connections) — `tests/unit_tests/test_ingestion.py`
- **Verify indexing reads text files and stores in both documents and vectors…** (1 connections) — `tests/unit_tests/test_ingestion.py`
- **Verify ingested doc directory resolves to valid Path object.** (1 connections) — `tests/unit_tests/test_ingestion.py`

## Relationships

- [index_documents_from_folder](index_documents_from_folder.md) (2 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)

## Source Files

- `tests/unit_tests/test_ingestion.py`

## Audit Trail

- EXTRACTED: 10 (83%)
- INFERRED: 2 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*