"""Database migration and backup utility for IT Operations Copilot.

Supports:
1. Migrating data from a remote or local MongoDB instance into local SQLite storage.
2. Non-destructive backups of existing local SQLite databases.
3. Exporting local database collections into portable JSON files.
4. Importing collections from portable JSON files into local database storage.

Usage examples:
    # 1. Migrate directly from MongoDB Atlas / local MongoDB to Local SQLite:
    python scripts/migrate_to_local_db.py --mongo-uri "mongodb://localhost:27017" --mongo-db "mcp_rag_agent_db"

    # 2. Export local SQLite database to JSON folder:
    python scripts/migrate_to_local_db.py --export-dir "./data/backup_export"

    # 3. Import JSON backup files into local SQLite:
    python scripts/migrate_to_local_db.py --import-dir "./data/backup_export"
"""

import argparse
import json
import logging
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# Add src to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mcp_rag_agent.core.config import config
from mcp_rag_agent.core.log_setup import mask_sensitive, setup_logging
from mcp_rag_agent.database.client import JSONCustomEncoder, LocalDatabaseClient

setup_logging()
logger = logging.getLogger("MigrateToLocalDB")

DEFAULT_COLLECTIONS = [
    "documents",
    "vectors",
    "it_tickets",
    "it_incidents",
    "it_users",
    "it_devices",
    "it_service_statuses",
    "it_audit_logs",
    "it_approvals",
    "conversations",
    "checkpoints",
]


def backup_local_database(local_db_path: str) -> Optional[str]:
    """Create a timestamped backup of the local database file if it exists."""
    path = Path(local_db_path)
    if not path.exists() or path.stat().st_size == 0:
        logger.info(f"No existing local database file at '{path}' to backup.")
        return None

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    backup_file = path.parent / f"{path.stem}_backup_{timestamp}{path.suffix}.bak"
    shutil.copy2(path, backup_file)
    logger.info(f"[BACKUP] Created non-destructive backup: {backup_file}")
    print(f"[BACKUP] Created backup at: {backup_file}")
    return str(backup_file)


def migrate_from_mongodb(
    mongo_uri: str,
    mongo_db_name: str,
    local_db_path: str,
    collections: list[str],
    dry_run: bool = False,
) -> dict[str, int]:
    """Migrate documents from MongoDB into the local SQLite database."""
    from pymongo import MongoClient

    safe_uri = mask_sensitive(mongo_uri)
    logger.info(f"Connecting to source MongoDB at {safe_uri}, database: {mongo_db_name}...")
    print(f"[CONNECT] Source MongoDB: {safe_uri} (db: {mongo_db_name})")

    mongo_client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    mongo_client.admin.command("ping")
    source_db = mongo_client[mongo_db_name]

    # Initialize destination local database
    if not dry_run:
        backup_local_database(local_db_path)

    local_client = LocalDatabaseClient(database_path=local_db_path)
    if not dry_run:
        local_client.connect()

    summary: dict[str, int] = {}
    available_collections = source_db.list_collection_names()
    target_collections = [c for c in collections if c in available_collections]

    print(f"\n[MIGRATE] Found {len(target_collections)} matching collection(s) in MongoDB:")
    for col_name in target_collections:
        source_col = source_db[col_name]
        total_source = source_col.count_documents({})
        print(f"  - Collection '{col_name}': {total_source} document(s)")

        if dry_run:
            summary[col_name] = total_source
            continue

        local_col = local_client.get_collection(col_name)
        migrated_count = 0

        # Read in batches of 500
        cursor = source_col.find({})
        batch: list[dict[str, Any]] = []
        for doc in cursor:
            # Ensure _id is string
            doc["_id"] = str(doc["_id"])
            batch.append(doc)
            if len(batch) >= 500:
                local_col.insert_many(batch)
                migrated_count += len(batch)
                batch = []

        if batch:
            local_col.insert_many(batch)
            migrated_count += len(batch)

        summary[col_name] = migrated_count
        print(f"    -> Successfully migrated {migrated_count} document(s) to local collection '{col_name}'")

    if not dry_run:
        local_client.disconnect()
        mongo_client.close()

    return summary


