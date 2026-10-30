---
source_file: "src/mcp_rag_agent/api/routes/health.py"
type: "code"
community: "datetime"
location: "L35"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/datetime
---

# readiness_check()

## Connections
- [[Config]] - `uses` [INFERRED]
- [[Deep readiness probe verifying database connectivity and model configuration.]] - `rationale_for` [EXTRACTED]
- [[ReadinessDetails]] - `uses` [INFERRED]
- [[ReadinessResponse]] - `uses` [INFERRED]
- [[Response_1]] - `references` [EXTRACTED]
- [[_ping_mongo()]] - `indirect_call` [INFERRED]
- [[asyncio_19]] - `calls` [EXTRACTED]
- [[get()]] - `references` [EXTRACTED]
- [[routeshealth.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/datetime