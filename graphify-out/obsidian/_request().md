---
source_file: "tests/unit_tests/it_support/test_tickets.py"
type: "code"
community: "pytest"
location: "L22"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/pytest
---

# _request()

## Connections
- [[ITCategory]] - `uses` [INFERRED]
- [[TicketCreate]] - `uses` [INFERRED]
- [[test_create_and_duplicate_detection()]] - `calls` [EXTRACTED]
- [[test_escalation_is_allowed_only_from_open_or_in_progress()]] - `calls` [EXTRACTED]
- [[test_invalid_lifecycle_transition_is_rejected()]] - `calls` [EXTRACTED]
- [[test_lifecycle_allows_only_deterministic_transitions()]] - `calls` [EXTRACTED]
- [[test_mongodb_failure_is_not_silenced()]] - `calls` [EXTRACTED]
- [[test_ticket_comments_and_service_methods()]] - `calls` [EXTRACTED]
- [[test_ticket_store_crud_uses_shared_mongodb_client()]] - `calls` [EXTRACTED]
- [[test_ticket_store_queries_and_not_found_handling()]] - `calls` [EXTRACTED]
- [[test_tickets.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/pytest