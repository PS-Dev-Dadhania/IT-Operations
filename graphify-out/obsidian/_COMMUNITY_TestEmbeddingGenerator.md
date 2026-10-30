---
type: community
cohesion: 0.18
members: 13
---

# TestEmbeddingGenerator

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-test_dimensions_defaults_to_config_dimension()]] - code - tests/unit_tests/test_embedding_generator.py
- [[dot-test_explicit_dimensions_overrides_default()]] - code - tests/unit_tests/test_embedding_generator.py
- [[dot-test_generate_batch_empty_list()]] - code - tests/unit_tests/test_embedding_generator.py
- [[dot-test_generate_calls_openai_with_correct_parameters()]] - code - tests/unit_tests/test_embedding_generator.py
- [[dot-test_generate_raises_when_api_key_missing()]] - code - tests/unit_tests/test_embedding_generator.py
- [[Test suite for EmbeddingGenerator.]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[TestEmbeddingGenerator]] - code - tests/unit_tests/test_embedding_generator.py
- [[Verify dimensions defaults to config.embedding_dimension (256) when not…]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[Verify generate calls OpenAI embeddings.create with correct model and…]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[Verify generate raises ConfigurationError when API key is missing.]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[Verify generate_batch returns empty list for empty inputs without calling API.]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[Verify passing explicit dimensions overrides the config default.]] - rationale - tests/unit_tests/test_embedding_generator.py
- [[asyncio_17]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEmbeddingGenerator
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_typing]]
- 1 edge to [[_COMMUNITY_ConfigurationError]]
- 1 edge to [[_COMMUNITY_unittest_mock]]

## Top bridge nodes
- [[TestEmbeddingGenerator]] - degree 9, connects to 3 communities
- [[dot-test_generate_batch_empty_list()]] - degree 4, connects to 1 community
- [[dot-test_generate_calls_openai_with_correct_parameters()]] - degree 4, connects to 1 community
- [[dot-test_generate_raises_when_api_key_missing()]] - degree 4, connects to 1 community
- [[dot-test_dimensions_defaults_to_config_dimension()]] - degree 3, connects to 1 community