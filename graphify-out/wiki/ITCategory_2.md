# ITCategory

> God node · 51 connections · `src/mcp_rag_agent/it_support/models.py`

**Community:** [ITCategory](ITCategory.md)

## Connections by Relation

### calls
- create_ticket_typed() `EXTRACTED`

### contains
- it_support/models.py `EXTRACTED`

### imports
- [mcp_server/tools.py](mcp_server-tools.py.md) `EXTRACTED`
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) `EXTRACTED`
- runbooks/models.py `EXTRACTED`
- executor.py `EXTRACTED`
- [tickets/models.py](tickets-models.py.md) `EXTRACTED`
- runbook_definitions.py `EXTRACTED`
- tickets/store.py `EXTRACTED`
- incidents/models.py `EXTRACTED`
- registry.py `EXTRACTED`
- [intent.py](intent.py.md) `EXTRACTED`

### inherits
- Enum `EXTRACTED`
- str `EXTRACTED`

### rationale_for
- Stable top-level taxonomy used by Phase 13-A classification. `EXTRACTED`

### references
- .select_and_start() `EXTRACTED`
- .find_for_query() `EXTRACTED`
- .get_by_category() `EXTRACTED`

### uses
- [RunbookExecutor](RunbookExecutor.md) `INFERRED`
- RunbookRegistry `INFERRED`
- [Runbook](Runbook.md) `INFERRED`
- test_setup() `INFERRED`
- ITIntentClassifier `INFERRED`
- TicketCreate `INFERRED`
- IncidentMatchCriteria `INFERRED`
- _create_sample_runbook() `INFERRED`
- TestStatePersistenceAndValidation `INFERRED`
- IncidentCreate `INFERRED`
- _request() `INFERRED`
- _incident() `INFERRED`
- TestRunbookRegistrationAndLookup `INFERRED`
- test_incident_store_queries_and_not_found_handling() `INFERRED`
- create_github_runbook() `INFERRED`
- create_jira_runbook() `INFERRED`
- create_laptop_display_runbook() `INFERRED`
- create_mfa_runbook() `INFERRED`
- create_outlook_runbook() `INFERRED`
- create_password_runbook() `INFERRED`
- *…and 13 more `uses` connection(s) not listed (lowest-degree first to go)*

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*