---
source_file: "src/mcp_rag_agent/agent/runner.py"
type: "code"
community: "RAGAgentRunner"
location: "L35"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RAGAgentRunner
---

# RAGAgentRunner

## Connections
- [[dot-__init__()_36]] - `references` [EXTRACTED]
- [[dot-__init__()_13]] - `references` [EXTRACTED]
- [[dot-__init__()_34]] - `method` [EXTRACTED]
- [[dot-_extract_citations()]] - `method` [EXTRACTED]
- [[dot-_extract_retrieval_info()]] - `method` [EXTRACTED]
- [[dot-_extract_retrieved_chunks()]] - `method` [EXTRACTED]
- [[dot-_is_out_of_scope_response()]] - `method` [EXTRACTED]
- [[dot-ainvoke()]] - `method` [EXTRACTED]
- [[dot-get_runner()]] - `references` [EXTRACTED]
- [[dot-run()]] - `method` [EXTRACTED]
- [[dot-set_runner()_1]] - `references` [EXTRACTED]
- [[dot-set_runner()]] - `references` [EXTRACTED]
- [[dot-test_ainvoke_returns_observability_fields()]] - `calls` [INFERRED]
- [[dot-test_conversation_persistence_across_instances()]] - `calls` [INFERRED]
- [[dot-test_empty_query_records_validation_error()]] - `calls` [INFERRED]
- [[dot-test_llm_execution_failure_records_model_error()]] - `calls` [INFERRED]
- [[dot-test_llm_timeout_records_timeout_error()]] - `calls` [INFERRED]
- [[dot-test_out_of_domain_query_records_guardrail_block()]] - `calls` [INFERRED]
- [[dot-test_prompt_injection_records_guardrail_block()]] - `calls` [INFERRED]
- [[dot-test_runner_ainvoke_backward_compatibility()]] - `calls` [INFERRED]
- [[dot-test_runner_blocks_query_prompt_injection()]] - `calls` [INFERRED]
- [[dot-test_runner_captures_structured_execution_metadata()]] - `calls` [INFERRED]
- [[dot-test_runner_citation_extraction_and_grounding()]] - `calls` [INFERRED]
- [[dot-test_runner_empty_query_returns_out_of_scope()]] - `calls` [INFERRED]
- [[dot-test_runner_enforces_grounded_refusal_on_empty_retrieval()]] - `calls` [INFERRED]
- [[dot-test_runner_enforces_refusal_on_low_confidence_retrieval()]] - `calls` [INFERRED]
- [[dot-test_runner_handles_out_of_domain_without_llm_invocation()]] - `calls` [INFERRED]
- [[dot-test_runner_out_of_scope_detection()]] - `calls` [INFERRED]
- [[dot-test_successful_run_extracts_tokens_and_cost()]] - `calls` [INFERRED]
- [[dot-test_thread_isolation()]] - `calls` [INFERRED]
- [[AgentExecutionMetadata]] - `uses` [INFERRED]
- [[AgentResponse]] - `uses` [INFERRED]
- [[ChatService]] - `uses` [INFERRED]
- [[ConversationService]] - `uses` [INFERRED]
- [[DecisionCategory]] - `uses` [INFERRED]
- [[GuardrailResult]] - `uses` [INFERRED]
- [[GuardrailViolation]] - `uses` [INFERRED]
- [[Production orchestrator encapsulating the 7 agentic responsibilities. 1. Query…]] - `rationale_for` [EXTRACTED]
- [[RAGGuardrails]] - `uses` [INFERRED]
- [[RetrievedChunkOutput]] - `uses` [INFERRED]
- [[TestAgentRunnerObservability]] - `uses` [INFERRED]
- [[TestAgentRunnerResponsibilities]] - `uses` [INFERRED]
- [[TestEmptyRetrievalHandling]] - `uses` [INFERRED]
- [[TestLowSimilarityCutoff]] - `uses` [INFERRED]
- [[TestOutOfDomainDetection]] - `uses` [INFERRED]
- [[TestThreadIsolationAndPersistence]] - `uses` [INFERRED]
- [[TestUserQueryPromptInjectionDefense]] - `uses` [INFERRED]
- [[ViolationType]] - `uses` [INFERRED]
- [[agent__init__.py]] - `imports` [EXTRACTED]
- [[app.py]] - `imports` [EXTRACTED]
- [[chat_service.py]] - `imports` [EXTRACTED]
- [[conversation_service.py]] - `imports` [EXTRACTED]
- [[create_agent.py]] - `imports` [EXTRACTED]
- [[create_app()]] - `uses` [INFERRED]
- [[create_rag_agent_instance()]] - `calls` [EXTRACTED]
- [[run_multi_turn_comparison()]] - `uses` [INFERRED]
- [[runner.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RAGAgentRunner