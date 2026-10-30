# DocumentCleaner

> 12 nodes · cohesion 0.23

## Key Concepts

- **DocumentCleaner** (18 connections) — `src/mcp_rag_agent/ingestion/cleaner.py`
- **TestDocumentCleaner** (7 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.__init__()** (3 connections) — `src/mcp_rag_agent/ingestion/chunker.py`
- **.clean()** (2 connections) — `src/mcp_rag_agent/ingestion/cleaner.py`
- **.test_clean_handles_empty_or_whitespace_string()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_clean_normalizes_crlf_and_excessive_newlines()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_clean_normalizes_unicode_nfkc()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_clean_removes_null_bytes_and_control_characters()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Initialize DocumentChunker. Args: chunk_size: Maximum character length per…** (1 connections) — `src/mcp_rag_agent/ingestion/chunker.py`
- **Clean and normalize a text string. Args: text: Raw input string from document…** (1 connections) — `src/mcp_rag_agent/ingestion/cleaner.py`
- **Sanitizes and normalizes extracted text from documents.** (1 connections) — `src/mcp_rag_agent/ingestion/cleaner.py`
- **Test suite for DocumentCleaner.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`

## Relationships

- [typing](typing.md) (6 shared connections)
- [ParsedDocument](ParsedDocument.md) (2 shared connections)
- [index_documents_from_folder](index_documents_from_folder.md) (1 shared connections)
- [ingestion/__init__.py](ingestion-__init__.py.md) (1 shared connections)
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) (1 shared connections)
- [test_ingestion_pipeline.py](test_ingestion_pipeline.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/ingestion/chunker.py`
- `src/mcp_rag_agent/ingestion/cleaner.py`
- `tests/unit_tests/test_ingestion_pipeline.py`

## Audit Trail

- EXTRACTED: 20 (74%)
- INFERRED: 7 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*