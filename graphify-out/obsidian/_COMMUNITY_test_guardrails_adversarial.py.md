---
type: community
cohesion: 0.07
members: 33
---

# test_guardrails_adversarial.py

**Cohesion:** 0.07 - loosely connected
**Members:** 33 nodes

## Members
- [[dot-test_detects_out_of_domain_queries()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_detects_query_prompt_injections()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_evaluate_retrieval_context_empty()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_mask_sensitive_data_scrubs_all_secret_patterns()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_runner_blocks_query_prompt_injection()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_runner_enforces_grounded_refusal_on_empty_retrieval()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_runner_enforces_refusal_on_low_confidence_retrieval()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_runner_handles_out_of_domain_without_llm_invocation()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Evaluating empty chunks list produces INSUFFICIENT_EVIDENCE and EMPTY_RETRIEVAL…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Out-of-domain queries must be flagged before retrieval or model invocation.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[RAGAgentRunner halts execution when prompt injection query is received.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[RAGAgentRunner must return Category C (OUT_OF_DOMAIN) without invoking the…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Runner replaces guess with grounded refusal when retrieval reports low…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Scrub OpenAI API keys, MongoDB URIs, Bearer tokens, passwords, and email…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[TestEmptyRetrievalHandling]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestLowSimilarityCutoff]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestOutOfDomainDetection]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestSensitiveInformationProtection]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestUserQueryPromptInjectionDefense]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Unit tests for Phase 6 RAG Safety and Grounding Guardrails. Tests all 8…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify direct prompt injection attempts, DAN jailbreaks, and system prompt…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify retrieval results falling below the confidence threshold are rejected.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify sensitive credentials, keys, bearer tokens, passwords, and emails are…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify system accurately distinguishes questions outside Company XYZ policy…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify system enforces Category B refusal standard when database yields no…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[When tool returns EMPTY, runner enforces standard refusal rather than…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[asyncio_2]] - code
- [[check_input_prompt_injection detects critical prompt injection attempts.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[mcp_rag_agent_guardrails_context_guardrails]] - concept
- [[mcp_rag_agent_guardrails_manager]] - concept
- [[mcp_rag_agent_guardrails_output_guardrails]] - concept
- [[parametrize]] - code
- [[test_guardrails_adversarial.py]] - code - tests/unit_tests/test_guardrails_adversarial.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_guardrails_adversarialpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ViolationType]]
- 8 edges to [[_COMMUNITY_RAGAgentRunner]]
- 7 edges to [[_COMMUNITY_RetrievedChunkOutput]]
- 4 edges to [[_COMMUNITY_unittest_mock]]
- 2 edges to [[_COMMUNITY_RAGGuardrails]]
- 1 edge to [[_COMMUNITY_TestAnswerGroundingValidation]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_ITCategory]]
- 1 edge to [[_COMMUNITY_test_observability.py]]

## Top bridge nodes
- [[test_guardrails_adversarial.py]] - degree 23, connects to 8 communities
- [[TestLowSimilarityCutoff]] - degree 8, connects to 3 communities
- [[TestEmptyRetrievalHandling]] - degree 7, connects to 2 communities
- [[TestOutOfDomainDetection]] - degree 7, connects to 2 communities
- [[TestUserQueryPromptInjectionDefense]] - degree 6, connects to 2 communities