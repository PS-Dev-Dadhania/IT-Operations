---
source_file: "tests/unit_tests/it_support/test_mcp_it_tools.py"
type: "code"
community: "setup_services"
location: "L128"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/setup_services
---

# setup_services()

## Connections
- [[DeviceRecord]] - `uses` [INFERRED]
- [[DeviceService]] - `uses` [INFERRED]
- [[MemoryDeviceStore_2]] - `calls` [EXTRACTED]
- [[MemoryTicketStore_2]] - `calls` [EXTRACTED]
- [[MemoryUserStore_2]] - `calls` [EXTRACTED]
- [[ServiceStatusChecker]] - `uses` [INFERRED]
- [[SupportTier]] - `uses` [INFERRED]
- [[TicketService]] - `uses` [INFERRED]
- [[UserContextRecord]] - `uses` [INFERRED]
- [[UserService]] - `uses` [INFERRED]
- [[UserStatus]] - `uses` [INFERRED]
- [[fixture_8]] - `references` [EXTRACTED]
- [[reset_retriever()]] - `calls` [INFERRED]
- [[set_device_service()]] - `calls` [INFERRED]
- [[set_service_status_checker()]] - `calls` [INFERRED]
- [[set_ticket_service()]] - `calls` [INFERRED]
- [[set_user_service()]] - `calls` [INFERRED]
- [[test_mcp_it_tools.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/setup_services