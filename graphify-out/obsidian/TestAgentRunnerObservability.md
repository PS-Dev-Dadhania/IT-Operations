---
source_file: "tests/unit_tests/test_observability.py"
type: "code"
community: "RAGAgentRunner"
location: "L419"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RAGAgentRunner
---

# TestAgentRunnerObservability

## Connections
- [[dot-test_ainvoke_returns_observability_fields()]] - `method` [EXTRACTED]
- [[dot-test_empty_query_records_validation_error()]] - `method` [EXTRACTED]
- [[dot-test_llm_execution_failure_records_model_error()]] - `method` [EXTRACTED]
- [[dot-test_llm_timeout_records_timeout_error()]] - `method` [EXTRACTED]
- [[dot-test_out_of_domain_query_records_guardrail_block()]] - `method` [EXTRACTED]
- [[dot-test_prompt_injection_records_guardrail_block()]] - `method` [EXTRACTED]
- [[dot-test_successful_run_extracts_tokens_and_cost()]] - `method` [EXTRACTED]
- [[AgentResponse]] - `uses` [INFERRED]
- [[DecisionCategory]] - `uses` [INFERRED]
- [[RAGAgentRunner]] - `uses` [INFERRED]
- [[Test RAGAgentRunner end-to-end tracing, token usage extraction, and error…]] - `rationale_for` [EXTRACTED]
- [[test_observability.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/RAGAgentRunner