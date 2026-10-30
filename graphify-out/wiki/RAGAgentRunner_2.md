# RAGAgentRunner

> God node · 57 connections · `src/mcp_rag_agent/agent/runner.py`

**Community:** [RAGAgentRunner](RAGAgentRunner.md)

## Connections by Relation

### calls
- create_rag_agent_instance() `EXTRACTED`
- .test_conversation_persistence_across_instances() `INFERRED`
- .test_thread_isolation() `INFERRED`
- .test_runner_ainvoke_backward_compatibility() `INFERRED`
- .test_runner_captures_structured_execution_metadata() `INFERRED`
- .test_runner_citation_extraction_and_grounding() `INFERRED`
- .test_runner_empty_query_returns_out_of_scope() `INFERRED`
- .test_runner_out_of_scope_detection() `INFERRED`
- .test_runner_enforces_grounded_refusal_on_empty_retrieval() `INFERRED`
- .test_runner_enforces_refusal_on_low_confidence_retrieval() `INFERRED`
- .test_runner_handles_out_of_domain_without_llm_invocation() `INFERRED`
- .test_runner_blocks_query_prompt_injection() `INFERRED`
- .test_ainvoke_returns_observability_fields() `INFERRED`
- .test_empty_query_records_validation_error() `INFERRED`
- .test_llm_execution_failure_records_model_error() `INFERRED`
- .test_llm_timeout_records_timeout_error() `INFERRED`
- .test_out_of_domain_query_records_guardrail_block() `INFERRED`
- .test_prompt_injection_records_guardrail_block() `INFERRED`
- .test_successful_run_extracts_tokens_and_cost() `INFERRED`

### contains
- runner.py `EXTRACTED`

### imports
- create_agent.py `EXTRACTED`
- app.py `EXTRACTED`
- conversation_service.py `EXTRACTED`
- chat_service.py `EXTRACTED`
- agent/__init__.py `EXTRACTED`

### method
- .run() `EXTRACTED`
- ._extract_retrieved_chunks() `EXTRACTED`
- .ainvoke() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._extract_retrieval_info() `EXTRACTED`
- ._extract_citations() `EXTRACTED`
- ._is_out_of_scope_response() `EXTRACTED`

### rationale_for
- Production orchestrator encapsulating the 7 agentic responsibilities. 1. Query… `EXTRACTED`

### references
- .get_runner() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .set_runner() `EXTRACTED`
- .set_runner() `EXTRACTED`

### uses
- [RetrievedChunkOutput](RetrievedChunkOutput.md) `INFERRED`
- [ViolationType](ViolationType.md) `INFERRED`
- [ConversationService](ConversationService.md) `INFERRED`
- DecisionCategory `INFERRED`
- create_app() `INFERRED`
- [ChatService](ChatService.md) `INFERRED`
- GuardrailViolation `INFERRED`
- GuardrailResult `INFERRED`
- [RAGGuardrails](RAGGuardrails.md) `INFERRED`
- AgentResponse `INFERRED`
- AgentExecutionMetadata `INFERRED`
- TestAgentRunnerObservability `INFERRED`
- TestThreadIsolationAndPersistence `INFERRED`
- TestAgentRunnerResponsibilities `INFERRED`
- TestLowSimilarityCutoff `INFERRED`
- TestEmptyRetrievalHandling `INFERRED`
- TestOutOfDomainDetection `INFERRED`
- TestUserQueryPromptInjectionDefense `INFERRED`
- run_multi_turn_comparison() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*