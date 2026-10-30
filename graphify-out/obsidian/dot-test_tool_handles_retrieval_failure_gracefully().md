---
source_file: "tests/unit_tests/test_agent_architecture.py"
type: "code"
community: "TestTypedToolInterface"
location: "L117"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestTypedToolInterface
---

# .test_tool_handles_retrieval_failure_gracefully()

## Connections
- [[SearchDocumentsInput]] - `calls` [INFERRED]
- [[TestTypedToolInterface]] - `method` [EXTRACTED]
- [[Verify retriever crash does not crash the agent, returns status='error'.]] - `rationale_for` [EXTRACTED]
- [[asyncio_10]] - `references` [EXTRACTED]
- [[search_policy_documents_typed()]] - `calls` [INFERRED]
- [[set_advanced_retriever()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/TestTypedToolInterface