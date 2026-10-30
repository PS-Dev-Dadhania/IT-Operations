# Graph Report - L2  (2026-10-21)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 2674 nodes · 6487 edges · 108 communities (71 shown, 37 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 1145 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d011fe78`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- typing
- mcp_server/tools.py
- ObservabilityTracer
- DeviceRecord
- AnswerGenerator
- Config
- test_it_evaluation.py
- agent/models.py
- metrics/__init__.py
- SecuritySubject
- test_evaluation_framework.py
- TicketRecord
- TestMongoDBClient
- test_api.py
- test_admin_api.py
- Role
- eval_runner.py
- unittest_mock
- tickets/models.py
- ConversationService
- ViolationType
- Runbook
- runbooks/__init__.py
- IncidentRecord
- approval.py
- test_guardrails_adversarial.py
- RAGAgentRunner
- ServiceStatusRecord
- RetrievedChunkOutput
- app.js
- test_mcp_it_tools.py
- ingestion/__init__.py
- retrieval/pipeline.py
- mcp_rag_agent/it_support/__init__.py
- retrieval.py
- ServiceStatusChecker
- audit.py
- ParsedDocument
- test_ingestion_pipeline.py
- test_runbooks.py
- get_checkpointer
- AdvancedRetriever
- ChatService
- ConfigurationError
- TestTypedToolInterface
- test_approval.py
- dependencies.py
- QueryPreprocessor
- .run
- AdminAPIService
- RunbookExecutor
- datetime
- pydantic
- DocumentIngestionPipeline
- UserNotFoundError
- RiskLevel
- RAGGuardrails
- RetrievedChunk
- operational.py
- index_documents_from_folder
- create_runbook_subgraph
- ITCategory
- users/store.py
- setup_services
- intent.py
- TestAPIIntegration
- test_incidents.py
- TestConfigValidation
- TicketService
- IncidentStore
- TicketStore
- test_tool_authorization_success_emits_audit_log
- benchmark_retrieval.py
- TestMCPIntegration
- pytest
- get_admin_evaluation
- StepExecutionResult
- UserContextRecord
- TestEmbeddingGenerator
- middleware.py
- DocumentCleaner
- MarkdownParser
- UserService
- test_mongodb_integration.py
- metrics_evaluator.py
- test_observability.py
- TestStructuredLoggingAndRedaction
- TestMongoDBLiveIntegration
- compute_it_metrics
- TestObservabilityTracer
- TestDocumentIngestion
- MemoryIncidentStore
- TestAnswerGroundingValidation
- TestDirectAndMCPParity
- delete_conversation
- start.sh

## God Nodes (most connected - your core abstractions)
1. `Config` - 80 edges
2. `TicketRecord` - 79 edges
3. `MongoDBClient` - 72 edges
4. `RAGAgentRunner` - 57 edges
5. `Role` - 51 edges
6. `ITCategory` - 51 edges
7. `SecuritySubject` - 49 edges
8. `IncidentRecord` - 44 edges
9. `DeviceRecord` - 43 edges
10. `TicketService` - 38 edges

## Surprising Connections (you probably didn't know these)
- `test_it_operations_tools_instantiation()` --calls--> `create_it_operations_tools()`  [INFERRED]
  tests/unit_tests/it_support/test_it_agent_flows.py → src/mcp_rag_agent/it_support/tools.py
- `TestStructuredLoggingAndRedaction` --uses--> `JSONLogFormatter`  [INFERRED]
  tests/unit_tests/test_observability.py → src/mcp_rag_agent/core/log_setup.py
- `TestEmbeddingGenerator` --uses--> `EmbeddingGenerator`  [INFERRED]
  tests/unit_tests/test_embedding_generator.py → src/mcp_rag_agent/embeddings/embedding_generator.py
- `seed_it_operations_data()` --uses--> `MongoDBClient`  [INFERRED]
  scripts/seed_it_operations_data.py → src/mcp_rag_agent/mongodb/client.py
- `TestMongoDBLiveIntegration` --uses--> `MongoDBClient`  [INFERRED]
  tests/integration_tests/test_mongodb_integration.py → src/mcp_rag_agent/mongodb/client.py

