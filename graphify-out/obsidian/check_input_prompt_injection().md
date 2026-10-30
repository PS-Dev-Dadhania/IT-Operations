---
source_file: "src/mcp_rag_agent/guardrails/input_guardrails.py"
type: "code"
community: "ViolationType"
location: "L189"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ViolationType
---

# check_input_prompt_injection()

## Connections
- [[dot-test_detects_query_prompt_injections()]] - `calls` [INFERRED]
- [[dot-validate_input()]] - `calls` [EXTRACTED]
- [[GuardrailViolation]] - `calls` [EXTRACTED]
- [[Scan user query for prompt injection, jailbreak attempts, or system prompt…]] - `rationale_for` [EXTRACTED]
- [[ViolationType]] - `uses` [INFERRED]
- [[guardrails__init__.py]] - `imports` [EXTRACTED]
- [[input_guardrails.py]] - `contains` [EXTRACTED]
- [[manager.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ViolationType