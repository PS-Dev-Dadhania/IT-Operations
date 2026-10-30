---
type: community
cohesion: 0.20
members: 11
---

# TestStructuredLoggingAndRedaction

**Cohesion:** 0.20 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-filter()_1]] - code - src/mcp_rag_agent/core/log_setup.py
- [[dot-test_json_log_formatter()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_mask_sensitive_patterns()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_masking_filter_on_log_records()]] - code - tests/unit_tests/test_observability.py
- [[Logging filter that ensures no secrets or credentials appear in log messages or…]] - rationale - src/mcp_rag_agent/core/log_setup.py
- [[MaskingFilter]] - code - src/mcp_rag_agent/core/log_setup.py
- [[Test secret redaction guarantees and JSONtext structured log formatting.]] - rationale - tests/unit_tests/test_observability.py
- [[TestStructuredLoggingAndRedaction]] - code - tests/unit_tests/test_observability.py
- [[Verify JSONLogFormatter emits valid JSON with expected telemetry fields.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify MaskingFilter scrubs secrets from record msg and args.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify all categories of credentials and sensitive data are redacted.]] - rationale - tests/unit_tests/test_observability.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestStructuredLoggingAndRedaction
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_test_observability.py]]
- 1 edge to [[_COMMUNITY_audit.py]]

## Top bridge nodes
- [[TestStructuredLoggingAndRedaction]] - degree 7, connects to 2 communities
- [[dot-filter()_1]] - degree 3, connects to 2 communities
- [[MaskingFilter]] - degree 6, connects to 1 community
- [[dot-test_json_log_formatter()]] - degree 3, connects to 1 community