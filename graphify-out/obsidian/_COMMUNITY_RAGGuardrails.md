---
type: community
cohesion: 0.13
members: 20
---

# RAGGuardrails

**Cohesion:** 0.13 - loosely connected
**Members:** 20 nodes

## Members
- [[dot-__init__()_40]] - code - src/mcp_rag_agent/guardrails/manager.py
- [[dot-filter_context()]] - code - src/mcp_rag_agent/guardrails/manager.py
- [[dot-test_decision_taxonomy_values()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_guardrail_result_defaults_and_serialization()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-validate_input()]] - code - src/mcp_rag_agent/guardrails/manager.py
- [[dot-validate_output()]] - code - src/mcp_rag_agent/guardrails/manager.py
- [[Apply context guardrails empty check, confidence threshold, injection…_1]] - rationale - src/mcp_rag_agent/guardrails/manager.py
- [[BaseModel_19]] - code
- [[Complete diagnostic result returned by RAG safety guardrails.]] - rationale - src/mcp_rag_agent/guardrails/models.py
- [[GuardrailResult]] - code - src/mcp_rag_agent/guardrails/models.py
- [[GuardrailResult initializes with secure defaults and serializes cleanly to JSON.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Mask credentials, API keys, bearer tokens, passwords, and emails from text or…]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[Production Guardrails orchestrator enforcing the 4-tier decision taxonomy A.…]] - rationale - src/mcp_rag_agent/guardrails/manager.py
- [[RAGGuardrails]] - code - src/mcp_rag_agent/guardrails/manager.py
- [[TestGuardrailResultSchema]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Validate answer citations, source existence, and factual grounding against…]] - rationale - src/mcp_rag_agent/guardrails/manager.py
- [[Validate user input against prompt injection and out-of-domain scope.]] - rationale - src/mcp_rag_agent/guardrails/manager.py
- [[Verify GuardrailResult model validation, serialization, and 4-tier decision…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify the 4 required decision categories exist with correct string values.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[mask_sensitive_data()]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RAGGuardrails
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_ViolationType]]
- 4 edges to [[_COMMUNITY_RetrievedChunkOutput]]
- 3 edges to [[_COMMUNITY_dot-run]]
- 3 edges to [[_COMMUNITY_agentmodels.py]]
- 2 edges to [[_COMMUNITY_RAGAgentRunner]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_test_guardrails_adversarial.py]]

## Top bridge nodes
- [[RAGGuardrails]] - degree 16, connects to 6 communities
- [[GuardrailResult]] - degree 16, connects to 4 communities
- [[mask_sensitive_data()]] - degree 7, connects to 2 communities
- [[dot-validate_output()]] - degree 6, connects to 2 communities
- [[TestGuardrailResultSchema]] - degree 6, connects to 2 communities