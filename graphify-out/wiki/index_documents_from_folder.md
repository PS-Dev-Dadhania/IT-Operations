# index_documents_from_folder

> 19 nodes · cohesion 0.14

## Key Concepts

- **index_documents_from_folder()** (16 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **_run_legacy_compatible_ingestion()** (10 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **PipelineSummary** (10 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **.compute_content_hash()** (6 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **.ingest_directory()** (6 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **.ingest_file()** (6 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **MagicMockWrapper** (5 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **Path** (3 connections)
- **Path** (2 connections)
- **.generate()** (1 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **.generate_batch()** (1 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **Any** (1 connections)
- **Fallback generator for mock tests when real EmbeddingGenerator is absent.** (1 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **Helper for mock-based tests asserting on semantic_search.index_document.** (1 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **Index all documents from a folder into MongoDB using the production pipeline.…** (1 connections) — `src/mcp_rag_agent/embeddings/index_documents.py`
- **Aggregate summary of an ingestion run across multiple documents.** (1 connections) — `src/mcp_rag_agent/ingestion/models.py`
- **Scan directory recursively and ingest all supported documents. Args:…** (1 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **Compute SHA-256 hash of file content. Args: file_path: Path to the target file.…** (1 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`
- **Process, chunk, embed, and store a single document. Args: file_path: Path to…** (1 connections) — `src/mcp_rag_agent/ingestion/pipeline.py`

## Relationships

- [typing](typing.md) (9 shared connections)
- [DocumentIngestionPipeline](DocumentIngestionPipeline.md) (7 shared connections)
- [ingestion/__init__.py](ingestion-__init__.py.md) (5 shared connections)
- [ParsedDocument](ParsedDocument.md) (2 shared connections)
- [TestDocumentIngestion](TestDocumentIngestion.md) (2 shared connections)
- [DocumentCleaner](DocumentCleaner.md) (1 shared connections)

## Source Files

- `src/mcp_rag_agent/embeddings/index_documents.py`
- `src/mcp_rag_agent/ingestion/models.py`
- `src/mcp_rag_agent/ingestion/pipeline.py`

## Audit Trail

- EXTRACTED: 41 (82%)
- INFERRED: 9 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*