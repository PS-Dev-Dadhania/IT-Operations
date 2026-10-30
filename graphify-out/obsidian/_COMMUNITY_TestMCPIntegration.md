---
type: community
cohesion: 0.15
members: 13
---

# TestMCPIntegration

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-test_mcp_prompt_generation()]] - code - tests/integration_tests/test_mcp_integration.py
- [[dot-test_mcp_server_initialization_and_metadata()]] - code - tests/integration_tests/test_mcp_integration.py
- [[dot-test_search_policy_documents_typed_contract()]] - code - tests/integration_tests/test_mcp_integration.py
- [[Integration test suite for FastMCP server tools and endpoints.]] - rationale - tests/integration_tests/test_mcp_integration.py
- [[Provide a prompt template for grounded question-answering using retrieved…]] - rationale - src/mcp_rag_agent/mcp_server/server.py
- [[TestMCPIntegration]] - code - tests/integration_tests/test_mcp_integration.py
- [[Verify FastMCP server instance attributes.]] - rationale - tests/integration_tests/test_mcp_integration.py
- [[Verify search_policy_documents_typed returns structured SearchDocumentsOutput…]] - rationale - tests/integration_tests/test_mcp_integration.py
- [[Verify the grounded QA system prompt is properly loaded.]] - rationale - tests/integration_tests/test_mcp_integration.py
- [[asyncio_16]] - code
- [[grounded_qa_prompt()]] - code - src/mcp_rag_agent/mcp_server/server.py
- [[prompt]] - code
- [[skipif]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMCPIntegration
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_mcp_servertools.py]]

## Top bridge nodes
- [[TestMCPIntegration]] - degree 6, connects to 2 communities
- [[dot-test_search_policy_documents_typed_contract()]] - degree 6, connects to 1 community
- [[grounded_qa_prompt()]] - degree 4, connects to 1 community