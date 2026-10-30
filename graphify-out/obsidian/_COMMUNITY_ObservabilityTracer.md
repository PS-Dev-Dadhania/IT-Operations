---
type: community
cohesion: 0.05
members: 83
---

# ObservabilityTracer

**Cohesion:** 0.05 - loosely connected
**Members:** 83 nodes

## Members
- [[dot-__init__()_14]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-async_span()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-filter()]] - code - src/mcp_rag_agent/core/log_setup.py
- [[dot-finish()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-hybrid_search()]] - code - src/mcp_rag_agent/mongodb/client.py
- [[dot-record_database_op()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-record_error()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-record_evaluation_metadata()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-record_llm_call()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-record_retrieval()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-record_tool_call()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-span()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[dot-test_connect_records_database_error_on_failure()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_default_context_is_empty()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_set_request_context_async_tasks()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_set_request_context_sync()]] - code - tests/unit_tests/test_observability.py
- [[dot-test_vector_search_records_telemetry_in_tracer()]] - code - tests/unit_tests/test_observability.py
- [[dot-text_search()_1]] - code - src/mcp_rag_agent/mongodb/client.py
- [[dot-vector_search()_1]] - code - src/mcp_rag_agent/mongodb/client.py
- [[Any_7]] - code
- [[Any_8]] - code
- [[Any_9]] - code
- [[Asynchronous context manager for tracing an operational step.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[BaseModel_6]] - code
- [[Calculate inference cost in USD given model and token counts.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Context manager to establish request correlation IDs across async task…]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Data models for Phase 8 Production Observability, telemetry, tracing, and…]] - rationale - src/mcp_rag_agent/observability/models.py
- [[Detailed record of an error or guardrail trigger occurring during execution.]] - rationale - src/mcp_rag_agent/observability/models.py
- [[Discrete operational span representing a sub-task in the execution pipeline.]] - rationale - src/mcp_rag_agent/observability/models.py
- [[End-to-end execution trace capturing metrics from Request through Response.]] - rationale - src/mcp_rag_agent/observability/models.py
- [[End-to-end request tracer recording operational metrics, spans, and errors.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Enum]] - code
- [[ErrorCategory]] - code - src/mcp_rag_agent/observability/models.py
- [[ErrorRecord]] - code - src/mcp_rag_agent/observability/models.py
- [[Exception]] - code
- [[Finish the trace and generate immutable RequestTrace snapshot.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Get the active ObservabilityTracer from context or None.]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Get the current request ID from context or empty string if unset.]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Get the current thread ID from context or empty string if unset.]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Get the current user ID from context or None if unset.]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Observability tracer tracking spans, latencies, tokens, costs, and categorized…]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[ObservabilityTracer]] - code - src/mcp_rag_agent/observability/tracer.py
- [[Perform full-text search using MongoDB text index or Atlas Search. This method…]] - rationale - src/mcp_rag_agent/mongodb/client.py
- [[Perform hybrid search combining vector similarity and full-text search. This…]] - rationale - src/mcp_rag_agent/mongodb/client.py
- [[Perform vector similarity search. Args collection_name Name of the…]] - rationale - src/mcp_rag_agent/mongodb/client.py
- [[Public API for Phase 8 Production Observability Subsystem.]] - rationale - src/mcp_rag_agent/observability/__init__.py
- [[Record LLM generation metrics, tokens, and inference cost.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Record MongoDB database operation telemetry.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Record a categorized error or guardrail trigger.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Record guardrail decisions and factual grounding scores.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Record retrieval pipeline execution metrics.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Record tool invocation telemetry.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[RequestTrace]] - code - src/mcp_rag_agent/observability/models.py
- [[Return dictionary of current correlation identifiers.]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Standardized error categories for end-to-end AI system diagnostics.]] - rationale - src/mcp_rag_agent/observability/models.py
- [[Synchronous context manager for tracing an operational step.]] - rationale - src/mcp_rag_agent/observability/tracer.py
- [[Test MongoDBClient database operation telemetry and error tagging.]] - rationale - tests/unit_tests/test_observability.py
- [[Test correlation ID tracking across synchronous and asynchronous contexts.]] - rationale - tests/unit_tests/test_observability.py
- [[TestCorrelationContext]] - code - tests/unit_tests/test_observability.py
- [[TestMongoDBClientTelemetry]] - code - tests/unit_tests/test_observability.py
- [[Thread-safe and async-safe request context management using contextvars.]] - rationale - src/mcp_rag_agent/observability/context.py
- [[Token consumption and financial accounting for LLM invocations.]] - rationale - src/mcp_rag_agent/observability/models.py
- [[TokenUsage]] - code - src/mcp_rag_agent/observability/models.py
- [[TraceSpan]] - code - src/mcp_rag_agent/observability/models.py
- [[Verify connection failures record ErrorCategory.DATABASE_ERROR in active tracer.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify context manager sets and restores correlation IDs.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify correlation IDs automatically propagate into spawned asyncio tasks.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify default context getters return empty strings or None.]] - rationale - tests/unit_tests/test_observability.py
- [[Verify vector search records database operation span in active tracer.]] - rationale - tests/unit_tests/test_observability.py
- [[background_worker()]] - code - tests/unit_tests/test_observability.py
- [[calculate_cost_usd()]] - code - src/mcp_rag_agent/observability/tracer.py
- [[context.py]] - code - src/mcp_rag_agent/observability/context.py
- [[contextlib]] - concept
- [[get_correlation_ids()]] - code - src/mcp_rag_agent/observability/context.py
- [[get_current_tracer()]] - code - src/mcp_rag_agent/observability/context.py
- [[get_request_id()]] - code - src/mcp_rag_agent/observability/context.py
- [[get_thread_id()]] - code - src/mcp_rag_agent/observability/context.py
- [[get_user_id()]] - code - src/mcp_rag_agent/observability/context.py
- [[observability__init__.py]] - code - src/mcp_rag_agent/observability/__init__.py
- [[observabilitymodels.py]] - code - src/mcp_rag_agent/observability/models.py
- [[set_request_context()]] - code - src/mcp_rag_agent/observability/context.py
- [[str]] - code
- [[tracer.py]] - code - src/mcp_rag_agent/observability/tracer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ObservabilityTracer
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_typing]]
- 13 edges to [[_COMMUNITY_mcp_servertools.py]]
- 12 edges to [[_COMMUNITY_agentmodels.py]]
- 10 edges to [[_COMMUNITY_dot-run]]
- 4 edges to [[_COMMUNITY_TestObservabilityTracer]]
- 4 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_test_observability.py]]
- 3 edges to [[_COMMUNITY_runbooks__init__.py]]
- 2 edges to [[_COMMUNITY_Config]]
- 2 edges to [[_COMMUNITY_SecuritySubject]]
- 1 edge to [[_COMMUNITY_ticketsmodels.py]]
- 1 edge to [[_COMMUNITY_RAGAgentRunner]]
- 1 edge to [[_COMMUNITY_datetime]]
- 1 edge to [[_COMMUNITY_pydantic]]

## Top bridge nodes
- [[observabilitymodels.py]] - degree 14, connects to 5 communities
- [[context.py]] - degree 15, connects to 4 communities
- [[set_request_context()]] - degree 13, connects to 4 communities
- [[ObservabilityTracer]] - degree 25, connects to 3 communities
- [[observability__init__.py]] - degree 24, connects to 3 communities