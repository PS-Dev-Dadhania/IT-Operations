---
source_file: "src/mcp_rag_agent/mcp_server/tools.py"
type: "code"
community: "ConfigurationError"
location: "L96"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ConfigurationError
---

# get_hybrid_search()

## Connections
- [[dot-test_get_hybrid_search_raises_on_unconfigured_credentials()]] - `calls` [INFERRED]
- [[dot-test_set_hybrid_search_mock()]] - `calls` [INFERRED]
- [[Config]] - `uses` [INFERRED]
- [[EmbeddingGenerator]] - `calls` [EXTRACTED]
- [[Get or lazily initialize the shared HybridSearch engine (legacy compatibility).]] - `rationale_for` [EXTRACTED]
- [[HybridSearch]] - `calls` [EXTRACTED]
- [[get_mongo_client()]] - `calls` [EXTRACTED]
- [[mcp_servertools.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ConfigurationError