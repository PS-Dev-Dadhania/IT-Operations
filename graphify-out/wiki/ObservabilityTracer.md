# ObservabilityTracer

> 83 nodes · cohesion 0.05

## Key Concepts

- **ObservabilityTracer** (25 connections) — `src/mcp_rag_agent/observability/tracer.py`
- **observability/__init__.py** (24 connections) — `src/mcp_rag_agent/observability/__init__.py`
- **get_request_id()** (22 connections) — `src/mcp_rag_agent/observability/context.py`
- **tracer.py** (18 connections) — `src/mcp_rag_agent/observability/tracer.py`
- **get_current_tracer()** (16 connections) — `src/mcp_rag_agent/observability/context.py`
- **context.py** (15 connections) — `src/mcp_rag_agent/observability/context.py`
- **observability/models.py** (14 connections) — `src/mcp_rag_agent/observability/models.py`
- **set_request_context()** (13 connections) — `src/mcp_rag_agent/observability/context.py`
- **ErrorRecord** (12 connections) — `src/mcp_rag_agent/observability/models.py`
- **TraceSpan** (12 connections) — `src/mcp_rag_agent/observability/models.py`
- **get_thread_id()** (11 connections) — `src/mcp_rag_agent/observability/context.py`
- **ErrorCategory** (11 connections) — `src/mcp_rag_agent/observability/models.py`
- **TokenUsage** (10 connections) — `src/mcp_rag_agent/observability/models.py`
- **get_correlation_ids()** (8 connections) — `src/mcp_rag_agent/observability/context.py`
- **get_user_id()** (8 connections) — `src/mcp_rag_agent/observability/context.py`
- **.text_search()** (7 connections) — `src/mcp_rag_agent/mongodb/client.py`
- **.vector_search()** (7 connections) — `src/mcp_rag_agent/mongodb/client.py`
- **Any** (7 connections)
- **RequestTrace** (7 connections) — `src/mcp_rag_agent/observability/models.py`
- **.record_error()** (7 connections) — `src/mcp_rag_agent/observability/tracer.py`
- **.test_set_request_context_sync()** (7 connections) — `tests/unit_tests/test_observability.py`
- **.async_span()** (6 connections) — `src/mcp_rag_agent/observability/tracer.py`
- **.record_llm_call()** (6 connections) — `src/mcp_rag_agent/observability/tracer.py`
- **.test_default_context_is_empty()** (6 connections) — `tests/unit_tests/test_observability.py`
- **.test_connect_records_database_error_on_failure()** (6 connections) — `tests/unit_tests/test_observability.py`
- *... and 58 more nodes in this community*

## Relationships

- [typing](typing.md) (28 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (13 shared connections)
- [agent/models.py](agent-models.py.md) (12 shared connections)
- [.run](run.md) (10 shared connections)
- [middleware.py](middleware.py.md) (4 shared connections)
- [TestObservabilityTracer](TestObservabilityTracer.md) (4 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (3 shared connections)
- [test_observability.py](test_observability.py.md) (3 shared connections)
- [SecuritySubject](SecuritySubject.md) (2 shared connections)
- [Config](Config.md) (2 shared connections)
- [datetime](datetime.md) (1 shared connections)
- [pydantic](pydantic.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/core/log_setup.py`
- `src/mcp_rag_agent/mongodb/client.py`
- `src/mcp_rag_agent/observability/__init__.py`
- `src/mcp_rag_agent/observability/context.py`
- `src/mcp_rag_agent/observability/models.py`
- `src/mcp_rag_agent/observability/tracer.py`
- `tests/unit_tests/test_observability.py`

## Audit Trail

- EXTRACTED: 208 (85%)
- INFERRED: 38 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*