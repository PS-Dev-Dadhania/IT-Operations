---
type: community
cohesion: 0.17
members: 12
---

# middleware.py

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-dispatch()]] - code - src/mcp_rag_agent/api/middleware.py
- [[BaseHTTPMiddleware]] - code
- [[CorrelationIdMiddleware]] - code - src/mcp_rag_agent/api/middleware.py
- [[HTTP middleware for correlation IDs, latency measurement, and request logging.]] - rationale - src/mcp_rag_agent/api/middleware.py
- [[Intercepts requests to extract or assign X-Request-ID and tracks response…]] - rationale - src/mcp_rag_agent/api/middleware.py
- [[Request_2]] - code
- [[Response_2]] - code
- [[middleware.py]] - code - src/mcp_rag_agent/api/middleware.py
- [[starlette_middleware_base]] - concept
- [[starlette_requests]] - concept
- [[starlette_responses]] - concept
- [[time]] - concept

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/middlewarepy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ObservabilityTracer]]
- 3 edges to [[_COMMUNITY_agentmodels.py]]
- 3 edges to [[_COMMUNITY_typing]]
- 2 edges to [[_COMMUNITY_benchmark_retrieval.py]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_mcp_servertools.py]]
- 1 edge to [[_COMMUNITY_eval_runner.py]]
- 1 edge to [[_COMMUNITY_retrievalpipeline.py]]
- 1 edge to [[_COMMUNITY_runbooks__init__.py]]

## Top bridge nodes
- [[time]] - degree 9, connects to 7 communities
- [[middleware.py]] - degree 12, connects to 4 communities
- [[CorrelationIdMiddleware]] - degree 6, connects to 2 communities
- [[dot-dispatch()]] - degree 4, connects to 1 community