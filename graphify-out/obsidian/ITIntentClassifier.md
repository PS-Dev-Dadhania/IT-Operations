---
source_file: "src/mcp_rag_agent/it_support/intent.py"
type: "code"
community: "ITCategory"
location: "L160"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ITCategory
---

# ITIntentClassifier

## Connections
- [[dot-__init__()_15]] - `calls` [EXTRACTED]
- [[dot-__init__()_44]] - `method` [EXTRACTED]
- [[dot-__init__()_12]] - `calls` [INFERRED]
- [[dot-classify()_1]] - `method` [EXTRACTED]
- [[dot-classify_async()]] - `method` [EXTRACTED]
- [[ITCategory]] - `uses` [INFERRED]
- [[ITIntentResult]] - `uses` [INFERRED]
- [[ProductionEvalRunner]] - `uses` [INFERRED]
- [[Rules are always evaluated before the optional injected LLM adapter.]] - `rationale_for` [EXTRACTED]
- [[RunbookRegistry]] - `uses` [INFERRED]
- [[classify_intent()]] - `calls` [EXTRACTED]
- [[intent.py]] - `contains` [EXTRACTED]
- [[mcp_rag_agentit_support__init__.py]] - `imports` [EXTRACTED]
- [[registry.py]] - `imports` [EXTRACTED]
- [[test_ambiguous_query_uses_injected_llm_fallback()]] - `uses` [INFERRED]
- [[test_deterministic_match_never_calls_fallback()]] - `uses` [INFERRED]
- [[test_known_queries_use_deterministic_rules()]] - `uses` [INFERRED]
- [[test_rule_classification_extracts_requested_entities()]] - `uses` [INFERRED]
- [[test_unknown_query_is_structured_and_concise()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/ITCategory