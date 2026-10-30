# QueryPreprocessor

> 22 nodes · cohesion 0.13

## Key Concepts

- **QueryPreprocessor** (16 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **preprocessor.py** (9 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **TestQueryPreprocessor** (9 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.preprocess()** (5 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **PreprocessedQuery** (4 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **.build_keyword_query()** (3 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **.normalize()** (3 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **.test_build_keyword_query_fixes_unbalanced_quotes()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_build_keyword_query_handles_leading_hyphen()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_normalize_strips_control_characters()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_normalize_translates_smart_quotes()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_normalize_unicode_nfkc_and_whitespace()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **.test_preprocess_returns_all_variants()** (2 connections) — `tests/unit_tests/test_advanced_retrieval.py`
- **unicodedata** (2 connections)
- **dataclasses** (1 connections)
- **Query preprocessing and normalization for hybrid retrieval.** (1 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **Preprocess a raw query into normalized, semantic, and keyword representations.…** (1 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **Preprocessed query variants optimized for different search modalities.** (1 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **Normalizes and prepares user queries for semantic vector search and keyword…** (1 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **Apply core normalization: Unicode NFKC, control-char removal, and space…** (1 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **Sanitize query for MongoDB text search ($text operator). Handles unbalanced…** (1 connections) — `src/mcp_rag_agent/retrieval/preprocessor.py`
- **Test suite for QueryPreprocessor.** (1 connections) — `tests/unit_tests/test_advanced_retrieval.py`

## Relationships

- [retrieval/pipeline.py](retrieval-pipeline.py.md) (6 shared connections)
- [typing](typing.md) (2 shared connections)
- [AdvancedRetriever](AdvancedRetriever.md) (2 shared connections)
- [ViolationType](ViolationType.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/retrieval/preprocessor.py`
- `tests/unit_tests/test_advanced_retrieval.py`

## Audit Trail

- EXTRACTED: 33 (80%)
- INFERRED: 8 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*