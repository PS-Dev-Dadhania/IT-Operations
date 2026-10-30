---
source_file: "tests/unit_tests/test_observability.py"
type: "code"
community: "ObservabilityTracer"
location: "L61"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ObservabilityTracer
---

# .test_set_request_context_sync()

## Connections
- [[TestCorrelationContext]] - `method` [EXTRACTED]
- [[Verify context manager sets and restores correlation IDs.]] - `rationale_for` [EXTRACTED]
- [[get_correlation_ids()]] - `calls` [INFERRED]
- [[get_request_id()]] - `calls` [INFERRED]
- [[get_thread_id()]] - `calls` [INFERRED]
- [[get_user_id()]] - `calls` [INFERRED]
- [[set_request_context()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/ObservabilityTracer