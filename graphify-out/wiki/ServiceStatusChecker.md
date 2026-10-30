# ServiceStatusChecker

> 27 nodes · cohesion 0.10

## Key Concepts

- **ServiceStatusChecker** (23 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **ServiceOperationalStatus** (16 connections) — `src/mcp_rag_agent/it_support/services/models.py`
- **test_services.py** (16 connections) — `tests/unit_tests/it_support/test_services.py`
- **seed_it_operations_data()** (9 connections) — `scripts/seed_it_operations_data.py`
- **normalize_service_name()** (6 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **.check_service_status()** (6 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **.set_service_status()** (6 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **get_seed_service_statuses()** (4 connections) — `scripts/seed_it_operations_data.py`
- **.list_all_services()** (4 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **test_service_status_store_mongodb_adapter()** (4 connections) — `tests/unit_tests/it_support/test_services.py`
- **mcp_rag_agent_it_support_incidents_models** (3 connections)
- **mcp_rag_agent_it_support_incidents_service** (3 connections)
- **get_seed_devices()** (3 connections) — `scripts/seed_it_operations_data.py`
- **.__init__()** (3 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **test_service_status_invalid_input_raises_value_error()** (3 connections) — `tests/unit_tests/it_support/test_services.py`
- **test_service_status_known_services_and_aliases()** (3 connections) — `tests/unit_tests/it_support/test_services.py`
- **test_service_status_unknown_service()** (3 connections) — `tests/unit_tests/it_support/test_services.py`
- **Idempotently seed users, devices, and service statuses.** (1 connections) — `scripts/seed_it_operations_data.py`
- **str** (1 connections)
- **Operational status of a monitored synthetic enterprise service.** (1 connections) — `src/mcp_rag_agent/it_support/services/models.py`
- **Any** (1 connections)
- **Update or register status for a service in the store.** (1 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **List statuses for all stored or standard services.** (1 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **Normalize input service query into a canonical service key.** (1 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- **Domain service checking synthetic operational status of enterprise services.** (1 connections) — `src/mcp_rag_agent/it_support/services/service.py`
- *... and 2 more nodes in this community*

## Relationships

- [ServiceStatusRecord](ServiceStatusRecord.md) (22 shared connections)
- [test_mcp_it_tools.py](test_mcp_it_tools.py.md) (6 shared connections)
- [IncidentRecord](IncidentRecord.md) (5 shared connections)
- [MemoryIncidentStore](MemoryIncidentStore.md) (4 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (3 shared connections)
- [test_incidents.py](test_incidents.py.md) (2 shared connections)
- [DeviceRecord](DeviceRecord.md) (2 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (2 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [setup_services](setup_services.md) (2 shared connections)
- [pytest](pytest.md) (2 shared connections)
- [users/store.py](users-store.py.md) (1 shared connections)

## Source Files

- `scripts/seed_it_operations_data.py`
- `src/mcp_rag_agent/it_support/services/models.py`
- `src/mcp_rag_agent/it_support/services/service.py`
- `tests/unit_tests/it_support/test_services.py`

## Audit Trail

- EXTRACTED: 64 (70%)
- INFERRED: 27 (30%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*