# TestConfigValidation

> 16 nodes · cohesion 0.12

## Key Concepts

- **TestConfigValidation** (11 connections) — `tests/unit_tests/test_config.py`
- **.test_default_embedding_dimension()** (3 connections) — `tests/unit_tests/test_config.py`
- **.test_import_without_credentials_does_not_raise_keyerror()** (3 connections) — `tests/unit_tests/test_config.py`
- **.test_session_memory_config_defaults()** (3 connections) — `tests/unit_tests/test_config.py`
- **.test_validate_all_passes_when_configured()** (3 connections) — `tests/unit_tests/test_config.py`
- **.test_validate_database_config_missing_db_name()** (3 connections) — `tests/unit_tests/test_config.py`
- **.test_validate_database_config_missing_url()** (3 connections) — `tests/unit_tests/test_config.py`
- **.test_validate_llm_config_missing_api_key()** (3 connections) — `tests/unit_tests/test_config.py`
- **Test suite for Config validation logic.** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify Config can be instantiated without crashing on KeyError.** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify default embedding dimension is 256.** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify validate_database_config raises ConfigurationError when db_url is…** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify validate_database_config raises ConfigurationError when db_name is…** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify validate_llm_config raises ConfigurationError when model_api_key is…** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify validate_all succeeds when all required fields are present.** (1 connections) — `tests/unit_tests/test_config.py`
- **Verify session memory configuration defaults.** (1 connections) — `tests/unit_tests/test_config.py`

## Relationships

- [Config](Config.md) (8 shared connections)
- [unittest_mock](unittest_mock.md) (1 shared connections)
- [ConfigurationError](ConfigurationError.md) (1 shared connections)

## Source Files

- `tests/unit_tests/test_config.py`

## Audit Trail

- EXTRACTED: 16 (64%)
- INFERRED: 9 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*