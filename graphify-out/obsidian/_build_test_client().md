---
source_file: "tests/unit_tests/it_support/test_ticket_api.py"
type: "code"
community: "test_admin_api.py"
location: "L57"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_admin_apipy
---

# _build_test_client()

## Connections
- [[Config]] - `uses` [INFERRED]
- [[ITTicketAPIService]] - `uses` [INFERRED]
- [[MemoryTicketStore_3]] - `calls` [EXTRACTED]
- [[TicketService]] - `uses` [INFERRED]
- [[create_app()]] - `calls` [INFERRED]
- [[test_ticket_api.py]] - `contains` [EXTRACTED]
- [[test_ticket_routes_disabled_when_feature_flag_off()]] - `calls` [EXTRACTED]
- [[test_ticket_routes_lifecycle_and_validation()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_admin_apipy