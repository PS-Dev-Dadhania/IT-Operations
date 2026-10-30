---
source_file: "tests/unit_tests/test_session_memory.py"
type: "code"
community: "get_checkpointer"
location: "L33"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/get_checkpointer
---

# .test_missing_database_url_degrades_to_memory()

## Connections
- [[Config]] - `calls` [INFERRED]
- [[TestSessionMemoryCheckpointer]] - `method` [EXTRACTED]
- [[When db_url or db_name is empty, degrades gracefully to MemorySaver.]] - `rationale_for` [EXTRACTED]
- [[get_checkpointer()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/get_checkpointer