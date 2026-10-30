---
type: community
cohesion: 0.15
members: 27
---

# ParsedDocument

**Cohesion:** 0.15 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-_clean_title_from_filename()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-chunk_document()]] - code - src/mcp_rag_agent/ingestion/chunker.py
- [[dot-parse()]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-parse()_1]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-parse()_2]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-parse()_3]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-parse()_4]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[dot-test_chunker_preserves_section_and_page_metadata()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_chunker_splits_long_text_and_sets_indices()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[dot-test_invalid_parameters_raise_value_error()]] - code - tests/unit_tests/test_ingestion_pipeline.py
- [[A logical segment of a document (e.g., page, section, or paragraph).]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[BaseModel_15]] - code
- [[Chunks documents intelligently while preserving sectionpage structure and…]] - rationale - src/mcp_rag_agent/ingestion/chunker.py
- [[Derive a readable default title from the file stem.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[DocumentChunk]] - code - src/mcp_rag_agent/ingestion/models.py
- [[DocumentChunker]] - code - src/mcp_rag_agent/ingestion/chunker.py
- [[DocumentSegment]] - code - src/mcp_rag_agent/ingestion/models.py
- [[Parse file content and return structured ParsedDocument. Args file_path Path…]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[ParsedDocument]] - code - src/mcp_rag_agent/ingestion/models.py
- [[ParsingError]] - code - src/mcp_rag_agent/ingestion/parsers.py
- [[Path_2]] - code
- [[Raised when parsing fails due to corruption, encryption, or format issues.]] - rationale - src/mcp_rag_agent/ingestion/parsers.py
- [[Represents a document extracted by a parser before chunking.]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[Represents an individual text chunk ready for embedding and storage.]] - rationale - src/mcp_rag_agent/ingestion/models.py
- [[Split a parsed document into structured DocumentChunks. Args parsed_doc The…]] - rationale - src/mcp_rag_agent/ingestion/chunker.py
- [[Test suite for DocumentChunker.]] - rationale - tests/unit_tests/test_ingestion_pipeline.py
- [[TestDocumentChunker]] - code - tests/unit_tests/test_ingestion_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ParsedDocument
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_ingestion__init__.py]]
- 8 edges to [[_COMMUNITY_typing]]
- 8 edges to [[_COMMUNITY_test_ingestion_pipeline.py]]
- 4 edges to [[_COMMUNITY_MarkdownParser]]
- 2 edges to [[_COMMUNITY_index_documents_from_folder]]
- 2 edges to [[_COMMUNITY_DocumentCleaner]]
- 2 edges to [[_COMMUNITY_DocumentIngestionPipeline]]
- 1 edge to [[_COMMUNITY_dot-to_vector_document]]

## Top bridge nodes
- [[DocumentChunker]] - degree 18, connects to 5 communities
- [[ParsedDocument]] - degree 21, connects to 4 communities
- [[DocumentChunk]] - degree 10, connects to 4 communities
- [[DocumentSegment]] - degree 16, connects to 3 communities
- [[Path_2]] - degree 10, connects to 2 communities