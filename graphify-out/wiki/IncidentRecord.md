# IncidentRecord

> 34 nodes · cohesion 0.13

## Key Concepts

- **IncidentRecord** (44 connections) — `src/mcp_rag_agent/it_support/incidents/models.py`
- **IncidentService** (30 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **IncidentStatus** (27 connections) — `src/mcp_rag_agent/it_support/models.py`
- **test_setup()** (20 connections) — `tests/unit_tests/api/test_admin_api.py`
- **incidents/models.py** (18 connections) — `src/mcp_rag_agent/it_support/incidents/models.py`
- **IncidentMatchCriteria** (17 connections) — `src/mcp_rag_agent/it_support/incidents/models.py`
- **incidents/store.py** (17 connections) — `src/mcp_rag_agent/it_support/incidents/store.py`
- **incidents/service.py** (14 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **incidents/__init__.py** (11 connections) — `src/mcp_rag_agent/it_support/incidents/__init__.py`
- **IncidentCreate** (11 connections) — `src/mcp_rag_agent/it_support/incidents/models.py`
- **MemoryIncidentStore** (9 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.find_known_incident()** (5 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **_get_default_seed_incidents()** (5 connections) — `src/mcp_rag_agent/it_support/incidents/store.py`
- **.create_incident()** (3 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **.update_status()** (3 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **.update_status()** (3 connections) — `tests/unit_tests/it_support/test_incidents.py`
- **BaseModel** (2 connections)
- **datetime** (2 connections)
- **_utc_now()** (2 connections) — `src/mcp_rag_agent/it_support/incidents/models.py`
- **.get_incident()** (2 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **.list_active_incidents()** (2 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **.list_all_incidents()** (2 connections) — `src/mcp_rag_agent/it_support/incidents/service.py`
- **.create()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.get()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- **.list_active()** (2 connections) — `tests/unit_tests/api/test_admin_api.py`
- *... and 9 more nodes in this community*

## Relationships

- [IncidentStore](IncidentStore.md) (20 shared connections)
- [test_incidents.py](test_incidents.py.md) (18 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (17 shared connections)
- [dependencies.py](dependencies.py.md) (12 shared connections)
- [MemoryIncidentStore](MemoryIncidentStore.md) (7 shared connections)
- [AdminAPIService](AdminAPIService.md) (7 shared connections)
- [ServiceStatusRecord](ServiceStatusRecord.md) (5 shared connections)
- [ServiceStatusChecker](ServiceStatusChecker.md) (5 shared connections)
- [ITCategory](ITCategory.md) (4 shared connections)
- [audit.py](audit.py.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [typing](typing.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/incidents/__init__.py`
- `src/mcp_rag_agent/it_support/incidents/models.py`
- `src/mcp_rag_agent/it_support/incidents/service.py`
- `src/mcp_rag_agent/it_support/incidents/store.py`
- `src/mcp_rag_agent/it_support/models.py`
- `tests/unit_tests/api/test_admin_api.py`
- `tests/unit_tests/it_support/test_incidents.py`

## Audit Trail

- EXTRACTED: 130 (68%)
- INFERRED: 60 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*