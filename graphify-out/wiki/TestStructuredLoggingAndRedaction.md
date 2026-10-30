# TestStructuredLoggingAndRedaction

> 11 nodes · cohesion 0.20

## Key Concepts

- **TestStructuredLoggingAndRedaction** (7 connections) — `tests/unit_tests/test_observability.py`
- **MaskingFilter** (6 connections) — `src/mcp_rag_agent/core/log_setup.py`
- **.filter()** (3 connections) — `src/mcp_rag_agent/core/log_setup.py`
- **.test_json_log_formatter()** (3 connections) — `tests/unit_tests/test_observability.py`
- **.test_masking_filter_on_log_records()** (3 connections) — `tests/unit_tests/test_observability.py`
- **.test_mask_sensitive_patterns()** (2 connections) — `tests/unit_tests/test_observability.py`
- **Logging filter that ensures no secrets or credentials appear in log messages or…** (1 connections) — `src/mcp_rag_agent/core/log_setup.py`
- **Test secret redaction guarantees and JSON/text structured log formatting.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify all categories of credentials and sensitive data are redacted.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify JSONLogFormatter emits valid JSON with expected telemetry fields.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify MaskingFilter scrubs secrets from record msg and args.** (1 connections) — `tests/unit_tests/test_observability.py`

## Relationships

- [typing](typing.md) (5 shared connections)
- [audit.py](audit.py.md) (1 shared connections)
- [test_observability.py](test_observability.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/core/log_setup.py`
- `tests/unit_tests/test_observability.py`

## Audit Trail

- EXTRACTED: 14 (78%)
- INFERRED: 4 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*