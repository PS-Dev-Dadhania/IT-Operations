---
type: community
cohesion: 0.20
members: 10
---

# TestObservabilityTracer

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-test_calculate_cost_usd()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_tracer_async_span()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_tracer_records_tool_retrieval_and_llm()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_tracer_sync_and_async_spans()]] - code - tests/unit_tests/test_observability.py
- [[Test span tracking, latency measurement, token calculations, and finish status.]] - rationale - tests/unit_tests/test_observability.py
- [[TestObservabilityTracer]] - code - tests/unit_tests/test_observability.py
- [[Verify async span tracks duration and handles errors.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify model rate cards calculate accurate USD pricing.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify synchronous and asynchronous spans record duration and attributes.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify tracer records operational lifecycle metrics and finishes cleanly.]] - rationale - tests/unit_tests/test_observability.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestObservabilityTracer
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ObservabilityTracer]]
- 1 edge to [[_COMMUNITY_test_observability.py]]
- 1 edge to [[_COMMUNITY_RAGAgentRunner]]

## Top bridge nodes
- [[dot-test_tracer_async_span()]] - degree 4, connects to 2 communities
- [[TestObservabilityTracer]] - degree 6, connects to 1 community
- [[dot-test_calculate_cost_usd()]] - degree 3, connects to 1 community
- [[dot-test_tracer_records_tool_retrieval_and_llm()]] - degree 3, connects to 1 community
- [[dot-test_tracer_sync_and_async_spans()]] - degree 3, connects to 1 community