---
type: community
cohesion: 0.18
members: 14
---

# test_tool_authorization_success_emits_audit_log

**Cohesion:** 0.18 - loosely connected
**Members:** 14 nodes

## Members
- [[Ensure clean services and memory stores for regression testing.]] - rationale - tests/unit_tests/security/test_security_regression.py
- [[Reset cached IT domain service and security instances.]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Set or override the AuditService instance.]] - rationale - src/mcp_rag_agent/mcp_server/tools.py
- [[Verify authorized tool execution creates an AUTHORIZED audit record.]] - rationale - tests/unit_tests/security/test_audit.py
- [[Verify tool authorization rejection creates a DENIED audit record.]] - rationale - tests/unit_tests/security/test_audit.py
- [[__init__()]] - code - tests/unit_tests/security/test_audit.py
- [[asyncio_15]] - code
- [[create()]] - code - tests/unit_tests/security/test_audit.py
- [[fixture_10]] - code
- [[reset_it_services()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[set_audit_service()]] - code - src/mcp_rag_agent/mcp_server/tools.py
- [[setup_security_environment()]] - code - tests/unit_tests/security/test_security_regression.py
- [[test_tool_authorization_denial_emits_audit_log()]] - code - tests/unit_tests/security/test_audit.py
- [[test_tool_authorization_success_emits_audit_log()]] - code - tests/unit_tests/security/test_audit.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_tool_authorization_success_emits_audit_log
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_mcp_servertools.py]]
- 3 edges to [[_COMMUNITY_test_admin_api.py]]
- 2 edges to [[_COMMUNITY_Role]]
- 2 edges to [[_COMMUNITY_approval.py]]
- 2 edges to [[_COMMUNITY_SecuritySubject]]
- 2 edges to [[_COMMUNITY_setup_services]]
- 1 edge to [[_COMMUNITY_audit.py]]
- 1 edge to [[_COMMUNITY_dependencies.py]]
- 1 edge to [[_COMMUNITY_UserContextRecord]]
- 1 edge to [[_COMMUNITY_UserService]]
- 1 edge to [[_COMMUNITY_AdminAPIService]]

## Top bridge nodes
- [[test_tool_authorization_success_emits_audit_log()]] - degree 15, connects to 8 communities
- [[setup_security_environment()]] - degree 10, connects to 5 communities
- [[test_tool_authorization_denial_emits_audit_log()]] - degree 9, connects to 4 communities
- [[reset_it_services()]] - degree 6, connects to 2 communities
- [[set_audit_service()]] - degree 6, connects to 1 community