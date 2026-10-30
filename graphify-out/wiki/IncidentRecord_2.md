# IncidentRecord

> God node · 44 connections · `src/mcp_rag_agent/it_support/incidents/models.py`

**Community:** [IncidentRecord](IncidentRecord.md)

## Connections by Relation

### calls
- _get_default_seed_incidents() `EXTRACTED`

### contains
- incidents/models.py `EXTRACTED`

### imports
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) `EXTRACTED`
- admin.py `EXTRACTED`
- admin_service.py `EXTRACTED`
- incidents/store.py `EXTRACTED`
- incidents/service.py `EXTRACTED`
- incidents/__init__.py `EXTRACTED`

### inherits
- IncidentCreate `EXTRACTED`

### references
- ._to_record() `EXTRACTED`
- .find_matching() `EXTRACTED`
- .get() `EXTRACTED`
- .update_status() `EXTRACTED`
- .find_known_incident() `EXTRACTED`
- .list_incidents() `EXTRACTED`
- .list_active() `EXTRACTED`
- .list_all() `EXTRACTED`
- .create_incident() `EXTRACTED`
- .update_status() `EXTRACTED`
- .create() `EXTRACTED`
- .update_status() `EXTRACTED`
- .list_active_incidents() `EXTRACTED`
- .list_all_incidents() `EXTRACTED`
- .list_active() `EXTRACTED`
- .list_all() `EXTRACTED`
- .get_incident() `EXTRACTED`
- .create() `EXTRACTED`
- .get() `EXTRACTED`
- .create() `EXTRACTED`
- *…and 3 more `references` connection(s) not listed (lowest-degree first to go)*

### uses
- IncidentService `INFERRED`
- [AdminAPIService](AdminAPIService.md) `INFERRED`
- IncidentStatus `INFERRED`
- [IncidentStore](IncidentStore.md) `INFERRED`
- test_setup() `INFERRED`
- [MemoryIncidentStore](MemoryIncidentStore.md) `INFERRED`
- [MemoryIncidentStore](MemoryIncidentStore.md) `INFERRED`
- [MemoryIncidentStore](MemoryIncidentStore.md) `INFERRED`
- list_admin_incidents() `INFERRED`
- test_incident_store_queries_and_not_found_handling() `INFERRED`
- test_incident_resolve_sets_end_time() `INFERRED`
- test_incident_store_uses_mongodb() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*