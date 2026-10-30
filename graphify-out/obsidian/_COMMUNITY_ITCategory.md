---
type: community
cohesion: 0.19
members: 18
---

# ITCategory

**Cohesion:** 0.19 - loosely connected
**Members:** 18 nodes

## Members
- [[ITCategory]] - code - src/mcp_rag_agent/it_support/models.py
- [[ITIntentClassifier]] - code - src/mcp_rag_agent/it_support/intent.py
- [[Offline checks for deterministic and fallback IT intent classification.]] - rationale - tests/unit_tests/it_support/test_intent.py
- [[Rules are always evaluated before the optional injected LLM adapter.]] - rationale - src/mcp_rag_agent/it_support/intent.py
- [[Runbook registry managing enterprise procedure lookup, versioning, and…]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Stable top-level taxonomy used by Phase 13-A classification.]] - rationale - src/mcp_rag_agent/it_support/models.py
- [[asyncio_14]] - code
- [[mcp_rag_agent_guardrails_input_guardrails]] - concept
- [[mcp_rag_agent_it_support_intent]] - concept
- [[parametrize_2]] - code
- [[registry.py]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[test_ambiguous_query_uses_injected_llm_fallback()]] - code - tests/unit_tests/it_support/test_intent.py
- [[test_deterministic_match_never_calls_fallback()]] - code - tests/unit_tests/it_support/test_intent.py
- [[test_intent.py]] - code - tests/unit_tests/it_support/test_intent.py
- [[test_it_terms_are_not_rejected_as_out_of_domain()]] - code - tests/unit_tests/it_support/test_intent.py
- [[test_known_queries_use_deterministic_rules()]] - code - tests/unit_tests/it_support/test_intent.py
- [[test_rule_classification_extracts_requested_entities()]] - code - tests/unit_tests/it_support/test_intent.py
- [[test_unknown_query_is_structured_and_concise()]] - code - tests/unit_tests/it_support/test_intent.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ITCategory
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Runbook]]
- 9 edges to [[_COMMUNITY_intent.py]]
- 8 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 6 edges to [[_COMMUNITY_RunbookExecutor]]
- 6 edges to [[_COMMUNITY_runbooks__init__.py]]
- 4 edges to [[_COMMUNITY_IncidentRecord]]
- 3 edges to [[_COMMUNITY_eval_runner.py]]
- 3 edges to [[_COMMUNITY_ticketsmodels.py]]
- 3 edges to [[_COMMUNITY_test_incidents.py]]
- 2 edges to [[_COMMUNITY_test_runbooks.py]]
- 2 edges to [[_COMMUNITY_mcp_servertools.py]]
- 2 edges to [[_COMMUNITY_dot-find_for_query]]
- 2 edges to [[_COMMUNITY_pytest]]
- 2 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_unittest_mock]]
- 1 edge to [[_COMMUNITY_create_runbook_subgraph]]
- 1 edge to [[_COMMUNITY_StepExecutionResult]]
- 1 edge to [[_COMMUNITY_TicketService]]
- 1 edge to [[_COMMUNITY_ViolationType]]
- 1 edge to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 1 edge to [[_COMMUNITY_test_admin_api.py]]

## Top bridge nodes
- [[ITCategory]] - degree 51, connects to 14 communities
- [[registry.py]] - degree 17, connects to 8 communities
- [[ITIntentClassifier]] - degree 19, connects to 5 communities
- [[test_intent.py]] - degree 13, connects to 3 communities
- [[test_ambiguous_query_uses_injected_llm_fallback()]] - degree 5, connects to 1 community