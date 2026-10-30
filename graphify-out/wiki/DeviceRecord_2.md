# DeviceRecord

> God node · 43 connections · `src/mcp_rag_agent/it_support/devices/models.py`

**Community:** [DeviceRecord](DeviceRecord.md)

## Connections by Relation

### calls
- _get_default_seed_devices() `EXTRACTED`

### contains
- devices/models.py `EXTRACTED`

### imports
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) `EXTRACTED`
- devices/store.py `EXTRACTED`
- devices/__init__.py `EXTRACTED`
- devices/service.py `EXTRACTED`

### inherits
- BaseModel `EXTRACTED`

### rationale_for
- Pydantic model representing an enterprise device. `EXTRACTED`

### references
- ._to_record() `EXTRACTED`
- .get() `EXTRACTED`
- .update_fields() `EXTRACTED`
- .list() `EXTRACTED`
- .list_devices() `EXTRACTED`
- .get_by_user() `EXTRACTED`
- .get_user_devices() `EXTRACTED`
- .create_device() `EXTRACTED`
- .get_device_info() `EXTRACTED`
- .upsert_device() `EXTRACTED`
- .create() `EXTRACTED`
- .upsert() `EXTRACTED`
- .get() `EXTRACTED`
- .get() `EXTRACTED`
- .get() `EXTRACTED`
- .get_by_user() `EXTRACTED`
- .get_by_user() `EXTRACTED`
- .get_by_user() `EXTRACTED`
- .get_by_user() `EXTRACTED`
- .create() `EXTRACTED`
- *…and 3 more `references` connection(s) not listed (lowest-degree first to go)*

### uses
- DeviceService `INFERRED`
- DeviceStore `INFERRED`
- setup_services() `INFERRED`
- setup_services() `INFERRED`
- MemoryDeviceStore `INFERRED`
- test_cross_user_device_access_blocked() `INFERRED`
- MemoryDeviceStore `INFERRED`
- MemoryDeviceStore `INFERRED`
- MemoryDeviceStore `INFERRED`
- _sample_device() `INFERRED`
- test_device_service_lookup_by_user_id() `INFERRED`
- get_seed_devices() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*