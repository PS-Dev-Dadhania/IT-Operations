---
source_file: "src/mcp_rag_agent/guardrails/context_guardrails.py"
type: "rationale"
community: "RetrievedChunkOutput"
location: "L31"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/RetrievedChunkOutput
---

# Scan and neutralize indirect prompt injections inside retrieved document text.

## Connections
- [[sanitize_document_text()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/RetrievedChunkOutput