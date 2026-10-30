# ParsedDocument

> 27 nodes · cohesion 0.15

## Key Concepts

- **ParsedDocument** (21 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **DocumentChunker** (18 connections) — `src/mcp_rag_agent/ingestion/chunker.py`
- **DocumentSegment** (16 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **DocumentChunk** (10 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Path** (10 connections)
- **ParsingError** (9 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **TestDocumentChunker** (8 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **._clean_title_from_filename()** (7 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.parse()** (7 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.parse()** (7 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.parse()** (6 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.parse()** (6 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **BaseModel** (5 connections)
- **.chunk_document()** (4 connections) — `src/mcp_rag_agent/ingestion/chunker.py`
- **.parse()** (4 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.test_chunker_preserves_section_and_page_metadata()** (4 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_chunker_splits_long_text_and_sets_indices()** (4 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **.test_invalid_parameters_raise_value_error()** (2 connections) — `tests/unit_tests/test_ingestion_pipeline.py`
- **Chunks documents intelligently while preserving section/page structure and…** (1 connections) — `src/mcp_rag_agent/ingestion/chunker.py`
- **Split a parsed document into structured DocumentChunks. Args: parsed_doc: The…** (1 connections) — `src/mcp_rag_agent/ingestion/chunker.py`
- **A logical segment of a document (e.g., page, section, or paragraph).** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Represents a document extracted by a parser before chunking.** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Represents an individual text chunk ready for embedding and storage.** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Raised when parsing fails due to corruption, encryption, or format issues.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Parse file content and return structured ParsedDocument. Args: file_path: Path…** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- *... and 2 more nodes in this community*

## Relationships

- [ingestion/__init__.py](ingestion-__init__.py.md) (24 shared connections)
- [typing](typing.md) (8 shared connections)
- [test_ingestion_pipeline.py](test_ingestion_pipeline.py.md) (8 shared connections)
- [MarkdownParser](MarkdownParser.md) (4 shared connections)
- [index_documents_from_folder](index_documents_from_folder.md) (2 shared connections)
- [DocumentCleaner](DocumentCleaner.md) (2 shared connections)
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) (2 shared connections)
- [.to_vector_document](to_vector_document.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/ingestion/chunker.py`
- `src/mcp_rag_agent/ingestion/models.py`
- `src/mcp_rag_agent/ingestion/parsers.py`
- `tests/unit_tests/test_ingestion_pipeline.py`

## Audit Trail

- EXTRACTED: 79 (76%)
- INFERRED: 25 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*