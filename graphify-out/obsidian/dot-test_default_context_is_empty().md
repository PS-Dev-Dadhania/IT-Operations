---
source_file: "tests/unit_tests/test_observability.py"
type: "code"
community: "ObservabilityTracer"
location: "L54"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ObservabilityTracer
---

# .test_default_context_is_empty()

## Connections
- [[TestCorrelationContext]] - `method` [EXTRACTED]
- [[Verify default context getters return empty strings or None.]] - `rationale_for` [EXTRACTED]
- [[get_current_tracer()]] - `calls` [INFERRED]
- [[get_request_id()]] - `calls` [INFERRED]
- [[get_thread_id()]] - `calls` [INFERRED]
- [[get_user_id()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/ObservabilityTracer