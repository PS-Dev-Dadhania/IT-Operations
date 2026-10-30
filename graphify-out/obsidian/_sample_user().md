---
source_file: "tests/unit_tests/it_support/test_users.py"
type: "code"
community: "UserNotFoundError"
location: "L16"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/UserNotFoundError
---

# _sample_user()

## Connections
- [[SupportTier]] - `uses` [INFERRED]
- [[UserContextRecord]] - `uses` [INFERRED]
- [[UserStatus]] - `uses` [INFERRED]
- [[test_user_model_instantiation_and_validation()]] - `calls` [EXTRACTED]
- [[test_user_service_valid_lookup()]] - `calls` [EXTRACTED]
- [[test_user_store_mongodb_adapter()]] - `calls` [EXTRACTED]
- [[test_users.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/UserNotFoundError