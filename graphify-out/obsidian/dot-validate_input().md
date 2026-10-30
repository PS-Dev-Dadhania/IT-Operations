---
source_file: "src/mcp_rag_agent/guardrails/manager.py"
type: "code"
community: "RAGGuardrails"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RAGGuardrails
---

# .validate_input()

## Connections
- [[GuardrailResult]] - `references` [EXTRACTED]
- [[RAGGuardrails]] - `method` [EXTRACTED]
- [[Validate user input against prompt injection and out-of-domain scope.]] - `rationale_for` [EXTRACTED]
- [[check_input_prompt_injection()]] - `calls` [EXTRACTED]
- [[check_out_of_domain()]] - `calls` [EXTRACTED]
- [[mask_sensitive_data()]] - `calls` [EXTRACTED]
- [[sanitize_query()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RAGGuardrails