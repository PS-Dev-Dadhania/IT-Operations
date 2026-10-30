---
source_file: "tests/unit_tests/security/test_security_regression.py"
type: "code"
community: "Role"
location: "L233"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Role
---

# test_cross_user_device_access_blocked()

## Connections
- [[DeviceRecord]] - `uses` [INFERRED]
- [[DeviceService]] - `uses` [INFERRED]
- [[Employee querying device assigned to another employee is DENIED.]] - `rationale_for` [EXTRACTED]
- [[GetDeviceInfoInput]] - `uses` [INFERRED]
- [[MemoryDeviceStore_3]] - `calls` [EXTRACTED]
- [[Role]] - `uses` [INFERRED]
- [[SecuritySubject]] - `uses` [INFERRED]
- [[asyncio]] - `references` [EXTRACTED]
- [[get_device_info_typed()]] - `calls` [INFERRED]
- [[set_device_service()]] - `calls` [INFERRED]
- [[test_security_regression.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Role