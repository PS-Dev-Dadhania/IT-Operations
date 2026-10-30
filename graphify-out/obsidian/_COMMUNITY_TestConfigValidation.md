---
type: community
cohesion: 0.12
members: 16
---

# TestConfigValidation

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-test_default_embedding_dimension()]] - code - tests/unit_tests/test_config.py
- [[dot-test_import_without_credentials_does_not_raise_keyerror()]] - code - tests/unit_tests/test_config.py
- [[dot-test_session_memory_config_defaults()]] - code - tests/unit_tests/test_config.py
- [[dot-test_validate_all_passes_when_configured()]] - code - tests/unit_tests/test_config.py
- [[dot-test_validate_database_config_missing_db_name()]] - code - tests/unit_tests/test_config.py
- [[dot-test_validate_database_config_missing_url()]] - code - tests/unit_tests/test_config.py
- [[dot-test_validate_llm_config_missing_api_key()]] - code - tests/unit_tests/test_config.py
- [[Test suite for Config validation logic.]] - rationale - tests/unit_tests/test_config.py
- [[TestConfigValidation]] - code - tests/unit_tests/test_config.py
- [[Verify Config can be instantiated without crashing on KeyError.]] - rationale - tests/unit_tests/test_config.py
- [[Verify default embedding dimension is 256.]] - rationale - tests/unit_tests/test_config.py
- [[Verify session memory configuration defaults.]] - rationale - tests/unit_tests/test_config.py
- [[Verify validate_all succeeds when all required fields are present.]] - rationale - tests/unit_tests/test_config.py
- [[Verify validate_database_config raises ConfigurationError when db_name is…]] - rationale - tests/unit_tests/test_config.py
- [[Verify validate_database_config raises ConfigurationError when db_url is…]] - rationale - tests/unit_tests/test_config.py
- [[Verify validate_llm_config raises ConfigurationError when model_api_key is…]] - rationale - tests/unit_tests/test_config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestConfigValidation
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Config]]
- 1 edge to [[_COMMUNITY_ConfigurationError]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[TestConfigValidation]] - degree 11, connects to 3 communities
- [[dot-test_default_embedding_dimension()]] - degree 3, connects to 1 community
- [[dot-test_import_without_credentials_does_not_raise_keyerror()]] - degree 3, connects to 1 community
- [[dot-test_session_memory_config_defaults()]] - degree 3, connects to 1 community
- [[dot-test_validate_all_passes_when_configured()]] - degree 3, connects to 1 community