# RetrievedChunkOutput

> 32 nodes · cohesion 0.09

## Key Concepts

- **RetrievedChunkOutput** (35 connections) — `src/mcp_rag_agent/agent/models.py`
- **evaluate_retrieval_context()** (16 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **check_conflicting_documents()** (7 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **sanitize_document_text()** (7 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **TestCitationValidation** (7 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestConflictingDocumentsDetection** (6 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestDocumentPromptInjectionDefense** (6 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **TestMaxContextLimits** (5 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_evaluate_output_grounding_rejects_answer_with_fabricated_citation()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_validate_citations_detects_fabricated_sources()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_detects_conflicting_day_allocations()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_evaluate_retrieval_context_records_conflict_warning()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_evaluate_retrieval_context_sandboxes_chunks()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_retrieval_below_confidence_threshold_triggers_violation()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_context_truncation_enforces_limit()** (4 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.test_sanitize_document_neutralizes_injection_patterns()** (3 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Typed representation of a single retrieved chunk for agent context.** (1 connections) — `src/mcp_rag_agent/agent/models.py`
- **Scan and neutralize indirect prompt injections inside retrieved document text.** (1 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **Inspect retrieved chunks for conflicting numerical or policy directives.** (1 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **Apply context guardrails: empty check, confidence threshold, injection…** (1 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **Verify indirect prompt injections embedded in retrieved documents are…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Document with embedded system prompt override has injection text neutralized.** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Context guardrail wraps chunk text inside untrusted data tags and flags…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Verify citations referencing documents not present in the retrieved set are…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Citation referencing an unretrieved document is classified as…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- *... and 7 more nodes in this community*

## Relationships

- [ViolationType](ViolationType.md) (23 shared connections)
- [test_guardrails_adversarial.py](test_guardrails_adversarial.py.md) (7 shared connections)
- [agent/models.py](agent-models.py.md) (5 shared connections)
- [RAGGuardrails](RAGGuardrails.md) (4 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (3 shared connections)
- [.run](run.md) (2 shared connections)
- [TestAnswerGroundingValidation](TestAnswerGroundingValidation.md) (2 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (1 shared connections)
- [Role](Role.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/agent/models.py`
- `src/mcp_rag_agent/guardrails/context_guardrails.py`
- `tests/unit_tests/test_guardrails_adversarial.py`

## Audit Trail

- EXTRACTED: 54 (59%)
- INFERRED: 38 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*