# .run

> 22 nodes · cohesion 0.10

## Key Concepts

- **.run()** (21 connections) — `src/mcp_rag_agent/agent/runner.py`
- **AgentExecutionMetadata** (12 connections) — `src/mcp_rag_agent/agent/models.py`
- **mock_runner()** (7 connections) — `tests/unit_tests/test_api.py`
- **test_chat_endpoint_with_structured_sources()** (7 connections) — `tests/unit_tests/test_api.py`
- **._extract_retrieved_chunks()** (5 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Any** (4 connections)
- **.ainvoke()** (4 connections) — `src/mcp_rag_agent/agent/runner.py`
- **._extract_retrieval_info()** (4 connections) — `src/mcp_rag_agent/agent/runner.py`
- **.__init__()** (4 connections) — `src/mcp_rag_agent/agent/runner.py`
- **._extract_citations()** (3 connections) — `src/mcp_rag_agent/agent/runner.py`
- **._is_out_of_scope_response()** (3 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Structured execution metadata attached to every agent response.** (1 connections) — `src/mcp_rag_agent/agent/models.py`
- **Extract retrieved chunks and document metadata from message trace.** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Extract cited document names from answer References section.** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Determine whether response indicates query was out of scope or ungrounded.** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Execute full agent workflow with timing, provenance, and grounding guarantees.…** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **LangGraph-compatible entry point preserving message dict interface with…** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Initialize runner. Args: agent_graph: Compiled LangGraph agent runnable.…** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Extract retrieved document IDs and tool execution latency from message trace.** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **_mock_aget_state()** (1 connections) — `tests/unit_tests/test_api.py`
- **Construct mock RAGAgentRunner returning realistic structured AgentResponse.** (1 connections) — `tests/unit_tests/test_api.py`
- **Verify POST /api/v1/chat returns structured SourceDocument objects with…** (1 connections) — `tests/unit_tests/test_api.py`

## Relationships

- [ObservabilityTracer](ObservabilityTracer.md) (10 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (8 shared connections)
- [agent/models.py](agent-models.py.md) (6 shared connections)
- [test_api.py](test_api.py.md) (4 shared connections)
- [RAGGuardrails](RAGGuardrails.md) (3 shared connections)
- [ViolationType](ViolationType.md) (3 shared connections)
- [RetrievedChunkOutput](RetrievedChunkOutput.md) (2 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (1 shared connections)
- [audit.py](audit.py.md) (1 shared connections)
- [Config](Config.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/agent/models.py`
- `src/mcp_rag_agent/agent/runner.py`
- `tests/unit_tests/test_api.py`

## Audit Trail

- EXTRACTED: 43 (69%)
- INFERRED: 19 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*