---
source_file: "tests/unit_tests/it_support/test_it_agent_flows.py"
type: "code"
community: "setup_services"
location: "L74"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/setup_services
---

# setup_services()

## Connections
- [[DeviceRecord]] - `uses` [INFERRED]
- [[DeviceService]] - `uses` [INFERRED]
- [[MemoryDeviceStore_1]] - `calls` [EXTRACTED]
- [[MemoryTicketStore_1]] - `calls` [EXTRACTED]
- [[MemoryUserStore]] - `calls` [EXTRACTED]
- [[ServiceStatusChecker]] - `uses` [INFERRED]
- [[SupportTier]] - `uses` [INFERRED]
- [[TicketService]] - `uses` [INFERRED]
- [[UserContextRecord]] - `uses` [INFERRED]
- [[UserService]] - `uses` [INFERRED]
- [[UserStatus]] - `uses` [INFERRED]
- [[fixture_7]] - `references` [EXTRACTED]
- [[reset_retriever()]] - `calls` [INFERRED]
- [[set_device_service()]] - `calls` [INFERRED]
- [[set_service_status_checker()]] - `calls` [INFERRED]
- [[set_ticket_service()]] - `calls` [INFERRED]
- [[set_user_service()]] - `calls` [INFERRED]
- [[test_it_agent_flows.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/setup_services