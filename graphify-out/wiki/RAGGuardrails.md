# RAGGuardrails

> 20 nodes · cohesion 0.13

## Key Concepts

- **RAGGuardrails** (16 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **GuardrailResult** (16 connections) — `src/mcp_rag_agent/guardrails/models.py`
- **.validate_input()** (7 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **mask_sensitive_data()** (7 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **.validate_output()** (6 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **TestGuardrailResultSchema** (6 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.filter_context()** (5 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **.test_guardrail_result_defaults_and_serialization()** (3 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **.__init__()** (2 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **BaseModel** (2 connections)
- **.test_decision_taxonomy_values()** (2 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Validate answer citations, source existence, and factual grounding against…** (1 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **Production Guardrails orchestrator enforcing the 4-tier decision taxonomy: A.…** (1 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **Validate user input against prompt injection and out-of-domain scope.** (1 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **Apply context guardrails: empty check, confidence threshold, injection…** (1 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **Complete diagnostic result returned by RAG safety guardrails.** (1 connections) — `src/mcp_rag_agent/guardrails/models.py`
- **Mask credentials, API keys, bearer tokens, passwords, and emails from text or…** (1 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **Verify GuardrailResult model validation, serialization, and 4-tier decision…** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **Verify the 4 required decision categories exist with correct string values.** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`
- **GuardrailResult initializes with secure defaults and serializes cleanly to JSON.** (1 connections) — `tests/unit_tests/test_guardrails_adversarial.py`

## Relationships

- [ViolationType](ViolationType.md) (17 shared connections)
- [RetrievedChunkOutput](RetrievedChunkOutput.md) (4 shared connections)
- [.run](run.md) (3 shared connections)
- [agent/models.py](agent-models.py.md) (3 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (2 shared connections)
- [Config](Config.md) (2 shared connections)
- [test_guardrails_adversarial.py](test_guardrails_adversarial.py.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/guardrails/manager.py`
- `src/mcp_rag_agent/guardrails/models.py`
- `src/mcp_rag_agent/guardrails/output_guardrails.py`
- `tests/unit_tests/test_guardrails_adversarial.py`

## Audit Trail

- EXTRACTED: 44 (77%)
- INFERRED: 13 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*