## Import Cycles
- None detected.

## Communities (108 total, 37 thin omitted)

### Community 0 - "typing"
Cohesion: 0.03
Nodes (12): CorrelationIdFilter, JSONLogFormatter, setup_logging(), TextLogFormatter, EmbeddingGenerator, HybridSearch, main(), main() (+4 more)

### Community 1 - "mcp_server/tools.py"
Cohesion: 0.04
Nodes (51): CheckServiceStatusInput, CheckServiceStatusOutput, CreateTicketToolInput, CreateTicketToolOutput, GetDeviceInfoInput, GetDeviceInfoOutput, GetUserContextInput, GetUserContextOutput (+43 more)

### Community 2 - "ObservabilityTracer"
Cohesion: 0.05
Nodes (16): get_correlation_ids(), get_current_tracer(), get_request_id(), get_thread_id(), get_user_id(), set_request_context(), ErrorCategory, ErrorRecord (+8 more)

### Community 3 - "DeviceRecord"
Cohesion: 0.05
Nodes (17): DeviceRecord, _utc_now(), DeviceService, DeviceNotFoundError, DeviceStore, _get_default_seed_devices(), MemoryDeviceStore, _sample_device() (+9 more)

### Community 4 - "AnswerGenerator"
Cohesion: 0.05
Nodes (4): AnswerGenerator, main(), MetricsEvaluator, TestAnswerGenerator

### Community 5 - "Config"
Cohesion: 0.05
Nodes (9): create_mcp_rag_agent(), get_mcp_connections(), _load_mcp_tools_and_prompt(), Config, get_langchain_run_config(), is_langsmith_enabled(), TestAgentCreation, TestLangSmithIntegration (+1 more)

### Community 6 - "test_it_evaluation.py"
Cohesion: 0.06
Nodes (10): BenchmarkDataset, convert_excel_to_benchmark(), get_default_dataset_path(), ITBenchmarkDataset, load_benchmark_dataset(), load_it_benchmark_dataset(), test_it_benchmark_dataset_loading(), test_malformed_benchmark_handling() (+2 more)

### Community 7 - "agent/models.py"
Cohesion: 0.07
Nodes (16): create_rag_agent_instance(), create_search_documents_tool(), _async_search(), _sync_search_stub(), demo(), __getattr__(), AgentResponse, SearchDocumentsInput (+8 more)

### Community 8 - "metrics/__init__.py"
Cohesion: 0.07
Nodes (10): compute_answer_correctness(), compute_answer_relevancy(), compute_context_precision(), compute_context_recall(), compute_faithfulness(), compute_generation_metrics(), _extract_content_tokens(), _extract_numbers() (+2 more)

### Community 9 - "SecuritySubject"
Cohesion: 0.09
Nodes (12): AuthorizationDecision, AuthorizationService, get_role_permissions(), has_permission(), Permission, SecuritySubject, set_current_subject(), with_security_subject() (+4 more)

### Community 10 - "test_evaluation_framework.py"
Cohesion: 0.09
Nodes (8): FailureCase, main(), MetricComparisonRow, RegressionComparator, EvalRunSummary, main(), test_regression_comparator_failure_detection(), TestRegressionComparator

### Community 11 - "TicketRecord"
Cohesion: 0.08
Nodes (9): TicketRecord, TicketNotFoundError, MemoryTicketStore, MemoryTicketStore, MemoryTicketStore, MemoryTicketStore, MemoryTicketStore, test_ticket_comments_and_service_methods() (+1 more)

### Community 13 - "test_api.py"
Cohesion: 0.05
Nodes (16): create_app(), client(), test_chat_custom_request_id_header(), test_chat_endpoint_success(), test_chat_internal_error_handling(), test_chat_validation_error_empty_message(), test_conversation_not_found(), test_create_and_get_conversation() (+8 more)

### Community 14 - "test_admin_api.py"
Cohesion: 0.06
Nodes (11): test_admin_audit_logs_rbac(), test_admin_evaluation_endpoint(), test_admin_incidents_rbac_and_data(), test_admin_metrics_endpoint(), test_admin_ticket_detail_endpoint(), test_admin_tickets_rbac_protection(), _build_test_client(), test_ticket_routes_disabled_when_feature_flag_off() (+3 more)

