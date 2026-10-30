# test_ingestion_pipeline.py

> 26 nodes · cohesion 0.09

## Key Concepts

- **test_ingestion_pipeline.py** (15 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **TestDocumentParsers** (14 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **PDFParser** (12 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **TextParser** (11 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.test_corrupt_pdf_raises_parsing_error()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_docx_parser_headings_and_paragraphs()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_pdf_parser_multipage_and_pages()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_text_parser_success()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_unsupported_file_type_raises_error()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **io** (1 connections)
- **mcp_rag_agent_ingestion_chunker** (1 connections)
- **mcp_rag_agent_ingestion_cleaner** (1 connections)
- **mcp_rag_agent_ingestion_models** (1 connections)
- **mcp_rag_agent_ingestion_parsers** (1 connections)
- **mcp_rag_agent_ingestion_pipeline** (1 connections)
- **.supported_extensions()** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Parser for PDF (.pdf) documents with page number tracking.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Parser for plain text (.txt) files.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.supported_extensions()** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Comprehensive unit tests for production-grade document ingestion pipeline.…** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify DOCX parser parses paragraphs and captures heading sections.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify unsupported extensions raise UnsupportedFileTypeError.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify corrupt PDF raises ParsingError.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Test suite for format-specific parsers.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Verify plain text parsing and title extraction.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- *... and 1 more nodes in this community*

## Relationships

- [ingestion/__init__.py](ingestion-__init__.py.md) (9 shared connections)
- [ParsedDocument](ParsedDocument.md) (8 shared connections)
- [MarkdownParser](MarkdownParser.md) (4 shared connections)
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) (2 shared connections)
- [pytest](pytest.md) (1 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (1 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [DocumentCleaner](DocumentCleaner.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/ingestion/parsers.py`
- `tests/unit_tests/test_ingestion_pipeline.py`

## Audit Trail

- EXTRACTED: 41 (75%)
- INFERRED: 14 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*