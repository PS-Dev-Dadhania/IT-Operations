---
source_file: "tests/unit_tests/api/test_admin_api.py"
type: "code"
community: "IncidentRecord"
location: "L100"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/IncidentRecord
---

# test_setup()

## Connections
- [[AdminAPIService]] - `uses` [INFERRED]
- [[AuditEvent]] - `uses` [INFERRED]
- [[AuditService]] - `uses` [INFERRED]
- [[AuditStore]] - `uses` [INFERRED]
- [[Config]] - `uses` [INFERRED]
- [[ITCategory]] - `uses` [INFERRED]
- [[IncidentRecord]] - `uses` [INFERRED]
- [[IncidentService]] - `uses` [INFERRED]
- [[IncidentStatus]] - `uses` [INFERRED]
- [[MemoryIncidentStore]] - `calls` [EXTRACTED]
- [[MemoryTicketStore]] - `calls` [EXTRACTED]
- [[Priority]] - `uses` [INFERRED]
- [[RiskLevel]] - `uses` [INFERRED]
- [[Role]] - `uses` [INFERRED]
- [[TicketLifecycleStatus]] - `uses` [INFERRED]
- [[TicketRecord]] - `uses` [INFERRED]
- [[TicketService]] - `uses` [INFERRED]
- [[create_app()]] - `calls` [INFERRED]
- [[fixture_5]] - `references` [EXTRACTED]
- [[test_admin_api.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/IncidentRecord