# middleware.py

> 12 nodes · cohesion 0.17

## Key Concepts

- **middleware.py** (12 connections) — `src/mcp_rag_agent/api/middleware.py`
- **time** (9 connections)
- **CorrelationIdMiddleware** (6 connections) — `src/mcp_rag_agent/api/middleware.py`
- **.dispatch()** (4 connections) — `src/mcp_rag_agent/api/middleware.py`
- **BaseHTTPMiddleware** (1 connections)
- **Request** (1 connections)
- **Response** (1 connections)
- **HTTP middleware for correlation IDs, latency measurement, and request logging.** (1 connections) — `src/mcp_rag_agent/api/middleware.py`
- **Intercepts requests to extract or assign X-Request-ID and tracks response…** (1 connections) — `src/mcp_rag_agent/api/middleware.py`
- **starlette_middleware_base** (1 connections)
- **starlette_requests** (1 connections)
- **starlette_responses** (1 connections)

## Relationships

- [ObservabilityTracer](ObservabilityTracer.md) (4 shared connections)
- [typing](typing.md) (3 shared connections)
- [agent/models.py](agent-models.py.md) (3 shared connections)
- [benchmark_retrieval.py](benchmark_retrieval.py.md) (2 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (1 shared connections)
- [test_api.py](test_api.py.md) (1 shared connections)
- [eval_runner.py](eval_runner.py.md) (1 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (1 shared connections)
- [retrieval/pipeline.py](retrieval-pipeline.py.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/api/middleware.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*