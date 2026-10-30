---
source_file: "src/mcp_rag_agent/agent/models.py"
type: "code"
community: "RetrievedChunkOutput"
location: "L26"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RetrievedChunkOutput
---

# RetrievedChunkOutput

## Connections
- [[dot-_extract_retrieved_chunks()]] - `references` [EXTRACTED]
- [[dot-filter_context()]] - `references` [EXTRACTED]
- [[dot-test_context_truncation_enforces_limit()]] - `calls` [INFERRED]
- [[dot-test_detects_conflicting_day_allocations()]] - `calls` [INFERRED]
- [[dot-test_evaluate_output_grounding_flags_ungrounded_content()]] - `calls` [INFERRED]
- [[dot-test_evaluate_output_grounding_rejects_answer_with_fabricated_citation()]] - `calls` [INFERRED]
- [[dot-test_evaluate_retrieval_context_records_conflict_warning()]] - `calls` [INFERRED]
- [[dot-test_evaluate_retrieval_context_sandboxes_chunks()]] - `calls` [INFERRED]
- [[dot-test_retrieval_below_confidence_threshold_triggers_violation()]] - `calls` [INFERRED]
- [[dot-test_validate_citations_detects_fabricated_sources()]] - `calls` [INFERRED]
- [[dot-validate_output()]] - `references` [EXTRACTED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[RAGAgentRunner]] - `uses` [INFERRED]
- [[RAGGuardrails]] - `uses` [INFERRED]
- [[TestAnswerGroundingValidation]] - `uses` [INFERRED]
- [[TestCitationValidation]] - `uses` [INFERRED]
- [[TestConflictingDocumentsDetection]] - `uses` [INFERRED]
- [[TestDocumentPromptInjectionDefense]] - `uses` [INFERRED]
- [[TestLowSimilarityCutoff]] - `uses` [INFERRED]
- [[TestMaxContextLimits]] - `uses` [INFERRED]
- [[Typed representation of a single retrieved chunk for agent context.]] - `rationale_for` [EXTRACTED]
- [[agent__init__.py]] - `imports` [EXTRACTED]
- [[agentmodels.py]] - `contains` [EXTRACTED]
- [[check_conflicting_documents()]] - `uses` [INFERRED]
- [[context_guardrails.py]] - `imports` [EXTRACTED]
- [[evaluate_output_grounding()]] - `uses` [INFERRED]
- [[evaluate_retrieval_context()]] - `uses` [INFERRED]
- [[manager.py]] - `imports` [EXTRACTED]
- [[mcp_servertools.py]] - `imports` [EXTRACTED]
- [[output_guardrails.py]] - `imports` [EXTRACTED]
- [[runner.py]] - `imports` [EXTRACTED]
- [[search_policy_documents_typed()]] - `calls` [EXTRACTED]
- [[test_chat_endpoint_with_structured_sources()]] - `uses` [INFERRED]
- [[test_retrieval_document_access_filtering()]] - `uses` [INFERRED]
- [[validate_citations()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/RetrievedChunkOutput