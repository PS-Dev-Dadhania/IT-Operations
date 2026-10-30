# TestAPIIntegration

> 16 nodes · cohesion 0.14

## Key Concepts

- **TestAPIIntegration** (7 connections) — `tests/integration_tests/test_api_integration.py`
- **test_api_integration.py** (6 connections) — `tests/integration_tests/test_api_integration.py`
- **.app_client()** (5 connections) — `tests/integration_tests/test_api_integration.py`
- **TestClient** (3 connections)
- **.test_correlation_id_header_injection()** (3 connections) — `tests/integration_tests/test_api_integration.py`
- **.test_health_liveness_probe()** (3 connections) — `tests/integration_tests/test_api_integration.py`
- **.test_root_endpoint_metadata()** (3 connections) — `tests/integration_tests/test_api_integration.py`
- **mcp_rag_agent_api_app** (1 connections)
- **starlette_testclient** (1 connections)
- **fixture** (1 connections)
- **Integration tests for FastAPI application layer.** (1 connections) — `tests/integration_tests/test_api_integration.py`
- **Integration test suite for FastAPI application endpoints.** (1 connections) — `tests/integration_tests/test_api_integration.py`
- **Create test client with test configuration.** (1 connections) — `tests/integration_tests/test_api_integration.py`
- **Verify API root endpoint exposes expected navigation links.** (1 connections) — `tests/integration_tests/test_api_integration.py`
- **Verify liveness probe returns healthy status.** (1 connections) — `tests/integration_tests/test_api_integration.py`
- **Verify X-Request-ID header is always injected and propagated.** (1 connections) — `tests/integration_tests/test_api_integration.py`

## Relationships

- [Config](Config.md) (2 shared connections)
- [pytest](pytest.md) (1 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [test_api.py](test_api.py.md) (1 shared connections)

## Source Files

- `tests/integration_tests/test_api_integration.py`

## Audit Trail

- EXTRACTED: 19 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*