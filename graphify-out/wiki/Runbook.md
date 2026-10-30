# Runbook

> 35 nodes · cohesion 0.11

## Key Concepts

- **Runbook** (31 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **RunbookStep** (20 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **runbook_definitions.py** (20 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **get_all_standard_runbooks()** (16 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_github_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_jira_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_laptop_display_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_mfa_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_outlook_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_password_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_phishing_incident_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_printer_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_vpn_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **create_wifi_runbook()** (7 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **.register()** (5 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **.__init__()** (4 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **.validate_graph()** (3 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **.get_step()** (2 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **.test_invalid_graph_transition_raises_error_at_validation()** (2 connections) — `tests/unit_tests/it_support/test_runbooks.py`
- **A deterministic step within an IT troubleshooting runbook.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **Immutable, structured enterprise runbook procedure.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **Validate that all transitions point to known steps or valid terminal states.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/models.py`
- **Register a validated runbook. If marked active, sets as active version for its…** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/registry.py`
- **Safe synthetic enterprise troubleshooting runbook definitions.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- **Runbook 1: Corporate VPN Troubleshooting.** (1 connections) — `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- *... and 10 more nodes in this community*

## Relationships

- [runbooks/__init__.py](runbooks-__init__.py.md) (21 shared connections)
- [ITCategory](ITCategory.md) (16 shared connections)
- [RunbookExecutor](RunbookExecutor.md) (8 shared connections)
- [.find_for_query](find_for_query.md) (3 shared connections)
- [mcp_rag_agent/it_support/__init__.py](mcp_rag_agent-it_support-__init__.py.md) (3 shared connections)
- [create_runbook_subgraph](create_runbook_subgraph.md) (2 shared connections)

## Source Files

- `src/mcp_rag_agent/it_support/runbooks/models.py`
- `src/mcp_rag_agent/it_support/runbooks/registry.py`
- `src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py`
- `tests/unit_tests/it_support/test_runbooks.py`

## Audit Trail

- EXTRACTED: 81 (67%)
- INFERRED: 40 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*