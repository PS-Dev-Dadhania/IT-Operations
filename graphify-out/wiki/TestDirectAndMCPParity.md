# TestDirectAndMCPParity

> 6 nodes · cohesion 0.33

## Key Concepts

- **TestDirectAndMCPParity** (4 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_direct_and_mcp_input_schema_equivalence()** (3 connections) — `tests/unit_tests/test_agent_architecture.py`
- **.test_direct_and_mcp_tool_name_parity()** (3 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Verify tool signatures and behavioral consistency between Direct and MCP modes.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Both direct mode and MCP mode must expose 'search_policy_documents'.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`
- **Both direct tool and MCP tool must accept 'query' and 'top_k' parameters.** (1 connections) — `tests/unit_tests/test_agent_architecture.py`

## Relationships

- [agent/models.py](agent-models.py.md) (2 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)

## Source Files

- `tests/unit_tests/test_agent_architecture.py`

## Audit Trail

- EXTRACTED: 6 (75%)
- INFERRED: 2 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*