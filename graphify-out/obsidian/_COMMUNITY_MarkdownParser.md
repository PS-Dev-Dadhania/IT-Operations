---
type: community
cohesion: 0.17
members: 12
---

# MarkdownParser

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-__init__()_53]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-is_supported()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-register_parser()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-supported_extensions()_4]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-test_markdown_parser_headings_and_sections()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[Check if a file format is supported.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[MarkdownParser]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Parser for Markdown (.md, .markdown) files with heading awareness.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[ParserRegistry]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Register a custom document parser.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Registry managing available document parsers.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Verify markdown parser extracts title and partitions by headings.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MarkdownParser
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ingestion__init__.py]]
- 4 edges to [[_COMMUNITY_ParsedDocument]]
- 4 edges to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_DocumentIngestionPipeline]]

## Top bridge nodes
- [[MarkdownParser]] - degree 11, connects to 3 communities
- [[ParserRegistry]] - degree 10, connects to 3 communities
- [[dot-__init__()_53]] - degree 5, connects to 2 communities
- [[dot-is_supported()]] - degree 3, connects to 1 community
- [[dot-register_parser()]] - degree 3, connects to 1 community