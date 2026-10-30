---
source_file: "tests/unit_tests/it_support/test_tickets.py"
type: "code"
community: "pytest"
location: "L165"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/pytest
---

# test_ticket_store_queries_and_not_found_handling()

## Connections
- [[TicketComment]] - `uses` [INFERRED]
- [[TicketNotFoundError]] - `uses` [INFERRED]
- [[TicketRecord]] - `uses` [INFERRED]
- [[TicketStore]] - `uses` [INFERRED]
- [[_request()]] - `calls` [EXTRACTED]
- [[pytest]] - `calls` [EXTRACTED]
- [[test_tickets.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/pytest