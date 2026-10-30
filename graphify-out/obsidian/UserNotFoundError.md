---
source_file: "src/mcp_rag_agent/it_support/users/store.py"
type: "code"
community: "UserNotFoundError"
location: "L16"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/UserNotFoundError
---

# UserNotFoundError

## Connections
- [[dot-_to_record()_4]] - `calls` [EXTRACTED]
- [[dot-get()_23]] - `calls` [EXTRACTED]
- [[dot-get()_16]] - `calls` [INFERRED]
- [[dot-get()_19]] - `calls` [INFERRED]
- [[dot-get()_17]] - `calls` [INFERRED]
- [[dot-update_fields()_9]] - `calls` [EXTRACTED]
- [[dot-update_fields()_6]] - `calls` [INFERRED]
- [[KeyError_4]] - `inherits` [EXTRACTED]
- [[MemoryUserStore]] - `uses` [INFERRED]
- [[MemoryUserStore_2]] - `uses` [INFERRED]
- [[MemoryUserStore_1]] - `uses` [INFERRED]
- [[Raised when a requested user cannot be found.]] - `rationale_for` [EXTRACTED]
- [[get_user_context_typed()]] - `uses` [INFERRED]
- [[mcp_rag_agentit_support__init__.py]] - `imports` [EXTRACTED]
- [[mcp_servertools.py]] - `imports` [EXTRACTED]
- [[test_user_service_missing_user_raises_not_found()]] - `uses` [INFERRED]
- [[test_user_store_mongodb_adapter()]] - `uses` [INFERRED]
- [[users__init__.py]] - `imports` [EXTRACTED]
- [[usersservice.py]] - `imports` [EXTRACTED]
- [[usersstore.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/UserNotFoundError