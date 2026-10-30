# TestTypedToolInterface

> 24 nodes · cohesion 0.12

## Key Concepts

- **TestTypedToolInterface** (13 connections) — `tests/unit_tests/test_agent_architecture.py`
- **RetrievalLatency** (11 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **RetrievalResult** (11 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **test_retrieval_confidential_security_docs_filtered_for_employee()** (11 connections) — `tests/unit_tests/security/test_security_regression.py`
- **.test_tool_invocation_success()** (9 connections) — `tests/unit_tests/test_agent_architecture.py`
- **asyncio** (8 connections)
- **.test_tool_invocation_empty_results()** (8 connections) — `tests/unit_tests/test_agent_architecture.py`
- **set_advanced_retriever()** (7 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **.test_tool_handles_retrieval_failure_gracefully()** (6 connections) — `tests/unit_tests/test_agent_architecture.py`
- **BaseModel** (5 connections)
- **CandidateItem** (4 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **.test_tool_input_validation_errors()** (3 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_secret_masking()** (2 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Set or override the AdvancedRetriever instance (for testing and dependency…** (1 connections) — `src/mcp_rag_agent/mcp_server/tools.py`
- **Full retrieval response containing ranked chunks, latency metrics, and optional…** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **Intermediate candidate document from vector or keyword search.** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **Detailed timing metrics across retrieval stages in milliseconds.** (1 connections) — `src/mcp_rag_agent/retrieval/models.py`
- **Confidential security ops docs are stripped BEFORE the LLM sees retrieval…** (1 connections) — `tests/unit_tests/security/test_security_regression.py`
- **Verify Pydantic input model rejects invalid queries and limits.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Verify retriever crash does not crash the agent, returns status='error'.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Verify secrets like OpenAI keys and Mongo URIs are scrubbed.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Test suite for search_policy_documents strongly typed schema and error…** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Verify successful retrieval returns typed SearchDocumentsOutput.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Verify empty results return status='empty' and clean fallback string.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`

## Relationships

- [agent/models.py](agent-models.py.md) (11 shared connections)
- [retrieval/pipeline.py](retrieval-pipeline.py.md) (9 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (5 shared connections)
- [RetrievedChunk](RetrievedChunk.md) (4 shared connections)
- [AdvancedRetriever](AdvancedRetriever.md) (3 shared connections)
- [.retrieve](retrieve.md) (2 shared connections)
- [Role](Role.md) (2 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (1 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (1 shared connections)
- [SecuritySubject](SecuritySubject.md) (1 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [setup_services](setup_services.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/mcp_server/tools.py`
- `src/mcp_rag_agent/retrieval/models.py`
- `tests/unit_tests/security/test_security_regression.py`
- `tests/unit_tests/test_agent_architecture.py`

## Audit Trail

- EXTRACTED: 44 (59%)
- INFERRED: 31 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*