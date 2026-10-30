---
source_file: "src/mcp_rag_agent/core/checkpointer.py"
type: "code"
community: "get_checkpointer"
location: "L18"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/get_checkpointer
---

# get_checkpointer()

## Connections
- [[dot-__init__()_37]] - `calls` [EXTRACTED]
- [[dot-test_checkpointer_initialization_with_mongodb()]] - `calls` [INFERRED]
- [[dot-test_connection_failure_gracefully_degrades_to_memory()]] - `calls` [INFERRED]
- [[dot-test_feature_flag_disabled_returns_none()]] - `calls` [INFERRED]
- [[dot-test_missing_database_url_degrades_to_memory()]] - `calls` [INFERRED]
- [[dot-test_missing_database_url_returns_none_if_no_fallback()]] - `calls` [INFERRED]
- [[BaseCheckpointSaver]] - `references` [EXTRACTED]
- [[Config]] - `uses` [INFERRED]
- [[Factory to construct a conversation checkpointer according to configuration. -…]] - `rationale_for` [EXTRACTED]
- [[checkpointer.py]] - `contains` [EXTRACTED]
- [[executor.py]] - `imports` [EXTRACTED]
- [[get_checkpointer_async()]] - `indirect_call` [INFERRED]
- [[mask_sensitive()_1]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/get_checkpointer