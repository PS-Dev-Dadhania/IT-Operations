---
source_file: "evaluation/runners/eval_runner.py"
type: "code"
community: "eval_runner.py"
location: "L300"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/eval_runnerpy
---

# .evaluate_item_retrieval_only()

## Connections
- [[dot-_evaluate_it_workflow_offline()]] - `calls` [EXTRACTED]
- [[dot-run_evaluation()]] - `calls` [EXTRACTED]
- [[BenchmarkItem]] - `references` [EXTRACTED]
- [[EvalRunItemResult]] - `calls` [EXTRACTED]
- [[Evaluate retrieval performance without executing LLM generation.]] - `rationale_for` [EXTRACTED]
- [[ITBenchmarkItem]] - `references` [EXTRACTED]
- [[ProductionEvalRunner]] - `method` [EXTRACTED]
- [[SearchDocumentsInput]] - `calls` [INFERRED]
- [[compute_retrieval_metrics()]] - `calls` [EXTRACTED]
- [[search_policy_documents_typed()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/eval_runnerpy