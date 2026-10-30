# ViolationType

> 37 nodes · cohesion 0.14

## Key Concepts

- **ViolationType** (26 connections) — `src/mcp_rag_agent/guardrails/models.py`
- **DecisionCategory** (25 connections) — `src/mcp_rag_agent/guardrails/models.py`
- **manager.py** (24 connections) — `src/mcp_rag_agent/guardrails/manager.py`
- **re** (23 connections)
- **guardrails/__init__.py** (22 connections) — `src/mcp_rag_agent/guardrails/__init__.py`
- **GuardrailViolation** (17 connections) — `src/mcp_rag_agent/guardrails/models.py`
- **output_guardrails.py** (17 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **context_guardrails.py** (15 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **guardrails/models.py** (15 connections) — `src/mcp_rag_agent/guardrails/models.py`
- **evaluate_output_grounding()** (14 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **input_guardrails.py** (12 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- **check_out_of_domain()** (10 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- **validate_citations()** (9 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **check_input_prompt_injection()** (8 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- **calculate_grounding_score()** (7 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **sanitize_query()** (6 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- **extract_citations_from_text()** (4 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **_normalize_name()** (4 connections) — `src/mcp_rag_agent/guardrails/output_guardrails.py`
- **Enum** (3 connections)
- **str** (2 connections)
- **Context guardrails: Document prompt injection defense, confidence thresholds,…** (1 connections) — `src/mcp_rag_agent/guardrails/context_guardrails.py`
- **RAG Safety and Grounding Guardrails package.** (1 connections) — `src/mcp_rag_agent/guardrails/__init__.py`
- **Input guardrails: Prompt injection defense and out-of-domain detection for user…** (1 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- **Normalize whitespace and strip unprintable control characters from user query.** (1 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- **Scan user query for prompt injection, jailbreak attempts, or system prompt…** (1 connections) — `src/mcp_rag_agent/guardrails/input_guardrails.py`
- *... and 12 more nodes in this community*

## Relationships

- [RetrievedChunkOutput](RetrievedChunkOutput.md) (23 shared connections)
- [RAGGuardrails](RAGGuardrails.md) (17 shared connections)
- [agent/models.py](agent-models.py.md) (12 shared connections)
- [typing](typing.md) (9 shared connections)
- [test_guardrails_adversarial.py](test_guardrails_adversarial.py.md) (9 shared connections)
- [TestAnswerGroundingValidation](TestAnswerGroundingValidation.md) (5 shared connections)
- [metrics/__init__.py](metrics-__init__.py.md) (4 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (4 shared connections)
- [.run](run.md) (3 shared connections)
- [retrieval.py](retrieval.py.md) (2 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [ServiceStatusChecker](ServiceStatusChecker.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/guardrails/__init__.py`
- `src/mcp_rag_agent/guardrails/context_guardrails.py`
- `src/mcp_rag_agent/guardrails/input_guardrails.py`
- `src/mcp_rag_agent/guardrails/manager.py`
- `src/mcp_rag_agent/guardrails/models.py`
- `src/mcp_rag_agent/guardrails/output_guardrails.py`

## Audit Trail

- EXTRACTED: 147 (78%)
- INFERRED: 42 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*