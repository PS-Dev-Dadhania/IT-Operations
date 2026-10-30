# TestObservabilityTracer

> 10 nodes · cohesion 0.20

## Key Concepts

- **TestObservabilityTracer** (6 connections) — `tests/unit_tests/test_observability.py`
- **.test_tracer_async_span()** (4 connections) — `tests/unit_tests/test_observability.py`
- **.test_calculate_cost_usd()** (3 connections) — `tests/unit_tests/test_observability.py`
- **.test_tracer_records_tool_retrieval_and_llm()** (3 connections) — `tests/unit_tests/test_observability.py`
- **.test_tracer_sync_and_async_spans()** (3 connections) — `tests/unit_tests/test_observability.py`
- **Test span tracking, latency measurement, token calculations, and finish status.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify model rate cards calculate accurate USD pricing.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify synchronous and asynchronous spans record duration and attributes.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify async span tracks duration and handles errors.** (1 connections) — `tests/unit_tests/test_observability.py`
- **Verify tracer records operational lifecycle metrics and finishes cleanly.** (1 connections) — `tests/unit_tests/test_observability.py`

## Relationships

- [ObservabilityTracer](ObservabilityTracer.md) (4 shared connections)
- [test_observability.py](test_observability.py.md) (1 shared connections)
- [RAGAgentRunner](RAGAgentRunner.md) (1 shared connections)

## Source Files

- `tests/unit_tests/test_observability.py`

## Audit Trail

- EXTRACTED: 11 (73%)
- INFERRED: 4 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*