---
source_file: "scripts/seed_it_operations_data.py"
type: "code"
community: "ServiceStatusChecker"
location: "L199"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ServiceStatusChecker
---

# seed_it_operations_data()

## Connections
- [[DeviceStore]] - `uses` [INFERRED]
- [[Idempotently seed users, devices, and service statuses.]] - `rationale_for` [EXTRACTED]
- [[MongoDBClient]] - `uses` [INFERRED]
- [[ServiceStatusStore]] - `uses` [INFERRED]
- [[UserStore]] - `uses` [INFERRED]
- [[get_seed_devices()]] - `calls` [EXTRACTED]
- [[get_seed_service_statuses()]] - `calls` [EXTRACTED]
- [[get_seed_users()]] - `calls` [EXTRACTED]
- [[seed_it_operations_data.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ServiceStatusChecker