### Community 15 - "Role"
Cohesion: 0.06
Nodes (21): Role, auth_service(), employee_subject(), it_admin_subject(), it_support_subject(), other_employee_subject(), security_analyst_subject(), test_can_check_role_permissions() (+13 more)

### Community 16 - "eval_runner.py"
Cohesion: 0.10
Nodes (7): BenchmarkItem, ITBenchmarkItem, compute_retrieval_metrics(), EvalRunItemResult, main(), ProductionEvalRunner, TestProductionEvalRunner

### Community 18 - "tickets/models.py"
Cohesion: 0.12
Nodes (11): create_ticket(), _ensure_enabled(), get_ticket(), patch_ticket(), ITTicketAPIService, TicketComment, TicketCreate, TicketOperationResult (+3 more)

### Community 19 - "ConversationService"
Cohesion: 0.10
Nodes (9): create_conversation(), get_conversation_history(), list_conversations(), ChatMessageItem, ConversationHistoryResponse, ConversationThreadResponse, CreateConversationRequest, DeleteConversationResponse (+1 more)

### Community 20 - "ViolationType"
Cohesion: 0.14
Nodes (11): check_input_prompt_injection(), check_out_of_domain(), sanitize_query(), DecisionCategory, GuardrailViolation, ViolationType, calculate_grounding_score(), evaluate_output_grounding() (+3 more)

### Community 21 - "Runbook"
Cohesion: 0.11
Nodes (13): Runbook, RunbookStep, create_github_runbook(), create_jira_runbook(), create_laptop_display_runbook(), create_mfa_runbook(), create_outlook_runbook(), create_password_runbook() (+5 more)

### Community 22 - "runbooks/__init__.py"
Cohesion: 0.12
Nodes (8): RunbookExecutionState, RunbookStatus, StepActionType, StepEvaluationInput, StepExecutionRecord, StepOutcome, _utc_now(), RunbookToolInput

### Community 23 - "IncidentRecord"
Cohesion: 0.13
Nodes (9): IncidentCreate, IncidentMatchCriteria, IncidentRecord, _utc_now(), IncidentService, _get_default_seed_incidents(), IncidentStatus, MemoryIncidentStore (+1 more)

### Community 24 - "approval.py"
Cohesion: 0.10
Nodes (7): ApprovalNotFoundError, ApprovalRequest, ApprovalService, ApprovalStore, InvalidApprovalStateError, _utc_now(), test_unapproved_high_risk_action_blocked()

### Community 25 - "test_guardrails_adversarial.py"
Cohesion: 0.07
Nodes (5): TestEmptyRetrievalHandling, TestLowSimilarityCutoff, TestOutOfDomainDetection, TestSensitiveInformationProtection, TestUserQueryPromptInjectionDefense

### Community 26 - "RAGAgentRunner"
Cohesion: 0.09
Nodes (3): RAGAgentRunner, TestAgentRunnerResponsibilities, TestAgentRunnerObservability

### Community 27 - "ServiceStatusRecord"
Cohesion: 0.12
Nodes (6): ServiceStatusRecord, _utc_now(), _get_default_seed_services(), ServiceNotFoundError, ServiceStatusStore, MemoryServiceStore

### Community 28 - "RetrievedChunkOutput"
Cohesion: 0.09
Nodes (8): RetrievedChunkOutput, check_conflicting_documents(), evaluate_retrieval_context(), sanitize_document_text(), TestCitationValidation, TestConflictingDocumentsDetection, TestDocumentPromptInjectionDefense, TestMaxContextLimits

### Community 29 - "app.js"
Cohesion: 0.15
Nodes (31): checkHealth(), createConversation(), deleteConversation(), escapeHtml(), getAdminAudit(), getAdminEvaluation(), getAdminIncidents(), getAdminMetrics() (+23 more)

### Community 30 - "test_mcp_it_tools.py"
Cohesion: 0.10
Nodes (10): test_agent_toolbelt_includes_it_operations_when_flag_enabled(), test_it_operations_tools_instantiation(), test_it_tools_access_request_and_ticket_creation(), test_it_tools_vpn_workflow(), test_check_service_status_operational_and_unknown(), test_create_ticket_flow_and_duplicate_detection(), test_get_device_info_by_device_id_and_user_id(), test_get_device_info_missing_args() (+2 more)

