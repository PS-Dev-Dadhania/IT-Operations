---
type: community
cohesion: 0.13
members: 22
---

# QueryPreprocessor

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-build_keyword_query()]] - code - src/mcp_rag_agent/retrieval/preprocessor.py
- [[dot-normalize()]] - code - src/mcp_rag_agent/retrieval/preprocessor.py
- [[dot-preprocess()]] - code - src/mcp_rag_agent/retrieval/preprocessor.py
- [[dot-test_build_keyword_query_fixes_unbalanced_quotes()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_build_keyword_query_handles_leading_hyphen()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_normalize_strips_control_characters()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_normalize_translates_smart_quotes()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_normalize_unicode_nfkc_and_whitespace()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dot-test_preprocess_returns_all_variants()]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[Apply core normalization Unicode NFKC, control-char removal, and space…]] - rationale - src/mcp_rag_agent/retrieval/preprocessor.py
- [[Normalizes and prepares user queries for semantic vector search and keyword…]] - rationale - src/mcp_rag_agent/retrieval/preprocessor.py
- [[Preprocess a raw query into normalized, semantic, and keyword representations.…]] - rationale - src/mcp_rag_agent/retrieval/preprocessor.py
- [[Preprocessed query variants optimized for different search modalities.]] - rationale - src/mcp_rag_agent/retrieval/preprocessor.py
- [[PreprocessedQuery]] - code - src/mcp_rag_agent/retrieval/preprocessor.py
- [[Query preprocessing and normalization for hybrid retrieval.]] - rationale - src/mcp_rag_agent/retrieval/preprocessor.py
- [[QueryPreprocessor]] - code - src/mcp_rag_agent/retrieval/preprocessor.py
- [[Sanitize query for MongoDB text search ($text operator). Handles unbalanced…]] - rationale - src/mcp_rag_agent/retrieval/preprocessor.py
- [[Test suite for QueryPreprocessor.]] - rationale - tests/unit_tests/test_advanced_retrieval.py
- [[TestQueryPreprocessor]] - code - tests/unit_tests/test_advanced_retrieval.py
- [[dataclasses]] - concept
- [[preprocessor.py]] - code - src/mcp_rag_agent/retrieval/preprocessor.py
- [[unicodedata]] - concept

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/QueryPreprocessor
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_retrievalpipeline.py]]
- 2 edges to [[_COMMUNITY_AdvancedRetriever]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_ViolationType]]

## Top bridge nodes
- [[preprocessor.py]] - degree 9, connects to 3 communities
- [[QueryPreprocessor]] - degree 16, connects to 2 communities
- [[TestQueryPreprocessor]] - degree 9, connects to 1 community
- [[PreprocessedQuery]] - degree 4, connects to 1 community
- [[unicodedata]] - degree 2, connects to 1 community