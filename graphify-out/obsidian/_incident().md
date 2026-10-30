---
source_file: "tests/unit_tests/it_support/test_incidents.py"
type: "code"
community: "test_incidents.py"
location: "L15"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_incidentspy
---

# _incident()

## Connections
- [[ITCategory]] - `uses` [INFERRED]
- [[IncidentCreate]] - `uses` [INFERRED]
- [[Priority]] - `uses` [INFERRED]
- [[test_incident_create_retrieve_and_status_update()]] - `calls` [EXTRACTED]
- [[test_incident_resolve_sets_end_time()]] - `calls` [EXTRACTED]
- [[test_incident_service_find_known_case_insensitivity_and_partial_signals()]] - `calls` [EXTRACTED]
- [[test_incident_store_queries_and_not_found_handling()]] - `calls` [EXTRACTED]
- [[test_incident_store_uses_mongodb()]] - `calls` [EXTRACTED]
- [[test_incidents.py]] - `contains` [EXTRACTED]
- [[test_known_incident_detection_requires_structured_match()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_incidentspy