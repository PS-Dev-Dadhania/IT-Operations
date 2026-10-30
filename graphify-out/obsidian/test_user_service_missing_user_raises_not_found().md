---
source_file: "tests/unit_tests/it_support/test_users.py"
type: "code"
community: "UserNotFoundError"
location: "L81"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/UserNotFoundError
---

# test_user_service_missing_user_raises_not_found()

## Connections
- [[MemoryUserStore_1]] - `calls` [EXTRACTED]
- [[UserNotFoundError]] - `uses` [INFERRED]
- [[UserService]] - `uses` [INFERRED]
- [[pytest]] - `calls` [EXTRACTED]
- [[test_users.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/UserNotFoundError