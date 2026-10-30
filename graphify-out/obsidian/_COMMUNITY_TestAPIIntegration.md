---
type: community
cohesion: 0.14
members: 16
---

# TestAPIIntegration

**Cohesion:** 0.14 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-app_client()]] - code - tests/integration_tests/test_api_integration.py
- [[dot-test_correlation_id_header_injection()]] - code - tests/integration_tests/test_api_integration.py
- [[dot-test_health_liveness_probe()]] - code - tests/integration_tests/test_api_integration.py
- [[dot-test_root_endpoint_metadata()]] - code - tests/integration_tests/test_api_integration.py
- [[Create test client with test configuration.]] - rationale - tests/integration_tests/test_api_integration.py
- [[Integration test suite for FastAPI application endpoints.]] - rationale - tests/integration_tests/test_api_integration.py
- [[Integration tests for FastAPI application layer.]] - rationale - tests/integration_tests/test_api_integration.py
- [[TestAPIIntegration]] - code - tests/integration_tests/test_api_integration.py
- [[TestClient]] - code
- [[Verify API root endpoint exposes expected navigation links.]] - rationale - tests/integration_tests/test_api_integration.py
- [[Verify X-Request-ID header is always injected and propagated.]] - rationale - tests/integration_tests/test_api_integration.py
- [[Verify liveness probe returns healthy status.]] - rationale - tests/integration_tests/test_api_integration.py
- [[fixture_9]] - code
- [[mcp_rag_agent_api_app]] - concept
- [[starlette_testclient]] - concept
- [[test_api_integration.py]] - code - tests/integration_tests/test_api_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAPIIntegration
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_test_api.py]]
- 1 edge to [[_COMMUNITY_pytest]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[test_api_integration.py]] - degree 6, connects to 2 communities
- [[dot-app_client()]] - degree 5, connects to 2 communities
- [[TestAPIIntegration]] - degree 7, connects to 1 community