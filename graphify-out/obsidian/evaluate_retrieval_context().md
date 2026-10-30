---
source_file: "src/mcp_rag_agent/guardrails/context_guardrails.py"
type: "code"
community: "RetrievedChunkOutput"
location: "L77"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RetrievedChunkOutput
---

# evaluate_retrieval_context()

## Connections
- [[dot-filter_context()]] - `calls` [EXTRACTED]
- [[dot-test_context_truncation_enforces_limit()]] - `calls` [INFERRED]
- [[dot-test_evaluate_retrieval_context_empty()]] - `calls` [INFERRED]
- [[dot-test_evaluate_retrieval_context_records_conflict_warning()]] - `calls` [INFERRED]
- [[dot-test_evaluate_retrieval_context_sandboxes_chunks()]] - `calls` [INFERRED]
- [[dot-test_retrieval_below_confidence_threshold_triggers_violation()]] - `calls` [INFERRED]
- [[Apply context guardrails empty check, confidence threshold, injection…]] - `rationale_for` [EXTRACTED]
- [[DecisionCategory]] - `uses` [INFERRED]
- [[GuardrailViolation]] - `calls` [EXTRACTED]
- [[RetrievedChunkOutput]] - `uses` [INFERRED]
- [[ViolationType]] - `uses` [INFERRED]
- [[check_conflicting_documents()]] - `calls` [EXTRACTED]
- [[context_guardrails.py]] - `contains` [EXTRACTED]
- [[guardrails__init__.py]] - `imports` [EXTRACTED]
- [[manager.py]] - `imports` [EXTRACTED]
- [[sanitize_document_text()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RetrievedChunkOutput