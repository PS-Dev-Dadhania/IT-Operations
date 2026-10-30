---
type: community
cohesion: 0.33
members: 7
---

# .retrieve

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-_extract_chunk_identity()]] - code - src/mcp_rag_agent/retrieval/pipeline.py
- [[dot-retrieve()]] - code - src/mcp_rag_agent/retrieval/pipeline.py
- [[Any_37]] - code
- [[Execute hybrid search pipeline with candidate over-fetching, RRF fusion, and…]] - rationale - src/mcp_rag_agent/retrieval/pipeline.py
- [[Extract chunk_id, document_id, and document_name reliably from raw MongoDB…]] - rationale - src/mcp_rag_agent/retrieval/pipeline.py
- [[fetch_keyword_candidates()]] - code - src/mcp_rag_agent/retrieval/pipeline.py
- [[fetch_vector_candidates()]] - code - src/mcp_rag_agent/retrieval/pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/retrieve
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AdvancedRetriever]]
- 2 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 1 edge to [[_COMMUNITY_retrievalpipeline.py]]
- 1 edge to [[_COMMUNITY_RetrievedChunk]]

## Top bridge nodes
- [[dot-retrieve()]] - degree 10, connects to 4 communities
- [[dot-_extract_chunk_identity()]] - degree 4, connects to 1 community