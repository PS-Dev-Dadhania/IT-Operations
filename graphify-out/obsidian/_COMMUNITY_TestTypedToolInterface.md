---
type: community
cohesion: 0.12
members: 24
---

# TestTypedToolInterface

**Cohesion:** 0.12 - loosely connected
**Members:** 24 nodes

## Members
- [[dot-test_secret_masking()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_tool_handles_retrieval_failure_gracefully()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_tool_input_validation_errors()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_tool_invocation_empty_results()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_tool_invocation_success()]] - code - tests/unit_tests/test_agent_architecture.py
- [[BaseModel_17]] - code
- [[CandidateItem]] - code - src/mcp_rag_agent/retrieval/models.py
- [[Confidential security ops docs are stripped BEFORE the LLM sees retrieval…]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[Detailed timing metrics across retrieval stages in milliseconds.]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[Full retrieval response containing ranked chunks, latency metrics, and optional…]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[Intermediate candidate document from vector or keyword search.]] - rationale - src/mcp_rag_agent/retrieval/models.py
- [[RetrievalLatency]] - code - src/mcp_rag_agent/retrieval/models.py
- [[RetrievalResult]] - code - src/mcp_rag_agent/retrieval/models.py
- [[Set or override the AdvancedRetriever instance (for testing and dependency…]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Test suite for search_policy_documents strongly typed schema and error…]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[TestTypedToolInterface]] - code - tests/unit_tests/test_agent_architecture.py
- [[Verify Pydantic input model rejects invalid queries and limits.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Verify empty results return status='empty' and clean fallback string.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Verify retriever crash does not crash the agent, returns status='error'.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Verify secrets like OpenAI keys and Mongo URIs are scrubbed.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Verify successful retrieval returns typed SearchDocumentsOutput.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[asyncio_10]] - code
- [[set_advanced_retriever()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[test_retrieval_confidential_security_docs_filtered_for_employee()]] - code - tests/unit_tests/security/test_security_regression.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestTypedToolInterface
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_agentmodels.py]]
- 9 edges to [[_COMMUNITY_retrievalpipeline.py]]
- 5 edges to [[_COMMUNITY_RAGAgentRunner]]
- 4 edges to [[_COMMUNITY_RetrievedChunk]]
- 3 edges to [[_COMMUNITY_AdvancedRetriever]]
- 2 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_dot-retrieve]]
- 1 edge to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_setup_services]]
- 1 edge to [[_COMMUNITY_SecuritySubject]]
- 1 edge to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]

## Top bridge nodes
- [[test_retrieval_confidential_security_docs_filtered_for_employee()]] - degree 11, connects to 5 communities
- [[TestTypedToolInterface]] - degree 13, connects to 4 communities
- [[RetrievalLatency]] - degree 11, connects to 3 communities
- [[RetrievalResult]] - degree 11, connects to 3 communities
- [[dot-test_tool_invocation_success()]] - degree 9, connects to 2 communities