### Community 31 - "ingestion/__init__.py"
Cohesion: 0.10
Nodes (7): IngestionResult, IngestionStatus, BaseDocumentParser, DocxParser, get_parser(), IngestionError, UnsupportedFileTypeError

### Community 32 - "retrieval/pipeline.py"
Cohesion: 0.11
Nodes (5): RetrievalDebugInfo, BaseReranker, CrossEncoderReranker, get_reranker(), NoOpReranker

### Community 33 - "mcp_rag_agent/it_support/__init__.py"
Cohesion: 0.14
Nodes (16): Device, Incident, ITIssue, Priority, SupportUser, Ticket, TicketStatus, _utc_now() (+8 more)

### Community 34 - "retrieval.py"
Cohesion: 0.11
Nodes (7): compute_hit_rate(), compute_mrr(), compute_precision_at_k(), compute_recall_at_k(), _matches_any_relevant(), normalize_doc_name(), TestRetrievalMetrics

### Community 35 - "ServiceStatusChecker"
Cohesion: 0.10
Nodes (10): get_seed_devices(), get_seed_service_statuses(), seed_it_operations_data(), ServiceOperationalStatus, normalize_service_name(), ServiceStatusChecker, test_service_status_invalid_input_raises_value_error(), test_service_status_known_services_and_aliases() (+2 more)

### Community 36 - "audit.py"
Cohesion: 0.11
Nodes (6): mask_sensitive(), AuditEvent, AuditStore, _get_default_seed_audits(), _sanitize_details(), _utc_now()

### Community 37 - "ParsedDocument"
Cohesion: 0.15
Nodes (6): DocumentChunker, DocumentChunk, DocumentSegment, ParsedDocument, ParsingError, TestDocumentChunker

### Community 38 - "test_ingestion_pipeline.py"
Cohesion: 0.09
Nodes (3): PDFParser, TextParser, TestDocumentParsers

### Community 39 - "test_runbooks.py"
Cohesion: 0.09
Nodes (6): get_default_registry(), create_runbook_tool(), _execute(), TestRunbookRegistrationAndLookup, TestRunbookSelection, TestRunbookToolIntegration

### Community 40 - "get_checkpointer"
Cohesion: 0.10
Nodes (4): get_checkpointer(), TestSessionMemoryCheckpointer, make_agent_graph(), fake_ainvoke()

### Community 41 - "AdvancedRetriever"
Cohesion: 0.13
Nodes (5): AdvancedRetriever, TestOverfetchingAndFiltering, TestRetrievalDebugAndObservability, TestRetrievedChunkSchemaCompliance, TestRRFRankingAndDeduplication

### Community 42 - "ChatService"
Cohesion: 0.14
Nodes (7): get_chat_service(), chat_endpoint(), ChatRequest, ChatResponse, ChatResponseMetadata, SourceDocument, ChatService

### Community 43 - "ConfigurationError"
Cohesion: 0.09
Nodes (5): ConfigurationError, main(), get_hybrid_search(), set_hybrid_search(), TestToolsAndRetriever

### Community 44 - "TestTypedToolInterface"
Cohesion: 0.12
Nodes (6): set_advanced_retriever(), CandidateItem, RetrievalLatency, RetrievalResult, test_retrieval_confidential_security_docs_filtered_for_employee(), TestTypedToolInterface

### Community 45 - "test_approval.py"
Cohesion: 0.11
Nodes (12): ApprovalStatus, admin_subject(), approval_service(), it_support_subject(), requester_subject(), test_approval_by_authorized_admin(), test_execute_approved_action_workflow(), test_expired_approval_cannot_be_approved_or_executed() (+4 more)

### Community 46 - "dependencies.py"
Cohesion: 0.15
Nodes (8): get_admin_service(), get_config(), get_conversation_service(), get_current_security_subject(), get_it_ticket_service(), require_admin_role(), require_audit_permission(), AuditService

