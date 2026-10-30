---
source_file: "src/mcp_rag_agent/guardrails/output_guardrails.py"
type: "code"
community: "ViolationType"
location: "L405"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ViolationType
---

# evaluate_output_grounding()

## Connections
- [[dot-test_evaluate_output_grounding_flags_ungrounded_content()]] - `calls` [INFERRED]
- [[dot-test_evaluate_output_grounding_rejects_answer_with_fabricated_citation()]] - `calls` [INFERRED]
- [[dot-validate_output()]] - `calls` [EXTRACTED]
- [[DecisionCategory]] - `uses` [INFERRED]
- [[GuardrailViolation]] - `calls` [EXTRACTED]
- [[RetrievedChunkOutput]] - `uses` [INFERRED]
- [[Validate answer citations and measure grounding score against retrieved chunks.…]] - `rationale_for` [EXTRACTED]
- [[ViolationType]] - `uses` [INFERRED]
- [[calculate_grounding_score()]] - `calls` [EXTRACTED]
- [[extract_citations_from_text()]] - `calls` [EXTRACTED]
- [[guardrails__init__.py]] - `imports` [EXTRACTED]
- [[manager.py]] - `imports` [EXTRACTED]
- [[output_guardrails.py]] - `contains` [EXTRACTED]
- [[validate_citations()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ViolationType