---
type: community
cohesion: 0.05
members: 76
---

# DeviceRecord

**Cohesion:** 0.05 - loosely connected
**Members:** 76 nodes

## Members
- [[dot-__init__()_21]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[dot-__init__()_22]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-__init__()_23]] - code - tests/unit_tests/it_support/test_devices.py
- [[dot-__init__()_24]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-__init__()_25]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-__init__()_26]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-_collection()_2]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-_to_record()_1]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-create()_9]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-create()_10]] - code - tests/unit_tests/it_support/test_devices.py
- [[dot-create()_11]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-create_device()]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[dot-get()_11]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-get()_12]] - code - tests/unit_tests/it_support/test_devices.py
- [[dot-get()_13]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-get()_14]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-get()_15]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-get_by_user()]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-get_by_user()_1]] - code - tests/unit_tests/it_support/test_devices.py
- [[dot-get_by_user()_2]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[dot-get_by_user()_3]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[dot-get_by_user()_4]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-get_device_info()]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[dot-get_user_devices()]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[dot-list()_4]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-list()_5]] - code - tests/unit_tests/it_support/test_devices.py
- [[dot-list()_6]] - code - tests/unit_tests/security/test_security_regression.py
- [[dot-list_devices()]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[dot-update_fields()_5]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-upsert()_2]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[dot-upsert()_3]] - code - tests/unit_tests/it_support/test_devices.py
- [[dot-upsert_device()]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[Any_11]] - code
- [[Any_12]] - code
- [[BaseModel_12]] - code
- [[Device domain models and typed schemas for IT support operations.]] - rationale - src/mcp_rag_agent/it_support/devices/models.py
- [[Device domain service for fetching and managing device context.]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[DeviceNotFoundError]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[DeviceRecord]] - code - src/mcp_rag_agent/it_support/devices/models.py
- [[DeviceService]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[DeviceStore]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[Domain service managing device info lookups and management.]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[In-memory device store double for regression tests.]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[In-memory test double for DeviceStore.]] - rationale - tests/unit_tests/it_support/test_devices.py
- [[KeyError_3]] - code
- [[List devices matching optional filter criteria.]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[MemoryDeviceStore]] - code - tests/unit_tests/it_support/test_devices.py
- [[MemoryDeviceStore_1]] - code - tests/unit_tests/it_support/test_it_agent_flows.py
- [[MemoryDeviceStore_2]] - code - tests/unit_tests/it_support/test_mcp_it_tools.py
- [[MemoryDeviceStore_3]] - code - tests/unit_tests/security/test_security_regression.py
- [[MongoDB persistence adapter for devices with in-memory fallback support.]] - rationale - src/mcp_rag_agent/it_support/devices/store.py
- [[Persistence store for enterprise devices with in-memory fallback.]] - rationale - src/mcp_rag_agent/it_support/devices/store.py
- [[Public device context exports for IT support operations.]] - rationale - src/mcp_rag_agent/it_support/devices/__init__.py
- [[Pydantic model representing an enterprise device.]] - rationale - src/mcp_rag_agent/it_support/devices/models.py
- [[Raised when a requested device cannot be found.]] - rationale - src/mcp_rag_agent/it_support/devices/store.py
- [[Register a new device.]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[Retrieve all devices registered to a specific user. Args user_id Unique…]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[Retrieve device info by device_id. Args device_id Unique identifier for the…]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[Unit tests for device context models, store, and domain service.]] - rationale - tests/unit_tests/it_support/test_devices.py
- [[Upsert a device record (idempotent seeding).]] - rationale - src/mcp_rag_agent/it_support/devices/service.py
- [[_get_default_seed_devices()]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[_sample_device()]] - code - tests/unit_tests/it_support/test_devices.py
- [[_utc_now()_5]] - code - src/mcp_rag_agent/it_support/devices/models.py
- [[datetime_5]] - code
- [[devices__init__.py]] - code - src/mcp_rag_agent/it_support/devices/__init__.py
- [[devicesmodels.py]] - code - src/mcp_rag_agent/it_support/devices/models.py
- [[devicesservice.py]] - code - src/mcp_rag_agent/it_support/devices/service.py
- [[devicesstore.py]] - code - src/mcp_rag_agent/it_support/devices/store.py
- [[mcp_rag_agent_it_support_devices_service]] - concept
- [[test_device_model_instantiation_and_validation()]] - code - tests/unit_tests/it_support/test_devices.py
- [[test_device_service_invalid_id_raises_value_error()]] - code - tests/unit_tests/it_support/test_devices.py
- [[test_device_service_lookup_by_device_id()]] - code - tests/unit_tests/it_support/test_devices.py
- [[test_device_service_lookup_by_user_id()]] - code - tests/unit_tests/it_support/test_devices.py
- [[test_device_service_missing_device_raises_not_found()]] - code - tests/unit_tests/it_support/test_devices.py
- [[test_device_store_mongodb_adapter()]] - code - tests/unit_tests/it_support/test_devices.py
- [[test_devices.py]] - code - tests/unit_tests/it_support/test_devices.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DeviceRecord
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_setup_services]]
- 6 edges to [[_COMMUNITY_mcp_servertools.py]]
- 6 edges to [[_COMMUNITY_test_mcp_it_tools.py]]
- 5 edges to [[_COMMUNITY_typing]]
- 5 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 4 edges to [[_COMMUNITY_pytest]]
- 3 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_ServiceStatusChecker]]
- 2 edges to [[_COMMUNITY_test_admin_api.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_datetime]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[DeviceRecord]] - degree 43, connects to 4 communities
- [[DeviceService]] - degree 21, connects to 4 communities
- [[DeviceStore]] - degree 21, connects to 3 communities
- [[test_devices.py]] - degree 14, connects to 3 communities
- [[devicesstore.py]] - degree 12, connects to 3 communities