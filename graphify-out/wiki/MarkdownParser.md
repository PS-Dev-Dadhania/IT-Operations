# MarkdownParser

> 12 nodes · cohesion 0.17

## Key Concepts

- **MarkdownParser** (11 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **ParserRegistry** (10 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.__init__()** (5 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.is_supported()** (3 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.register_parser()** (3 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.test_markdown_parser_headings_and_sections()** (3 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.supported_extensions()** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Parser for Markdown (.md, .markdown) files with heading awareness.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Registry managing available document parsers.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Register a custom document parser.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Check if a file format is supported.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Verify markdown parser extracts title and partitions by headings.** (1 connections) — `tests/unit_tests/test_ingestion_pipeline.py`

## Relationships

- [ingestion/__init__.py](ingestion-__init__.py.md) (8 shared connections)
- [ParsedDocument](ParsedDocument.md) (4 shared connections)
- [test_ingestion_pipeline.py](test_ingestion_pipeline.py.md) (4 shared connections)
- [typing](typing.md) (2 shared connections)
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/ingestion/parsers.py`
- `tests/unit_tests/test_ingestion_pipeline.py`

## Audit Trail

- EXTRACTED: 25 (83%)
- INFERRED: 5 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*