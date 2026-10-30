---
source_file: "src/mcp_rag_agent/guardrails/input_guardrails.py"
type: "code"
community: "ViolationType"
location: "L213"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ViolationType
---

# check_out_of_domain()

## Connections
- [[dot-test_detects_out_of_domain_queries()]] - `calls` [INFERRED]
- [[dot-validate_input()]] - `calls` [EXTRACTED]
- [[Check if query is outside the scope of organizational policy question-answering.]] - `rationale_for` [EXTRACTED]
- [[GuardrailViolation]] - `calls` [EXTRACTED]
- [[ViolationType]] - `uses` [INFERRED]
- [[guardrails__init__.py]] - `imports` [EXTRACTED]
- [[input_guardrails.py]] - `contains` [EXTRACTED]
- [[manager.py]] - `imports` [EXTRACTED]
- [[re]] - `calls` [EXTRACTED]
- [[test_it_terms_are_not_rejected_as_out_of_domain()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/ViolationType