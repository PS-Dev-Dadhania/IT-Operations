# test_guardrails_adversarial.py

> 33 nodes · cohesion 0.07

## Key Concepts

- **test_guardrails_adversarial.py** (23 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestLowSimilarityCutoff** (8 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestEmptyRetrievalHandling** (7 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestOutOfDomainDetection** (7 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestUserQueryPromptInjectionDefense** (6 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **asyncio** (4 connections)
- **.test_runner_enforces_grounded_refusal_on_empty_retrieval()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_runner_enforces_refusal_on_low_confidence_retrieval()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_detects_out_of_domain_queries()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_runner_handles_out_of_domain_without_llm_invocation()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_detects_query_prompt_injections()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_runner_blocks_query_prompt_injection()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_evaluate_retrieval_context_empty()** (3 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestSensitiveInformationProtection** (3 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_mask_sensitive_data_scrubs_all_secret_patterns()** (3 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **parametrize** (2 connections)
- **mcp_rag_agent_guardrails_context_guardrails** (1 connections)
- **mcp_rag_agent_guardrails_manager** (1 connections)
- **mcp_rag_agent_guardrails_output_guardrails** (1 connections)
- **Unit tests for Phase 6: RAG Safety and Grounding Guardrails. Tests all 8…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Verify system enforces Category B refusal standard when database yields no…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Evaluating empty chunks list produces INSUFFICIENT_EVIDENCE and EMPTY_RETRIEVAL…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **When tool returns [EMPTY], runner enforces standard refusal rather than…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Verify direct prompt injection attempts, DAN jailbreaks, and system prompt…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **check_input_prompt_injection detects critical prompt injection attempts.** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- *... and 8 more nodes in this community*

## Relationships

- [ViolationType](ViolationType.md) (9 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (8 shared connections)
- [RetrievedChunkOutput](RetrievedChunkOutput.md) (7 shared connections)
- [unittest_mock](unittest_mock.md) (4 shared connections)
- [RAGGuardrails](RAGGuardrails.md) (2 shared connections)
- [pytest](pytest.md) (1 shared connections)
- [typing](typing.md) (1 shared connections)
- [ITCategory](ITCategory.md) (1 shared connections)
- [test_observability.py](test_observability.py.md) (1 shared connections)
- [TestAnswerGroundingValidation](TestAnswerGroundingValidation.md) (1 shared connections)

## Source Files

- `tests/unit_tests/test_guardrails_adversarial.py`

## Audit Trail

- EXTRACTED: 51 (72%)
- INFERRED: 20 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*