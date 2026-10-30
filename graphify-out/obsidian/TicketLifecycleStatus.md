---
source_file: "src/mcp_rag_agent/it_support/tickets/models.py"
type: "code"
community: "TicketService"
location: "L16"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TicketService
---

# TicketLifecycleStatus

## Connections
- [[dot-transition_status()]] - `references` [EXTRACTED]
- [[dot-update_status()_3]] - `references` [EXTRACTED]
- [[AdminAPIService]] - `uses` [INFERRED]
- [[Enum_9]] - `inherits` [EXTRACTED]
- [[MemoryTicketStore_2]] - `uses` [INFERRED]
- [[MemoryTicketStore_3]] - `uses` [INFERRED]
- [[MemoryTicketStore_4]] - `uses` [INFERRED]
- [[MemoryTicketStore_5]] - `uses` [INFERRED]
- [[TicketService]] - `uses` [INFERRED]
- [[TicketStore]] - `uses` [INFERRED]
- [[_get_default_seed_tickets()]] - `uses` [INFERRED]
- [[admin_service.py]] - `imports` [EXTRACTED]
- [[mcp_rag_agentit_support__init__.py]] - `imports` [EXTRACTED]
- [[mcp_servertools.py]] - `imports` [EXTRACTED]
- [[str_9]] - `inherits` [EXTRACTED]
- [[test_escalation_is_allowed_only_from_open_or_in_progress()]] - `uses` [INFERRED]
- [[test_invalid_lifecycle_transition_is_rejected()]] - `uses` [INFERRED]
- [[test_lifecycle_allows_only_deterministic_transitions()]] - `uses` [INFERRED]
- [[test_setup()]] - `uses` [INFERRED]
- [[tickets__init__.py]] - `imports` [EXTRACTED]
- [[ticketsmodels.py]] - `contains` [EXTRACTED]
- [[ticketsservice.py]] - `imports` [EXTRACTED]
- [[ticketsstore.py]] - `imports` [EXTRACTED]
- [[update_ticket_typed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TicketService