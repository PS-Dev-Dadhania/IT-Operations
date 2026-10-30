---
source_file: "tests/unit_tests/test_observability.py"
type: "code"
community: "ObservabilityTracer"
location: "L363"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ObservabilityTracer
---

# .test_connect_records_database_error_on_failure()

## Connections
- [[dot-patch()]] - `calls` [INFERRED]
- [[MongoDBClient]] - `calls` [INFERRED]
- [[ObservabilityTracer]] - `calls` [INFERRED]
- [[TestMongoDBClientTelemetry]] - `method` [EXTRACTED]
- [[Verify connection failures record ErrorCategory.DATABASE_ERROR in active tracer.]] - `rationale_for` [EXTRACTED]
- [[set_request_context()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/ObservabilityTracer