### Community 47 - "QueryPreprocessor"
Cohesion: 0.13
Nodes (3): PreprocessedQuery, QueryPreprocessor, TestQueryPreprocessor

### Community 48 - ".run"
Cohesion: 0.10
Nodes (3): AgentExecutionMetadata, mock_runner(), test_chat_endpoint_with_structured_sources()

### Community 49 - "AdminAPIService"
Cohesion: 0.12
Nodes (7): get_admin_audit_logs(), get_admin_ticket(), list_admin_incidents(), list_admin_tickets(), health_check(), AdminAPIService, get()

### Community 50 - "RunbookExecutor"
Cohesion: 0.21
Nodes (5): RunbookExecutor, RunbookRegistry, _create_sample_runbook(), TestRunbookExecutionLifecycle, TestStatePersistenceAndValidation

### Community 51 - "datetime"
Cohesion: 0.14
Nodes (4): readiness_check(), HealthResponse, ReadinessDetails, ReadinessResponse

### Community 52 - "pydantic"
Cohesion: 0.10
Nodes (9): test_get_role_permissions_is_copy(), test_has_permission_helper(), test_it_admin_role_permissions(), test_permission_enum_values(), test_risk_level_enum(), test_role_enum_values(), test_security_analyst_role_permissions(), test_security_subject_validation() (+1 more)

### Community 53 - "DocumentIngestionPipeline"
Cohesion: 0.16
Nodes (3): DocumentIngestionPipeline, TestDuplicateDetectionAndIncrementalIngestion, TestIngestionFailures

### Community 54 - "UserNotFoundError"
Cohesion: 0.14
Nodes (8): UserNotFoundError, MemoryUserStore, MemoryUserStore, _sample_user(), test_user_service_invalid_id_raises_value_error(), test_user_service_missing_user_raises_not_found(), test_user_service_valid_lookup(), test_user_store_mongodb_adapter()

### Community 55 - "RiskLevel"
Cohesion: 0.13
Nodes (6): RiskPolicy, RiskLevel, test_is_approval_required_gate(), test_risk_classification_tiers(), test_audit_event_model(), test_audit_log_event_and_query()

### Community 56 - "RAGGuardrails"
Cohesion: 0.13
Nodes (4): RAGGuardrails, GuardrailResult, mask_sensitive_data(), TestGuardrailResultSchema

### Community 57 - "RetrievedChunk"
Cohesion: 0.12
Nodes (3): RetrievedChunk, LLMReranker, TestRerankerAbstraction

### Community 58 - "operational.py"
Cohesion: 0.13
Nodes (5): compute_cost_usd(), estimate_tokens(), extract_operational_metrics(), OperationalMetrics, TestOperationalMetrics

### Community 59 - "index_documents_from_folder"
Cohesion: 0.14
Nodes (4): index_documents_from_folder(), MagicMockWrapper, _run_legacy_compatible_ingestion(), PipelineSummary

### Community 60 - "create_runbook_subgraph"
Cohesion: 0.12
Nodes (8): create_runbook_subgraph(), escalate_node(), evaluate_node(), resolve_node(), step_node(), _get_runbook_from_state(), RunbookGraphState, RunbookNotFoundError

### Community 61 - "ITCategory"
Cohesion: 0.19
Nodes (8): ITIntentClassifier, ITCategory, test_ambiguous_query_uses_injected_llm_fallback(), test_deterministic_match_never_calls_fallback(), test_it_terms_are_not_rejected_as_out_of_domain(), test_known_queries_use_deterministic_rules(), test_rule_classification_extracts_requested_entities(), test_unknown_query_is_structured_and_concise()

### Community 62 - "users/store.py"
Cohesion: 0.21
Nodes (6): get_seed_users(), SupportTier, UserStatus, _utc_now(), _get_default_seed_users(), test_user_model_instantiation_and_validation()

### Community 63 - "setup_services"
Cohesion: 0.13
Nodes (7): reset_retriever(), set_device_service(), set_ticket_service(), set_user_service(), setup_services(), MemoryUserStore, setup_services()

### Community 64 - "intent.py"
Cohesion: 0.16
Nodes (5): classify_intent(), _extract_entities(), IntentLLMFallback, ITEntities, ITIntentResult

