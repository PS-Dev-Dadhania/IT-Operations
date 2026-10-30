---
type: community
cohesion: 0.13
members: 19
---

# operational.py

**Cohesion:** 0.13 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-test_compute_cost_usd()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_estimate_tokens()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[dot-test_extract_operational_metrics()]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Accurately count or estimate tokens for a given string.]] - rationale - evaluation/metrics/operational.py
- [[Assemble complete operational metrics from execution trace. Args query User…]] - rationale - evaluation/metrics/operational.py
- [[BaseModel_20]] - code
- [[Calculate monetary cost in USD based on official token pricing tables. Args…]] - rationale - evaluation/metrics/operational.py
- [[Container tracking operational latency, throughput, token counts, and financial…]] - rationale - evaluation/metrics/operational.py
- [[Cost calculation accurately multiplies token usage by rate cards.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Operational metrics assembler captures latencies and calculates cost.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Operational metrics Retrieval latency, model generation latency, token counts,…]] - rationale - evaluation/metrics/operational.py
- [[OperationalMetrics]] - code - evaluation/metrics/operational.py
- [[TestOperationalMetrics]] - code - tests/unit_tests/test_evaluation_framework.py
- [[Token estimation provides reasonable positive counts.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[Verify token estimation, cost calculation, and latency aggregation.]] - rationale - tests/unit_tests/test_evaluation_framework.py
- [[compute_cost_usd()]] - code - evaluation/metrics/operational.py
- [[estimate_tokens()]] - code - evaluation/metrics/operational.py
- [[extract_operational_metrics()]] - code - evaluation/metrics/operational.py
- [[operational.py]] - code - evaluation/metrics/operational.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/operationalpy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_metrics__init__.py]]
- 5 edges to [[_COMMUNITY_test_evaluation_framework.py]]
- 3 edges to [[_COMMUNITY_eval_runner.py]]
- 2 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[operational.py]] - degree 11, connects to 5 communities
- [[extract_operational_metrics()]] - degree 10, connects to 3 communities
- [[compute_cost_usd()]] - degree 6, connects to 2 communities
- [[estimate_tokens()]] - degree 6, connects to 2 communities
- [[OperationalMetrics]] - degree 5, connects to 1 community