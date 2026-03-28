# Python CRUD Patterns

A personal reference for common CRUD patterns in Python.

---

## Create

| File | Description |
|------|-------------|
| `simple_insert.py` | Basic single-record insert using raw SQL or an ORM |
| `bulk_ops.py` | Insert multiple records at once efficiently |
| `atomic_transaction.py` | Wrap multiple inserts in a transaction to ensure all-or-nothing execution |
| `upsert.py` | Insert a record, or update it if it already exists (`INSERT ... ON CONFLICT`) |

## Read

| File | Description |
|------|-------------|
| `simple_select.py` | Fetch all records or a single record by ID |
| `filter_query.py` | Query with `WHERE` conditions and dynamic filters |
| `pagination.py` | Limit results with offset-based or cursor-based pagination |
| `join_query.py` | Fetch related data across multiple tables using joins |

## Update

| File | Description |
|------|-------------|
| `simple_update.py` | Update a single record by ID |
| `partial_update.py` | Update only specified fields (PATCH semantics) |
| `optimistic_lock.py` | Prevent conflicting updates using a version field |

## Delete

| File | Description |
|------|-------------|
| `hard_delete.py` | Permanently remove a record from the database |
| `soft_delete.py` | Mark a record as deleted without removing it (e.g. `deleted_at` column) |
| `cascade_delete.py` | Delete a record and its related records across tables |
| `iterator_stream.py` | Delete a large number of records in batches to avoid locking |
| `relation_join.py` | Delete records selected via a join condition |