### Community 66 - "test_incidents.py"
Cohesion: 0.21
Nodes (8): _incident(), MemoryIncidentStore, test_incident_create_retrieve_and_status_update(), test_incident_resolve_sets_end_time(), test_incident_service_find_known_case_insensitivity_and_partial_signals(), test_incident_store_queries_and_not_found_handling(), test_incident_store_uses_mongodb(), test_known_incident_detection_requires_structured_match()

### Community 68 - "TicketService"
Cohesion: 0.14
Nodes (3): TicketLifecycleStatus, TicketService, _get_default_seed_tickets()

### Community 71 - "test_tool_authorization_success_emits_audit_log"
Cohesion: 0.18
Nodes (5): reset_it_services(), set_audit_service(), test_tool_authorization_denial_emits_audit_log(), test_tool_authorization_success_emits_audit_log(), setup_security_environment()

### Community 72 - "benchmark_retrieval.py"
Cohesion: 0.21
Nodes (4): create_mock_retrieval_environment(), main(), run_advanced_search(), run_baseline_search()

### Community 74 - "pytest"
Cohesion: 0.28
Nodes (9): _request(), test_create_and_duplicate_detection(), test_escalation_is_allowed_only_from_open_or_in_progress(), test_invalid_lifecycle_transition_is_rejected(), test_lifecycle_allows_only_deterministic_transitions(), test_mongodb_failure_is_not_silenced(), test_ticket_store_crud_uses_shared_mongodb_client(), test_ticket_store_queries_and_not_found_handling() (+1 more)

### Community 75 - "get_admin_evaluation"
Cohesion: 0.19
Nodes (4): get_admin_evaluation(), get_admin_metrics(), AdminEvaluationSummary, OperationalKPIs

### Community 84 - "metrics_evaluator.py"
Cohesion: 0.25
Nodes (4): ensure_assets_dir(), generate_horizontal_bar_chart(), load_eval_data(), main()

### Community 88 - "compute_it_metrics"
Cohesion: 0.22
Nodes (3): compute_it_metrics(), ITMetricResult, test_compute_it_metrics_precision()

## Knowledge Gaps
- **37 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MongoDBClient` connect `typing` to `mcp_server/tools.py`, `ObservabilityTracer`, `DeviceRecord`, `TestMongoDBClient`, `tickets/models.py`, `IncidentRecord`, `approval.py`, `ServiceStatusRecord`, `retrieval/pipeline.py`, `ServiceStatusChecker`, `audit.py`, `AdvancedRetriever`, `dependencies.py`, `DocumentIngestionPipeline`, `index_documents_from_folder`, `users/store.py`, `TicketService`, `IncidentStore`, `TestMongoDBLiveIntegration`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Are the 58 inferred relationships involving `Config` (e.g. with `create_rag_agent_instance()` and `create_mcp_rag_agent()`) actually correct?**
  _`Config` has 58 INFERRED edges - model-reasoned connections that need verification._
- **Should `typing` be split into smaller, more focused modules?**
  _Cohesion score 0.030416911332941866 - nodes in this community are weakly interconnected._
- **Why does `Config` connect `Config` to `typing`, `mcp_server/tools.py`, `TestAPIIntegration`, `TestConfigValidation`, `agent/models.py`, `get_checkpointer`, `ChatService`, `ConfigurationError`, `test_api.py`, `dependencies.py`, `test_admin_api.py`, `tickets/models.py`, `datetime`, `ConversationService`, `ViolationType`, `IncidentRecord`, `RAGGuardrails`, `test_mcp_it_tools.py`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `TicketRecord` (e.g. with `get_admin_ticket()` and `list_admin_tickets()`) actually correct?**
  _`TicketRecord` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Should `mcp_server/tools.py` be split into smaller, more focused modules?**
  _Cohesion score 0.042869057547956634 - nodes in this community are weakly interconnected._
- **Why does `TicketRecord` connect `TicketRecord` to `mcp_rag_agent/it_support/__init__.py`, `TicketService`, `TicketStore`, `pytest`, `dependencies.py`, `AdminAPIService`, `tickets/models.py`, `IncidentRecord`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._