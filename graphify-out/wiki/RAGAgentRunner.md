# RAGAgentRunner

> 33 nodes · cohesion 0.09

## Key Concepts

- **RAGAgentRunner** (57 connections) — `src/mcp_rag_agent/agent/runner.py`
- **TestAgentRunnerObservability** (12 connections) — `tests/unit_tests/test_observability.py`
- **asyncio** (10 connections)
- **TestAgentRunnerResponsibilities** (9 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_runner_ainvoke_backward_compatibility()** (4 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_runner_captures_structured_execution_metadata()** (4 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_runner_citation_extraction_and_grounding()** (4 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_runner_empty_query_returns_out_of_scope()** (4 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_runner_out_of_scope_detection()** (4 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_ainvoke_returns_observability_fields()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_empty_query_records_validation_error()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_llm_execution_failure_records_model_error()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_llm_timeout_records_timeout_error()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_out_of_domain_query_records_guardrail_block()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_prompt_injection_records_guardrail_block()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_successful_run_extracts_tokens_and_cost()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.set_runner()** (3 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **Production orchestrator encapsulating the 7 agentic responsibilities. 1. Query…** (1 connections) — `src/mcp_rag_agent/agent/runner.py`
- **Inject or override the RAGAgentRunner (useful for unit testing).** (1 connections) — `src/mcp_rag_agent/api/services/chat_service.py`
- **Test suite for the 7 explicit agentic responsibilities and metadata tracking.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Responsibility 1: Empty query handled gracefully without model call.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Responsibility 3 & Execution Metadata: Tracking latencies, request_id,…** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Responsibility 6: Citation generation parsing.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Responsibility 7: Standard COSTAR refusal triggers is_out_of_scope=True.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Ensure runner.ainvoke works with LangGraph dict input and evaluation harness.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- *... and 8 more nodes in this community*

## Relationships

- [agent/models.py](agent-models.py.md) (9 shared connections)
- [.run](run.md) (8 shared connections)
- [test_guardrails_adversarial.py](test_guardrails_adversarial.py.md) (8 shared connections)
- [TestTypedToolInterface](TestTypedToolInterface.md) (5 shared connections)
- [ConversationService](ConversationService.md) (4 shared connections)
- [ViolationType](ViolationType.md) (4 shared connections)
- [ChatService](ChatService.md) (3 shared connections)
- [Config](Config.md) (2 shared connections)
- [get_checkpointer](get_checkpointer.md) (2 shared connections)
- [unittest_mock](unittest_mock.md) (2 shared connections)
- [RAGGuardrails](RAGGuardrails.md) (2 shared connections)
- [test_observability.py](test_observability.py.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/agent/runner.py`
- `src/mcp_rag_agent/api/services/chat_service.py`
- `tests/unit_tests/test_agent_architecture.py`
- `tests/unit_tests/test_observability.py`

## Audit Trail

- EXTRACTED: 65 (62%)
- INFERRED: 40 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*