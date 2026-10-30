# ITCategory

> 18 nodes · cohesion 0.19

## Key Concepts

- **ITCategory** (51 connections) — `src/mcp_rag_agent/it_support/models.py`
- **ITIntentClassifier** (19 connections) — `src/mcp_rag_agent/it_support/intent.py`
- **registry.py** (17 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **test_intent.py** (13 connections) — `tests/unit_tests/it_support/test_intent.py`
- **test_ambiguous_query_uses_injected_llm_fallback()** (5 connections) — `tests/unit_tests/it_support/test_intent.py`
- **test_deterministic_match_never_calls_fallback()** (4 connections) — `tests/unit_tests/it_support/test_intent.py`
- **test_known_queries_use_deterministic_rules()** (4 connections) — `tests/unit_tests/it_support/test_intent.py`
- **test_it_terms_are_not_rejected_as_out_of_domain()** (3 connections) — `tests/unit_tests/it_support/test_intent.py`
- **test_rule_classification_extracts_requested_entities()** (3 connections) — `tests/unit_tests/it_support/test_intent.py`
- **test_unknown_query_is_structured_and_concise()** (3 connections) — `tests/unit_tests/it_support/test_intent.py`
- **mcp_rag_agent_guardrails_input_guardrails** (2 connections)
- **mcp_rag_agent_it_support_intent** (2 connections)
- **asyncio** (2 connections)
- **parametrize** (2 connections)
- **Rules are always evaluated before the optional injected LLM adapter.** (1 connections) — `src/mcp_rag_agent/it_support/intent.py`
- **Stable top-level taxonomy used by Phase 13-A classification.** (1 connections) — `src/mcp_rag_agent/it_support/models.py`
- **Runbook registry managing enterprise procedure lookup, versioning, and…** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **Offline checks for deterministic and fallback IT intent classification.** (1 connections) — `tests/unit_tests/it_support/test_intent.py`

## Relationships

- [Runbook](Runbook.md) (16 shared connections)
- [intent.py](intent.py.md) (9 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (8 shared connections)
- [RunbookExecutor](RunbookExecutor.md) (6 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (6 shared connections)
- [IncidentRecord](IncidentRecord.md) (4 shared connections)
- [eval_runner.py](eval_runner.py.md) (3 shared connections)
- [tickets/models.py](tickets-models.py.md) (3 shared connections)
- [test_incidents.py](test_incidents.py.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [.find_for_query](find_for_query.md) (2 shared connections)
- [test_runbooks.py](test_runbooks.py.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/intent.py`
- `src/mcp_rag_agent/it_support/models.py`
- `src/mcp_rag_agent/it_support/runbooks/registry.py`
- `tests/unit_tests/it_support/test_intent.py`

## Audit Trail

- EXTRACTED: 61 (58%)
- INFERRED: 44 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*