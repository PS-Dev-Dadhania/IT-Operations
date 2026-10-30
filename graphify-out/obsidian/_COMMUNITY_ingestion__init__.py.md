---
type: community
cohesion: 0.10
members: 31
---

# ingestion/__init__.py

**Cohesion:** 0.10 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-can_handle()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-get_parser()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-supported_extensions()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-supported_extensions()_1]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[ABC]] - code
- [[Abstract base class for format-specific document parsers.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Base exception for ingestion errors.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[BaseDocumentParser]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Check if this parser can handle the given file.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Convenience function to get a parser from the default registry.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Data models for document ingestion and chunking.]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[Document Ingestion Subsystem for MCP RAG Agent. Provides production-grade…]] - rationale - src/mcp_rag_agent/ingestion/__init__.py
- [[Document parsers for TXT, Markdown, PDF, and DOCX formats.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[DocxParser]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Enum_4]] - code
- [[Exception_1]] - code
- [[Get the appropriate parser for a given file path. Args file_path File path to…]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[IngestionError]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[IngestionResult]] - code - src/mcp_rag_agent/ingestion/models.py
- [[IngestionStatus]] - code - src/mcp_rag_agent/ingestion/models.py
- [[Parser for Microsoft Word (.docx) documents with heading & paragraph awareness.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Raised when an unsupported file extension is encountered.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Result summary for a single document ingestion.]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[Return the set of supported file extensions (lowercase, with dot).]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Status outcomes for document ingestion.]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[UnsupportedFileTypeError]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[get_parser()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[ingestion__init__.py]] - code - src/mcp_rag_agent/ingestion/__init__.py
- [[ingestionmodels.py]] - code - src/mcp_rag_agent/ingestion/models.py
- [[parsers.py]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[str_3]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ingestion/__init__py
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_ParsedDocument]]
- 16 edges to [[_COMMUNITY_typing]]
- 9 edges to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 8 edges to [[_COMMUNITY_MarkdownParser]]
- 6 edges to [[_COMMUNITY_DocumentIngestionPipeline]]
- 5 edges to [[_COMMUNITY_index_documents_from_folder]]
- 1 edge to [[_COMMUNITY_DocumentCleaner]]
- 1 edge to [[_COMMUNITY_datetime]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]

## Top bridge nodes
- [[ingestion__init__.py]] - degree 25, connects to 7 communities
- [[parsers.py]] - degree 22, connects to 6 communities
- [[ingestionmodels.py]] - degree 16, connects to 5 communities
- [[IngestionResult]] - degree 9, connects to 4 communities
- [[BaseDocumentParser]] - degree 16, connects to 3 communities