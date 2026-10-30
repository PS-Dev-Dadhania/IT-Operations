# audit.py

> 27 nodes · cohesion 0.11

## Key Concepts

- **audit.py** (22 connections) — `src/mcp_rag_agent/security/audit.py`
- **AuditEvent** (19 connections) — `src/mcp_rag_agent/security/audit.py`
- **AuditStore** (15 connections) — `src/mcp_rag_agent/security/audit.py`
- **mcp_rag_agent/mongodb/__init__.py** (11 connections) — `src/mcp_rag_agent/mongodb/__init__.py`
- **mask_sensitive()** (10 connections) — `src/mcp_rag_agent/core/log_setup.py`
- **_sanitize_details()** (8 connections) — `src/mcp_rag_agent/security/audit.py`
- **.log_event()** (7 connections) — `src/mcp_rag_agent/security/audit.py`
- **_get_default_seed_audits()** (6 connections) — `src/mcp_rag_agent/security/audit.py`
- **.query_events()** (4 connections) — `src/mcp_rag_agent/security/audit.py`
- **._collection()** (4 connections) — `src/mcp_rag_agent/security/audit.py`
- **.query()** (4 connections) — `src/mcp_rag_agent/security/audit.py`
- **datetime** (4 connections)
- **.__init__()** (3 connections) — `src/mcp_rag_agent/security/audit.py`
- **.insert()** (3 connections) — `src/mcp_rag_agent/security/audit.py`
- **Any** (3 connections)
- **.__init__()** (2 connections) — `src/mcp_rag_agent/security/audit.py`
- **_utc_now()** (2 connections) — `src/mcp_rag_agent/security/audit.py`
- **Any** (1 connections)
- **Mask credentials, API keys, passwords, bearer tokens, and connection strings.** (1 connections) — `src/mcp_rag_agent/core/log_setup.py`
- **MongoDB client and semantic search modules.** (1 connections) — `src/mcp_rag_agent/mongodb/__init__.py`
- **BaseModel** (1 connections)
- **MongoDB-backed structured audit logging service for enterprise IT operations.** (1 connections) — `src/mcp_rag_agent/security/audit.py`
- **Persistence store for security audit records.** (1 connections) — `src/mcp_rag_agent/security/audit.py`
- **Recursively mask secrets and remove private credential fields.** (1 connections) — `src/mcp_rag_agent/security/audit.py`
- **Create and persist a sanitized audit event.** (1 connections) — `src/mcp_rag_agent/security/audit.py`
- *... and 2 more nodes in this community*

## Relationships

- [dependencies.py](dependencies.py.md) (14 shared connections)
- [typing](typing.md) (8 shared connections)
- [RiskLevel](RiskLevel.md) (5 shared connections)
- [SecuritySubject](SecuritySubject.md) (4 shared connections)
- [Role](Role.md) (4 shared connections)
- [IncidentRecord](IncidentRecord.md) (3 shared connections)
- [AdminAPIService](AdminAPIService.md) (3 shared connections)
- [mcp_server/tools.py](mcp_server-tools.py.md) (2 shared connections)
- [test_admin_api.py](test_admin_api.py.md) (2 shared connections)
- [.run](run.md) (1 shared connections)
- [get_checkpointer](get_checkpointer.md) (1 shared connections)
- [TestStructuredLoggingAndRedaction](TestStructuredLoggingAndRedaction.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/core/log_setup.py`
- `src/mcp_rag_agent/mongodb/__init__.py`
- `src/mcp_rag_agent/security/audit.py`

## Audit Trail

- EXTRACTED: 85 (88%)
- INFERRED: 12 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*