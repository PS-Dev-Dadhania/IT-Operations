# TestEmbeddingGenerator

> 13 nodes · cohesion 0.18

## Key Concepts

- **TestEmbeddingGenerator** (9 connections) — `tests/unit_tests/test_embedding_generator.py`
- **.test_generate_batch_empty_list()** (4 connections) — `tests/unit_tests/test_embedding_generator.py`
- **.test_generate_calls_openai_with_correct_parameters()** (4 connections) — `tests/unit_tests/test_embedding_generator.py`
- **.test_generate_raises_when_api_key_missing()** (4 connections) — `tests/unit_tests/test_embedding_generator.py`
- **asyncio** (3 connections)
- **.test_dimensions_defaults_to_config_dimension()** (3 connections) — `tests/unit_tests/test_embedding_generator.py`
- **.test_explicit_dimensions_overrides_default()** (3 connections) — `tests/unit_tests/test_embedding_generator.py`
- **Test suite for EmbeddingGenerator.** (1 connections) — `tests/unit_tests/test_embedding_generator.py`
- **Verify dimensions defaults to config.embedding_dimension (256) when not…** (1 connections) — `tests/unit_tests/test_embedding_generator.py`
- **Verify passing explicit dimensions overrides the config default.** (1 connections) — `tests/unit_tests/test_embedding_generator.py`
- **Verify generate raises ConfigurationError when API key is missing.** (1 connections) — `tests/unit_tests/test_embedding_generator.py`
- **Verify generate_batch returns empty list for empty inputs without calling API.** (1 connections) — `tests/unit_tests/test_embedding_generator.py`
- **Verify generate calls OpenAI embeddings.create with correct model and…** (1 connections) — `tests/unit_tests/test_embedding_generator.py`

## Relationships

- [typing](typing.md) (6 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [ConfigurationError](ConfigurationError.md) (1 shared connections)

## Source Files

- `tests/unit_tests/test_embedding_generator.py`

## Audit Trail

- EXTRACTED: 15 (68%)
- INFERRED: 7 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*