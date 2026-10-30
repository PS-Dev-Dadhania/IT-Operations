# ingestion/__init__.py

> 31 nodes · cohesion 0.10

## Key Concepts

- **ingestion/__init__.py** (25 connections) — `src/mcp_rag_agent/ingestion/__init__.py`
- **parsers.py** (22 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **ingestion/models.py** (16 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **BaseDocumentParser** (16 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **IngestionStatus** (11 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **DocxParser** (11 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **IngestionResult** (9 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **IngestionError** (8 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **UnsupportedFileTypeError** (8 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **get_parser()** (5 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.get_parser()** (5 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.can_handle()** (4 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **.supported_extensions()** (3 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Enum** (2 connections)
- **ABC** (2 connections)
- **Document Ingestion Subsystem for MCP RAG Agent. Provides production-grade…** (1 connections) — `src/mcp_rag_agent/ingestion/__init__.py`
- **str** (1 connections)
- **Data models for document ingestion and chunking.** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Status outcomes for document ingestion.** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Result summary for a single document ingestion.** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **.supported_extensions()** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Exception** (1 connections)
- **Document parsers for TXT, Markdown, PDF, and DOCX formats.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Base exception for ingestion errors.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- **Raised when an unsupported file extension is encountered.** (1 connections) — `src/mcp_rag_agent/ingestion/parsers.py`
- *... and 6 more nodes in this community*

## Relationships

- [ParsedDocument](ParsedDocument.md) (24 shared connections)
- [typing](typing.md) (16 shared connections)
- [test_ingestion_pipeline.py](test_ingestion_pipeline.py.md) (9 shared connections)
- [MarkdownParser](MarkdownParser.md) (8 shared connections)
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) (6 shared connections)
- [index_documents_from_folder](index_documents_from_folder.md) (5 shared connections)
- [DocumentCleaner](DocumentCleaner.md) (1 shared connections)
- [datetime](datetime.md) (1 shared connections)
- [pydantic](pydantic.md) (1 shared connections)
- [ViolationType](ViolationType.md) (1 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/ingestion/__init__.py`
- `src/mcp_rag_agent/ingestion/models.py`
- `src/mcp_rag_agent/ingestion/parsers.py`

## Audit Trail

- EXTRACTED: 106 (90%)
- INFERRED: 12 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*