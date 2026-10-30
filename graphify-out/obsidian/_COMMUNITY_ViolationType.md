---
type: community
cohesion: 0.14
members: 37
---

# ViolationType

**Cohesion:** 0.14 - loosely connected
**Members:** 37 nodes

## Members
- [[Calculate lexical and factual overlap score between answer and retrieved…]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[Central RAGGuardrails manager orchestrating input, context, and output…]] - rationale - src/mcp_rag_agent/guardrails/manager.py
- [[Check if query is outside the scope of organizational policy question-answering.]] - rationale - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[Context guardrails Document prompt injection defense, confidence thresholds,…]] - rationale - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[Data models and abstractions for RAG Safety and Grounding Guardrails.]] - rationale - src/mcp_rag_agent/guardrails/models.py
- [[DecisionCategory]] - code - src/mcp_rag_agent/guardrails/models.py
- [[Details regarding a specific guardrail rule trigger.]] - rationale - src/mcp_rag_agent/guardrails/models.py
- [[Enum_1]] - code
- [[Extract cited document names, titles, or filenames from answer text.]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[GuardrailViolation]] - code - src/mcp_rag_agent/guardrails/models.py
- [[Input guardrails Prompt injection defense and out-of-domain detection for user…]] - rationale - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[Normalize file or document name for fuzzy comparison.]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[Normalize whitespace and strip unprintable control characters from user query.]] - rationale - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[Output guardrails Citation validation, source existence verification, answer…]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[RAG Safety and Grounding Guardrails package.]] - rationale - src/mcp_rag_agent/guardrails/__init__.py
- [[Scan user query for prompt injection, jailbreak attempts, or system prompt…]] - rationale - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[Specific guardrail violation categories.]] - rationale - src/mcp_rag_agent/guardrails/models.py
- [[The 4-tier grounding decision taxonomy required for production verification.]] - rationale - src/mcp_rag_agent/guardrails/models.py
- [[Validate answer citations and measure grounding score against retrieved chunks.…]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[Validate that every cited document actually exists in the retrieved chunks.…]] - rationale - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[ViolationType]] - code - src/mcp_rag_agent/guardrails/models.py
- [[_normalize_name()]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[calculate_grounding_score()]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[check_input_prompt_injection()]] - code - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[check_out_of_domain()]] - code - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[context_guardrails.py]] - code - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[evaluate_output_grounding()]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[extract_citations_from_text()]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[guardrails__init__.py]] - code - src/mcp_rag_agent/guardrails/__init__.py
- [[guardrailsmodels.py]] - code - src/mcp_rag_agent/guardrails/models.py
- [[input_guardrails.py]] - code - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[manager.py]] - code - src/mcp_rag_agent/guardrails/manager.py
- [[output_guardrails.py]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py
- [[re]] - concept
- [[sanitize_query()]] - code - src/mcp_rag_agent/guardrails/input_guardrails.py
- [[str_1]] - code
- [[validate_citations()]] - code - src/mcp_rag_agent/guardrails/output_guardrails.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ViolationType
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_RetrievedChunkOutput]]
- 17 edges to [[_COMMUNITY_RAGGuardrails]]
- 12 edges to [[_COMMUNITY_agentmodels.py]]
- 9 edges to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 9 edges to [[_COMMUNITY_typing]]
- 5 edges to [[_COMMUNITY_TestAnswerGroundingValidation]]
- 4 edges to [[_COMMUNITY_RAGAgentRunner]]
- 4 edges to [[_COMMUNITY_metrics__init__.py]]
- 3 edges to [[_COMMUNITY_dot-run]]
- 2 edges to [[_COMMUNITY_retrieval.py]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_ITCategory]]
- 1 edge to [[_COMMUNITY_ServiceStatusChecker]]
- 1 edge to [[_COMMUNITY_pydantic]]
- 1 edge to [[_COMMUNITY_ServiceStatusRecord]]
- 1 edge to [[_COMMUNITY_ingestion__init__.py]]
- 1 edge to [[_COMMUNITY_QueryPreprocessor]]
- 1 edge to [[_COMMUNITY_intent.py]]

## Top bridge nodes
- [[re]] - degree 23, connects to 11 communities
- [[DecisionCategory]] - degree 25, connects to 7 communities
- [[ViolationType]] - degree 26, connects to 6 communities
- [[manager.py]] - degree 24, connects to 5 communities
- [[GuardrailViolation]] - degree 17, connects to 5 communities