---
source_file: "tests/unit_tests/test_agent_architecture.py"
type: "code"
community: "TestTypedToolInterface"
location: "L51"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TestTypedToolInterface
---

# .test_tool_invocation_success()

## Connections
- [[RetrievalLatency]] - `calls` [INFERRED]
- [[RetrievalResult]] - `calls` [INFERRED]
- [[RetrievedChunk]] - `calls` [INFERRED]
- [[SearchDocumentsInput]] - `calls` [INFERRED]
- [[TestTypedToolInterface]] - `method` [EXTRACTED]
- [[Verify successful retrieval returns typed SearchDocumentsOutput.]] - `rationale_for` [EXTRACTED]
- [[asyncio_10]] - `references` [EXTRACTED]
- [[search_policy_documents_typed()]] - `calls` [INFERRED]
- [[set_advanced_retriever()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/TestTypedToolInterface