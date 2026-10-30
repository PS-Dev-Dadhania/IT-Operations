---
type: community
cohesion: 0.09
members: 26
---

# test_ingestion_pipeline.py

**Cohesion:** 0.09 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-supported_extensions()_2]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-supported_extensions()_3]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-test_corrupt_pdf_raises_parsing_error()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_docx_parser_headings_and_paragraphs()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_pdf_parser_multipage_and_pages()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_text_parser_success()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_unsupported_file_type_raises_error()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[Comprehensive unit tests for production-grade document ingestion pipeline.…]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[PDFParser]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Parser for PDF (.pdf) documents with page number tracking.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Parser for plain text (.txt) files.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Test suite for format-specific parsers.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[TestDocumentParsers]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[TextParser]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Verify DOCX parser parses paragraphs and captures heading sections.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify PDF parser extracts per-page text and assigns page numbers.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify corrupt PDF raises ParsingError.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify plain text parsing and title extraction.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[Verify unsupported extensions raise UnsupportedFileTypeError.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[io]] - concept
- [[mcp_rag_agent_ingestion_chunker]] - concept
- [[mcp_rag_agent_ingestion_cleaner]] - concept
- [[mcp_rag_agent_ingestion_models]] - concept
- [[mcp_rag_agent_ingestion_parsers]] - concept
- [[mcp_rag_agent_ingestion_pipeline]] - concept
- [[test_ingestion_pipeline.py]] - code - tests/unit_tests/test_ingestion_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_ingestion_pipelinepy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ingestion__init__.py]]
- 8 edges to [[_COMMUNITY_ParsedDocument]]
- 4 edges to [[_COMMUNITY_MarkdownParser]]
- 2 edges to [[_COMMUNITY_DocumentIngestionPipeline]]
- 1 edge to [[_COMMUNITY_DocumentCleaner]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_test_evaluation_framework.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[test_ingestion_pipeline.py]] - degree 15, connects to 6 communities
- [[TestDocumentParsers]] - degree 14, connects to 3 communities
- [[PDFParser]] - degree 12, connects to 3 communities
- [[TextParser]] - degree 11, connects to 3 communities
- [[dot-test_docx_parser_headings_and_paragraphs()]] - degree 3, connects to 1 community