def export_local_to_json(local_db_path: str, export_dir: str) -> dict[str, int]:
    """Export all collections from local SQLite database into JSON files."""
    exp_path = Path(export_dir)
    exp_path.mkdir(parents=True, exist_ok=True)

    client = LocalDatabaseClient(database_path=local_db_path)
    client.connect()
    summary: dict[str, int] = {}

    try:
        collections = client.list_collections()
        print(f"\n[EXPORT] Exporting {len(collections)} collections from '{local_db_path}' to '{export_dir}':")
        for col_name in collections:
            col = client.get_collection(col_name)
            docs = list(col.find({}))
            file_path = exp_path / f"{col_name}.json"
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(docs, f, cls=JSONCustomEncoder, indent=2, ensure_ascii=False)
            summary[col_name] = len(docs)
            print(f"  - Exported {len(docs)} document(s) to {file_path.name}")
    finally:
        client.disconnect()

    return summary


def import_json_to_local(import_dir: str, local_db_path: str) -> dict[str, int]:
    """Import JSON files into local SQLite database."""
    imp_path = Path(import_dir)
    if not imp_path.exists() or not imp_path.is_dir():
        raise FileNotFoundError(f"Import directory '{import_dir}' does not exist.")

    backup_local_database(local_db_path)
    client = LocalDatabaseClient(database_path=local_db_path)
    client.connect()
    summary: dict[str, int] = {}

    try:
        json_files = list(imp_path.glob("*.json"))
        print(f"\n[IMPORT] Importing {len(json_files)} JSON file(s) into '{local_db_path}':")
        for file in json_files:
            col_name = file.stem
            with open(file, "r", encoding="utf-8") as f:
                docs = json.load(f)
            if not isinstance(docs, list):
                logger.warning(f"File {file.name} does not contain a JSON list, skipping.")
                continue

            col = client.get_collection(col_name)
            if docs:
                col.insert_many(docs)
            summary[col_name] = len(docs)
            print(f"  - Imported {len(docs)} document(s) into collection '{col_name}'")
    finally:
        client.disconnect()

    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Database Migration and Backup Tool for IT Operations Copilot"
    )
    parser.add_argument(
        "--mongo-uri",
        type=str,
        default=os.environ.get("MONGODB_ATLAS_CLUSTER_URI", ""),
        help="Source MongoDB URI (e.g. mongodb://localhost:27017)",
    )
    parser.add_argument(
        "--mongo-db",
        type=str,
        default=os.environ.get("MONGODB_ATLAS_DB_NAME", ""),
        help="Source MongoDB database name",
    )
    parser.add_argument(
        "--local-db-path",
        type=str,
        default=config.local_db_path,
        help="Target local database file path (defaults to config.local_db_path)",
    )
    parser.add_argument(
        "--export-dir",
        type=str,
        default=None,
        help="Directory path to export local database collections to JSON files",
    )
    parser.add_argument(
        "--import-dir",
        type=str,
        default=None,
        help="Directory path containing JSON files to import into the local database",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Inspect source database and list collections without modifying local storage",
    )

    args = parser.parse_args()

    if args.export_dir:
        results = export_local_to_json(args.local_db_path, args.export_dir)
        print(f"\n[DONE] Export complete. Summary: {results}")
        return

    if args.import_dir:
        results = import_json_to_local(args.import_dir, args.local_db_path)
        print(f"\n[DONE] Import complete. Summary: {results}")
        return

    if args.mongo_uri and args.mongo_db:
        results = migrate_from_mongodb(
            mongo_uri=args.mongo_uri,
            mongo_db_name=args.mongo_db,
            local_db_path=args.local_db_path,
            collections=DEFAULT_COLLECTIONS,
            dry_run=args.dry_run,
        )
        print(f"\n[DONE] Migration complete. Summary: {results}")
        return

    print("No operation specified.")
    print("Use --export-dir <dir> to export local database to JSON.")
    print("Use --import-dir <dir> to import JSON into local database.")
    print("Use --mongo-uri <uri> --mongo-db <db> to migrate from MongoDB.")


if __name__ == "__main__":
    main()
