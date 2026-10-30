# pytest

> 13 nodes · cohesion 0.28

## Key Concepts

- **pytest** (55 connections)
- **test_tickets.py** (17 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **_request()** (11 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_invalid_lifecycle_transition_is_rejected()** (7 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_ticket_store_queries_and_not_found_handling()** (7 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_escalation_is_allowed_only_from_open_or_in_progress()** (5 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_lifecycle_allows_only_deterministic_transitions()** (5 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_mongodb_failure_is_not_silenced()** (5 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_create_and_duplicate_detection()** (4 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_ticket_store_crud_uses_shared_mongodb_client()** (4 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **test_unauthorized_role_cannot_approve()** (3 connections) — `tests/unit_tests/security/test_approval.py`
- **Ticket store and lifecycle tests with mocked MongoDB.** (1 connections) — `tests/unit_tests/it_support/test_tickets.py`
- **IT Support / Employee roles lack APPROVE_HIGH_RISK_ACTION permission.** (1 connections) — `tests/unit_tests/security/test_approval.py`

## Relationships

- [TicketRecord](TicketRecord.md) (11 shared connections)
- [unittest_mock](unittest_mock.md) (9 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (7 shared connections)
- [TicketService](TicketService.md) (7 shared connections)
- [test_approval.py](test_approval.py.md) (5 shared connections)
- [DeviceRecord](DeviceRecord.md) (4 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (4 shared connections)
- [UserNotFoundError](UserNotFoundError.md) (4 shared connections)
- [tickets/models.py](tickets-models.py.md) (3 shared connections)
- [TicketStore](TicketStore.md) (3 shared connections)
- [test_it_evaluation.py](test_it_evaluation.py.md) (2 shared connections)
- [ServiceStatusChecker](ServiceStatusChecker.md) (2 shared connections)

## Source Files

- `tests/unit_tests/it_support/test_tickets.py`
- `tests/unit_tests/security/test_approval.py`

## Audit Trail

- EXTRACTED: 85 (83%)
- INFERRED: 18 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*