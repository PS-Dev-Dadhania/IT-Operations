# AnswerGenerator

> 57 nodes · cohesion 0.05

## Key Concepts

- **AnswerGenerator** (18 connections) — `evaluation/answer_generator.py`
- **answer_generator.py** (12 connections) — `evaluation/answer_generator.py`
- **MetricsEvaluator** (9 connections) — `evaluation/metrics_evaluator.py`
- **.generate_answer_for_question()** (7 connections) — `evaluation/answer_generator.py`
- **main.py** (7 connections) — `evaluation/main.py`
- **test_answer_generator.py** (7 connections) — `tests/unit_tests/test_answer_generator.py`
- **.test_get_agent_initializes_lazily()** (7 connections) — `tests/unit_tests/test_answer_generator.py`
- **.get_agent()** (6 connections) — `evaluation/answer_generator.py`
- **.compute_all_metrics()** (6 connections) — `evaluation/metrics_evaluator.py`
- **.compute_metrics_for_row()** (6 connections) — `evaluation/metrics_evaluator.py`
- **TestAnswerGenerator** (6 connections) — `tests/unit_tests/test_answer_generator.py`
- **.test_evaluation_questions_receive_isolated_threads()** (6 connections) — `tests/unit_tests/test_session_memory.py`
- **.agent()** (5 connections) — `evaluation/answer_generator.py`
- **.generate_all_answers()** (5 connections) — `evaluation/answer_generator.py`
- **.test_generate_answer_for_question_calls_agent()** (5 connections) — `tests/unit_tests/test_answer_generator.py`
- **.__init__()** (4 connections) — `evaluation/answer_generator.py`
- **.load_test_cases()** (4 connections) — `evaluation/answer_generator.py`
- **.save_incremental()** (4 connections) — `evaluation/answer_generator.py`
- **Any** (4 connections)
- **main()** (4 connections) — `evaluation/main.py`
- **.__init__()** (4 connections) — `evaluation/metrics_evaluator.py`
- **.load_answers()** (4 connections) — `evaluation/metrics_evaluator.py`
- **.save_incremental()** (4 connections) — `evaluation/metrics_evaluator.py`
- **.save_summary_statistics()** (4 connections) — `evaluation/metrics_evaluator.py`
- **.test_init_without_agent_does_not_initialize()** (4 connections) — `tests/unit_tests/test_answer_generator.py`
- *... and 32 more nodes in this community*

## Relationships

- [unittest_mock](unittest_mock.md) (4 shared connections)
- [typing](typing.md) (3 shared connections)
- [test_evaluation_framework.py](test_evaluation_framework.py.md) (3 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [Config](Config.md) (2 shared connections)
- [metrics_evaluator.py](metrics_evaluator.py.md) (2 shared connections)
- [metrics/__init__.py](metrics-__init__.py.md) (2 shared connections)
- [test_it_evaluation.py](test_it_evaluation.py.md) (1 shared connections)
- [runbooks/__init__.py](runbooks-__init__.py.md) (1 shared connections)
- [agent/models.py](agent-models.py.md) (1 shared connections)
- [pytest](pytest.md) (1 shared connections)
- [tickets/models.py](tickets-models.py.md) (1 shared connections)

## Source Files

- `evaluation/answer_generator.py`
- `evaluation/main.py`
- `evaluation/metrics_evaluator.py`
- `tests/unit_tests/test_answer_generator.py`
- `tests/unit_tests/test_session_memory.py`

## Audit Trail

- EXTRACTED: 93 (88%)
- INFERRED: 13 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*