---
source_file: "src/mcp_rag_agent/it_support/incidents/models.py"
type: "code"
community: "IncidentRecord"
location: "L37"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/IncidentRecord
---

# IncidentMatchCriteria

## Connections
- [[dot-check_service_status()]] - `calls` [EXTRACTED]
- [[dot-find_known_incident()]] - `references` [EXTRACTED]
- [[dot-find_matching()_1]] - `references` [EXTRACTED]
- [[BaseModel_9]] - `inherits` [EXTRACTED]
- [[ITCategory]] - `uses` [INFERRED]
- [[IncidentService]] - `uses` [INFERRED]
- [[IncidentStore]] - `uses` [INFERRED]
- [[ServiceStatusChecker]] - `uses` [INFERRED]
- [[incidents__init__.py]] - `imports` [EXTRACTED]
- [[incidentsmodels.py]] - `contains` [EXTRACTED]
- [[incidentsservice.py]] - `imports` [EXTRACTED]
- [[incidentsstore.py]] - `imports` [EXTRACTED]
- [[mcp_rag_agentit_support__init__.py]] - `imports` [EXTRACTED]
- [[servicesservice.py]] - `imports` [EXTRACTED]
- [[test_incident_service_find_known_case_insensitivity_and_partial_signals()]] - `uses` [INFERRED]
- [[test_incident_store_queries_and_not_found_handling()]] - `uses` [INFERRED]
- [[test_known_incident_detection_requires_structured_match()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/IncidentRecord