---
type: community
cohesion: 0.10
members: 22
---

# .run

**Cohesion:** 0.10 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_34]] - code - src/mcp_rag_agent/agent/runner.py
- [[dot-_extract_citations()]] - code - src/mcp_rag_agent/agent/runner.py
- [[dot-_extract_retrieval_info()]] - code - src/mcp_rag_agent/agent/runner.py
- [[dot-_extract_retrieved_chunks()]] - code - src/mcp_rag_agent/agent/runner.py
- [[dot-_is_out_of_scope_response()]] - code - src/mcp_rag_agent/agent/runner.py
- [[dot-ainvoke()]] - code - src/mcp_rag_agent/agent/runner.py
- [[dot-run()]] - code - src/mcp_rag_agent/agent/runner.py
- [[AgentExecutionMetadata]] - code - src/mcp_rag_agent/agent/models.py
- [[Any_19]] - code
- [[Construct mock RAGAgentRunner returning realistic structured AgentResponse.]] - rationale - tests/unit_tests/test_api.py
- [[Determine whether response indicates query was out of scope or ungrounded.]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Execute full agent workflow with timing, provenance, and grounding guarantees.…]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Extract cited document names from answer References section.]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Extract retrieved chunks and document metadata from message trace.]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Extract retrieved document IDs and tool execution latency from message trace.]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Initialize runner. Args agent_graph Compiled LangGraph agent runnable.…]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[LangGraph-compatible entry point preserving message dict interface with…]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[Structured execution metadata attached to every agent response.]] - rationale - src/mcp_rag_agent/agent/models.py
- [[Verify POST apiv1chat returns structured SourceDocument objects with…]] - rationale - tests/unit_tests/test_api.py
- [[_mock_aget_state()]] - code - tests/unit_tests/test_api.py
- [[mock_runner()]] - code - tests/unit_tests/test_api.py
- [[test_chat_endpoint_with_structured_sources()]] - code - tests/unit_tests/test_api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ObservabilityTracer]]
- 8 edges to [[_COMMUNITY_RAGAgentRunner]]
- 6 edges to [[_COMMUNITY_agentmodels.py]]
- 4 edges to [[_COMMUNITY_test_api.py]]
- 3 edges to [[_COMMUNITY_ViolationType]]
- 3 edges to [[_COMMUNITY_RAGGuardrails]]
- 2 edges to [[_COMMUNITY_RetrievedChunkOutput]]
- 1 edge to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_Config]]

## Top bridge nodes
- [[dot-run()]] - degree 21, connects to 7 communities
- [[AgentExecutionMetadata]] - degree 12, connects to 5 communities
- [[test_chat_endpoint_with_structured_sources()]] - degree 7, connects to 4 communities
- [[mock_runner()]] - degree 7, connects to 3 communities
- [[dot-_extract_retrieved_chunks()]] - degree 5, connects to 2 communities