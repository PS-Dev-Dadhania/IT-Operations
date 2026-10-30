# operational.py

> 19 nodes · cohesion 0.13

## Key Concepts

- **operational.py** (11 connections) — `evaluation/metrics/operational.py`
- **extract_operational_metrics()** (10 connections) — `evaluation/metrics/operational.py`
- **compute_cost_usd()** (6 connections) — `evaluation/metrics/operational.py`
- **estimate_tokens()** (6 connections) — `evaluation/metrics/operational.py`
- **OperationalMetrics** (5 connections) — `evaluation/metrics/operational.py`
- **TestOperationalMetrics** (5 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_compute_cost_usd()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_estimate_tokens()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **.test_extract_operational_metrics()** (3 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **BaseModel** (1 connections)
- **Operational metrics: Retrieval latency, model generation latency, token counts,…** (1 connections) — `evaluation/metrics/operational.py`
- **Container tracking operational latency, throughput, token counts, and financial…** (1 connections) — `evaluation/metrics/operational.py`
- **Accurately count or estimate tokens for a given string.** (1 connections) — `evaluation/metrics/operational.py`
- **Calculate monetary cost in USD based on official token pricing tables. Args:…** (1 connections) — `evaluation/metrics/operational.py`
- **Assemble complete operational metrics from execution trace. Args: query: User…** (1 connections) — `evaluation/metrics/operational.py`
- **Verify token estimation, cost calculation, and latency aggregation.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Token estimation provides reasonable positive counts.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Cost calculation accurately multiplies token usage by rate cards.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`
- **Operational metrics assembler captures latencies and calculates cost.** (1 connections) — `tests/unit_tests/test_evaluation_framework.py`

## Relationships

- [metrics/__init__.py](metrics-__init__.py.md) (5 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (5 shared connections)
- [eval_runner.py](eval_runner.py.md) (3 shared connections)
- [typing](typing.md) (2 shared connections)
- [pydantic](pydantic.md) (1 shared connections)

## Source Files

- `evaluation/metrics/operational.py`
- `tests/unit_tests/test_evaluation_framework.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*