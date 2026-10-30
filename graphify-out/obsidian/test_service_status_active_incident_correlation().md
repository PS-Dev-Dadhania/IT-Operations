---
source_file: "tests/unit_tests/it_support/test_services.py"
type: "code"
community: "MemoryIncidentStore"
location: "L96"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MemoryIncidentStore
---

# test_service_status_active_incident_correlation()

## Connections
- [[IncidentCreate]] - `uses` [INFERRED]
- [[IncidentService]] - `uses` [INFERRED]
- [[IncidentStatus]] - `uses` [INFERRED]
- [[MemoryIncidentStore_2]] - `calls` [EXTRACTED]
- [[Priority]] - `uses` [INFERRED]
- [[ServiceOperationalStatus]] - `uses` [INFERRED]
- [[ServiceStatusChecker]] - `uses` [INFERRED]
- [[test_services.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MemoryIncidentStore