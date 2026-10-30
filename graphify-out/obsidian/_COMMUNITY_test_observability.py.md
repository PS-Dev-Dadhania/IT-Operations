---
type: community
cohesion: 0.18
members: 11
---

# test_observability.py

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-test_all_seven_error_categories_exist()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_error_record_creation_and_serialization()]] - code - tests/unit_tests/test_observability.py
- [[Test the 7 required error categories and ErrorRecord model.]] - rationale - tests/unit_tests/test_observability.py
- [[TestErrorTaxonomy]] - code - tests/unit_tests/test_observability.py
- [[Unit tests for Phase 8 Production Observability. Validates correlation context…]] - rationale - tests/unit_tests/test_observability.py
- [[Verify ErrorRecord fields and serialization.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify that all 7 required error categories are strictly defined.]] - rationale - tests/unit_tests/test_observability.py
- [[mcp_rag_agent_core_log_setup]] - concept
- [[mcp_rag_agent_guardrails_models]] - concept
- [[mcp_rag_agent_observability]] - concept
- [[test_observability.py]] - code - tests/unit_tests/test_observability.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_observabilitypy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_unittest_mock]]
- 3 edges to [[_COMMUNITY_ObservabilityTracer]]
- 2 edges to [[_COMMUNITY_RAGAgentRunner]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_TestStructuredLoggingAndRedaction]]
- 1 edge to [[_COMMUNITY_TestObservabilityTracer]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_test_guardrails_adversarial.py]]
- 1 edge to [[_COMMUNITY_test_mcp_it_tools.py]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_test_it_evaluation.py]]
- 1 edge to [[_COMMUNITY_test_mongodb_integration.py]]

## Top bridge nodes
- [[test_observability.py]] - degree 21, connects to 10 communities
- [[mcp_rag_agent_guardrails_models]] - degree 3, connects to 2 communities
- [[dot-test_error_record_creation_and_serialization()]] - degree 3, connects to 1 community
- [[mcp_rag_agent_core_log_setup]] - degree 2, connects to 1 community