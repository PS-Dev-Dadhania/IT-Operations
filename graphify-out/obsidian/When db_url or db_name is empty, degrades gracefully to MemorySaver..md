---
source_file: "tests/unit_tests/test_session_memory.py"
type: "rationale"
community: "get_checkpointer"
location: "L34"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/get_checkpointer
---

# When db_url or db_name is empty, degrades gracefully to MemorySaver.

## Connections
- [[dot-test_missing_database_url_degrades_to_memory()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/get_checkpointer