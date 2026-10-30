---
type: community
cohesion: 0.09
members: 32
---

# RetrievedChunkOutput

**Cohesion:** 0.09 - loosely connected
**Members:** 32 nodes

## Members
- [[dot-test_context_truncation_enforces_limit()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_detects_conflicting_day_allocations()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_evaluate_output_grounding_rejects_answer_with_fabricated_citation()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_evaluate_retrieval_context_records_conflict_warning()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_evaluate_retrieval_context_sandboxes_chunks()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_retrieval_below_confidence_threshold_triggers_violation()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_sanitize_document_neutralizes_injection_patterns()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[dot-test_validate_citations_detects_fabricated_sources()]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Apply context guardrails empty check, confidence threshold, injection…]] - rationale - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[Chunk with fusion score below threshold (0.015) is flagged as LOW_CONFIDENCE.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Citation referencing an unretrieved document is classified as…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Context guardrail wraps chunk text inside untrusted data tags and flags…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Context longer than max_context_chars is truncated and flagged.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Detects contradictory leave day allocations across different retrieved chunks.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Document with embedded system prompt override has injection text neutralized.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Inspect retrieved chunks for conflicting numerical or policy directives.]] - rationale - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[RetrievedChunkOutput]] - code - src/mcp_rag_agent/agent/models.py
- [[Scan and neutralize indirect prompt injections inside retrieved document text.]] - rationale - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[TestCitationValidation]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestConflictingDocumentsDetection]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestDocumentPromptInjectionDefense]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[TestMaxContextLimits]] - code - tests/unit_tests/test_guardrails_adversarial.py
- [[Typed representation of a single retrieved chunk for agent context.]] - rationale - src/mcp_rag_agent/agent/models.py
- [[Verify citations referencing documents not present in the retrieved set are…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify detection and warning when multiple retrieved documents specify…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify indirect prompt injections embedded in retrieved documents are…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[Verify retrieved context exceeding safety character limits is truncated cleanly.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[When an answer contains fabricated citations, decision downgrades to…]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[check_conflicting_documents()]] - code - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[evaluate_retrieval_context records CONFLICTING_DOCUMENTS violation and warning.]] - rationale - tests/unit_tests/test_guardrails_adversarial.py
- [[evaluate_retrieval_context()]] - code - src/mcp_rag_agent/guardrails/context_guardrails.py
- [[sanitize_document_text()]] - code - src/mcp_rag_agent/guardrails/context_guardrails.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/RetrievedChunkOutput
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_ViolationType]]
- 7 edges to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 5 edges to [[_COMMUNITY_agentmodels.py]]
- 4 edges to [[_COMMUNITY_RAGGuardrails]]
- 3 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_dot-run]]
- 2 edges to [[_COMMUNITY_TestAnswerGroundingValidation]]
- 1 edge to [[_COMMUNITY_RAGAgentRunner]]
- 1 edge to [[_COMMUNITY_Role]]

## Top bridge nodes
- [[RetrievedChunkOutput]] - degree 35, connects to 9 communities
- [[evaluate_retrieval_context()]] - degree 16, connects to 3 communities
- [[sanitize_document_text()]] - degree 7, connects to 3 communities
- [[TestCitationValidation]] - degree 7, connects to 2 communities
- [[TestConflictingDocumentsDetection]] - degree 6, connects to 2 communities