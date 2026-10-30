---
source_file: "src/mcp_rag_agent/observability/models.py"
type: "code"
community: "ObservabilityTracer"
location: "L23"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ObservabilityTracer
---

# ErrorRecord

## Connections
- [[dot-async_span()]] - `calls` [EXTRACTED]
- [[dot-record_error()]] - `references` [EXTRACTED]
- [[dot-span()]] - `calls` [EXTRACTED]
- [[dot-test_error_record_creation_and_serialization()]] - `calls` [INFERRED]
- [[AgentExecutionMetadata]] - `uses` [INFERRED]
- [[BaseModel_6]] - `inherits` [EXTRACTED]
- [[Detailed record of an error or guardrail trigger occurring during execution.]] - `rationale_for` [EXTRACTED]
- [[ObservabilityTracer]] - `uses` [INFERRED]
- [[agentmodels.py]] - `imports` [EXTRACTED]
- [[observability__init__.py]] - `imports` [EXTRACTED]
- [[observabilitymodels.py]] - `contains` [EXTRACTED]
- [[tracer.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ObservabilityTracer