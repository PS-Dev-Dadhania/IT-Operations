---
source_file: "tests/unit_tests/test_session_memory.py"
type: "rationale"
community: "get_checkpointer"
location: "L135"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/get_checkpointer
---

# Ensure turn on thread_A does not leak into thread_B.

## Connections
- [[dot-test_thread_isolation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/get_checkpointer