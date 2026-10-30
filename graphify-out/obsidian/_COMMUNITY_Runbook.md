---
type: community
cohesion: 0.11
members: 35
---

# Runbook

**Cohesion:** 0.11 - loosely connected
**Members:** 35 nodes

## Members
- [[dot-__init__()_15]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[dot-get_step()]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[dot-register()]] - code - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[dot-test_invalid_graph_transition_raises_error_at_validation()]] - code - tests/unit_tests/it_support/test_runbooks.py
- [[dot-validate_graph()]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[A deterministic step within an IT troubleshooting runbook.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Immutable, structured enterprise runbook procedure.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Register a validated runbook. If marked active, sets as active version for its…]] - rationale - src/mcp_rag_agent/it_support/runbooks/registry.py
- [[Return all 10 standard synthetic enterprise runbooks.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Runbook 10 Phishing & Security Incident Containment.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 1 Corporate VPN Troubleshooting.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 2 Wi-Fi Troubleshooting.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 3 Multi-Factor Authentication (MFA) Troubleshooting.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 4 Password & Account Lockout Procedure.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 5 GitHub Enterprise Access & SAML SSO.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 6 Jira & Confluence Access Troubleshooting.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 7 Microsoft Outlook & Exchange Online Troubleshooting.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 8 Enterprise & Office Printer Troubleshooting.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Runbook 9 Laptop Display & External Monitor Resolution.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[RunbookStep]] - code - src/mcp_rag_agent/it_support/runbooks/models.py
- [[Safe synthetic enterprise troubleshooting runbook definitions.]] - rationale - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[Validate that all transitions point to known steps or valid terminal states.]] - rationale - src/mcp_rag_agent/it_support/runbooks/models.py
- [[create_github_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_jira_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_laptop_display_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_mfa_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_outlook_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_password_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_phishing_incident_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_printer_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_vpn_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[create_wifi_runbook()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[get_all_standard_runbooks()]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py
- [[runbook_definitions.py]] - code - src/mcp_rag_agent/it_support/runbooks/runbook_definitions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Runbook
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_runbooks__init__.py]]
- 16 edges to [[_COMMUNITY_ITCategory]]
- 8 edges to [[_COMMUNITY_RunbookExecutor]]
- 3 edges to [[_COMMUNITY_dot-find_for_query]]
- 3 edges to [[_COMMUNITY_mcp_rag_agentit_support__init__.py]]
- 2 edges to [[_COMMUNITY_create_runbook_subgraph]]

## Top bridge nodes
- [[Runbook]] - degree 31, connects to 6 communities
- [[RunbookStep]] - degree 20, connects to 3 communities
- [[runbook_definitions.py]] - degree 20, connects to 3 communities
- [[get_all_standard_runbooks()]] - degree 16, connects to 2 communities
- [[create_github_runbook()]] - degree 7, connects to 2 communities