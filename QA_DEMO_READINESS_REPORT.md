# IT Operations & Support Copilot — QA Demo Readiness Report

**Verification date:** 30 October 2026  
**Overall status:** Ready for a demo of local storage, ticketing, RBAC, and MCP tooling. The only material demo limitation is the unfunded external LLM provider key.

## Live verification summary

| Area | Result | Evidence |
| --- | --- | --- |
| MCP-mode startup | PASS | Application started with `FEATURE_FLAG_MCPSERVER_ENABLED=true`; health and readiness returned HTTP 200. The log confirms MCP client connection and agent initialization. |
| Direct-mode startup | PASS | With the flag temporarily set to `false`, the application logged `Initializing RAG Agent in Direct mode` and both health and readiness returned HTTP 200. |
| MCP stdio invocation | PASS | A `MultiServerMCPClient` discovered seven tools and invoked `check_service_status(corporate_vpn)`. The JSON-RPC tool response reported `OPERATIONAL`. |
| SQLite persistence | PASS | Ticket `TKT-20139517BF` was created, the Uvicorn listener was stopped, the application was restarted, and the ticket was retrieved intact with its original ID, requester, content, and `new` status. |
| RBAC boundary | PASS | `GET /api/v1/admin/tickets` returned HTTP 403 for an Employee header and succeeded for an IT Admin header (eight returned records). |
| Focused regression tests | PASS | `23 passed` across local database integration, MCP integration, MCP IT tools, ticket API, and security regression tests. |

The focused test run emitted one non-functional warning: pytest could not write its cache under `.pytest_cache` because that folder is access-restricted in this environment. It did not affect test execution.

## Issues fixed before verification

1. **Missing single-document lookup in the database wrapper**  
   The ingestion pipeline called `find_document()`, while `MongoDBClient` exposed only `find_documents()`. A local-mode delegating `find_document()` was added in `src/mcp_rag_agent/mongodb/client.py`.

2. **Incomplete MCP search output contract**  
   `SearchDocumentsOutput` lacked `query`, although callers and integration tests depended on it. The optional field was added in `src/mcp_rag_agent/agent/models.py`, and the MCP tool now populates it in `src/mcp_rag_agent/mcp_server/tools.py`.

3. **Incorrect MCP integration precondition**  
   The integration guard accepted only `sk-`-style OpenAI credentials, even when the local database was usable. `tests/integration_tests/test_mcp_integration.py` now permits the local-storage verification path.

4. **Browser favicon 404**  
   A static 16×16 favicon and a `/favicon.ico` response were added in `src/mcp_rag_agent/api/static/favicon.ico` and `src/mcp_rag_agent/api/app.py`.

5. **Demo execution mode**  
   `.env` is set back to `FEATURE_FLAG_MCPSERVER_ENABLED=true` for the live demonstration.

## API contract note found during QA

The requested ticket sample used `user_id`, but the live `TicketCreate` contract requires `requester_id`. The original sample returns HTTP 422; substituting `requester_id: "EMP-1001"` creates the ticket successfully. Use the corrected payload below for the demo:

```json
{
  "title": "QA Demo Persistence Test",
  "description": "Verifying ticket persists across server restarts",
  "requester_id": "EMP-1001",
  "priority": "medium",
  "category": "software"
}
```

## Direct mode and MCP mode

| Mode | Flag | Verification |
| --- | --- | --- |
| Direct | `FEATURE_FLAG_MCPSERVER_ENABLED=false` | Agent initializes in-process with direct LangChain tools; health and readiness checks passed. |
| MCP (demo default) | `FEATURE_FLAG_MCPSERVER_ENABLED=true` | The API starts an MCP stdio client; it discovered seven registered tools and returned a structured tool result for `check_service_status`. |

## Database persistence evidence

`POST /api/v1/it/tickets` created `TKT-20139517BF`. Following a complete stop of the active Uvicorn listener and a fresh startup, `GET /api/v1/it/tickets/TKT-20139517BF` returned the stored ticket with:

- `requester_id`: `EMP-1001`
- `status`: `new`
- unchanged title, description, category, priority, and timestamps

This validates the SQLite-backed ticket path across process restart.

## Security and RBAC

- The authoritative role matrix is in `src/mcp_rag_agent/security/rbac.py`.
- Employees receive scoped permissions such as own-ticket viewing, ticket creation, device context, knowledge search, and service-status checks.
- `/api/v1/admin/*` endpoints require `it_admin` or `system_admin`; the employee denial and IT Admin success were exercised live.
- Ticket resource authorization further prevents employees from accessing or modifying tickets belonging to another requester (`src/mcp_rag_agent/security/authorization.py`).

## Startup commands

For the normal local demo:

```powershell
.\start_app.bat
```

For an explicit PowerShell start without automatic browser launch:

```powershell
$env:PYTHONPATH = "$PWD\src"
.\.venv\Scripts\python.exe -m uvicorn mcp_rag_agent.api.app:create_app --factory --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/ui` after startup. Before launching, confirm `.env` contains:

```text
FEATURE_FLAG_MCPSERVER_ENABLED=true
```

## Known limitations and demo guidance

- The configured Gemini credential is reported to receive a Google 403 quota/billing response. Local deterministic embeddings continue to support retrieval, but live generative chat needs a funded Gemini credential or a working OpenAI-compatible key.
- Do not present a successful live LLM completion unless a funded key has been verified immediately before the demo. The application should instead return its structured `MODEL_ERROR` response gracefully.
- If port 8000 is already in use, identify and stop only the process listening on that port before restarting Uvicorn.
- The historical full-suite baseline supplied for this readiness review was **364 passed, 3 skipped**. A new full-suite attempt was interrupted by the execution environment after progress began, so this report relies on the fresh focused result of **23 passed** rather than restating the historical full-suite count as a fresh run.
