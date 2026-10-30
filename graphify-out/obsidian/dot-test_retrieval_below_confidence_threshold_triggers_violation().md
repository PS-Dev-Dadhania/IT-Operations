---
source_file: "tests/unit_tests/test_guardrails_adversarial.py"
type: "code"
community: "RetrievedChunkOutput"
location: "L341"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/RetrievedChunkOutput
---

# .test_retrieval_below_confidence_threshold_triggers_violation()

## Connections
- [[Chunk with fusion score below threshold (0.015) is flagged as LOW_CONFIDENCE.]] - `rationale_for` [EXTRACTED]
- [[RetrievedChunkOutput]] - `calls` [INFERRED]
- [[TestLowSimilarityCutoff]] - `method` [EXTRACTED]
- [[evaluate_retrieval_context()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/RetrievedChunkOutput