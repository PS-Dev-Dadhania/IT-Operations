---
source_file: "tests/unit_tests/test_observability.py"
type: "code"
community: "ObservabilityTracer"
location: "L386"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ObservabilityTracer
---

# .test_vector_search_records_telemetry_in_tracer()

## Connections
- [[MongoDBClient]] - `calls` [INFERRED]
- [[ObservabilityTracer]] - `calls` [INFERRED]
- [[TestMongoDBClientTelemetry]] - `method` [EXTRACTED]
- [[Verify vector search records database operation span in active tracer.]] - `rationale_for` [EXTRACTED]
- [[set_request_context()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/ObservabilityTracer