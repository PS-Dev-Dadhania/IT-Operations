---
type: community
cohesion: 0.09
members: 33
---

# RAGAgentRunner

**Cohesion:** 0.09 - loosely connected
**Members:** 33 nodes

## Members
- [[dot-set_runner()_1]] - code - src/mcp_rag_agent/api/services/chat_service.py
- [[dot-test_ainvoke_returns_observability_fields()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_empty_query_records_validation_error()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_llm_execution_failure_records_model_error()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_llm_timeout_records_timeout_error()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_out_of_domain_query_records_guardrail_block()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_prompt_injection_records_guardrail_block()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_runner_ainvoke_backward_compatibility()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_runner_captures_structured_execution_metadata()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_runner_citation_extraction_and_grounding()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_runner_empty_query_returns_out_of_scope()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_runner_out_of_scope_detection()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_successful_run_extracts_tokens_and_cost()]] - code - tests/unit_tests/test_observability.py
- [[Ensure runner.ainvoke works with LangGraph dict input and evaluation harness.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Inject or override the RAGAgentRunner (useful for unit testing).]] - rationale - src/mcp_rag_agent/api/services/chat_service.py
- [[Production orchestrator encapsulating the 7 agentic responsibilities. 1. Query…]] - rationale - src/mcp_rag_agent/agent/runner.py
- [[RAGAgentRunner]] - code - src/mcp_rag_agent/agent/runner.py
- [[Responsibility 1 Empty query handled gracefully without model call.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Responsibility 3 & Execution Metadata Tracking latencies, request_id,…]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Responsibility 6 Citation generation parsing.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Responsibility 7 Standard COSTAR refusal triggers is_out_of_scope=True.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Test RAGAgentRunner end-to-end tracing, token usage extraction, and error…]] - rationale - tests/unit_tests/test_observability.py
- [[Test suite for the 7 explicit agentic responsibilities and metadata tracking.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[TestAgentRunnerObservability]] - code - tests/unit_tests/test_observability.py
- [[TestAgentRunnerResponsibilities]] - code - tests/unit_tests/test_agent_architecture.py
- [[Verify ainvoke dictionary output includes token_usage, errors, and trace.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify empty queries record ErrorCategory.VALIDATION_ERROR and status='blocked'.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify graph invocation exceptions record ErrorCategory.MODEL_ERROR.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify out-of-domain query records ErrorCategory.GUARDRAIL_BLOCK.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify prompt injection queries record ErrorCategory.GUARDRAIL_BLOCK.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify successful response captures token usage, cost, and trace spans.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify timeout exceptions record ErrorCategory.TIMEOUT.]] - rationale - tests/unit_tests/test_observability.py
- [[asyncio_3]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RAGAgentRunner
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_agentmodels.py]]
- 8 edges to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 8 edges to [[_COMMUNITY_dot-run]]
- 5 edges to [[_COMMUNITY_TestTypedToolInterface]]
- 4 edges to [[_COMMUNITY_ConversationService]]
- 4 edges to [[_COMMUNITY_ViolationType]]
- 3 edges to [[_COMMUNITY_ChatService]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_get_checkpointer]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 2 edges to [[_COMMUNITY_RAGGuardrails]]
- 2 edges to [[_COMMUNITY_test_observability.py]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_RetrievedChunkOutput]]
- 1 edge to [[_COMMUNITY_ObservabilityTracer]]
- 1 edge to [[_COMMUNITY_TestObservabilityTracer]]

## Top bridge nodes
- [[RAGAgentRunner]] - degree 57, connects to 12 communities
- [[TestAgentRunnerObservability]] - degree 12, connects to 3 communities
- [[asyncio_3]] - degree 10, connects to 3 communities
- [[TestAgentRunnerResponsibilities]] - degree 9, connects to 2 communities
- [[dot-test_runner_ainvoke_backward_compatibility()]] - degree 4, connects to 1 community