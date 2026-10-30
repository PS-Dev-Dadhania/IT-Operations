---
type: community
cohesion: 0.33
members: 6
---

# TestDirectAndMCPParity

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_direct_and_mcp_input_schema_equivalence()]] - code - tests/unit_tests/test_agent_architecture.py
- [[dot-test_direct_and_mcp_tool_name_parity()]] - code - tests/unit_tests/test_agent_architecture.py
- [[Both direct mode and MCP mode must expose 'search_policy_documents'.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[Both direct tool and MCP tool must accept 'query' and 'top_k' parameters.]] - rationale - tests/unit_tests/test_agent_architecture.py
- [[TestDirectAndMCPParity]] - code - tests/unit_tests/test_agent_architecture.py
- [[Verify tool signatures and behavioral consistency between Direct and MCP modes.]] - rationale - tests/unit_tests/test_agent_architecture.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDirectAndMCPParity
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_agentmodels.py]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[TestDirectAndMCPParity]] - degree 4, connects to 1 community
- [[dot-test_direct_and_mcp_input_schema_equivalence()]] - degree 3, connects to 1 community
- [[dot-test_direct_and_mcp_tool_name_parity()]] - degree 3, connects to 1 community