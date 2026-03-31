# How to Run

## Running a script

Always run from the project root using `-m` so that `src` is resolved correctly.

```bash
python -m src.create.simple_insert
python -m src.create.bulk_ops
python -m src.create.atomic_transaction
python -m src.create.upsert
```

## Inspecting the database

Open the SQLite database with:

```bash
sqlite3 dev.db
```

Or run a query directly:

```bash
# All records
sqlite3 dev.db "SELECT * FROM users;"

# Limit results
sqlite3 dev.db "SELECT * FROM users LIMIT 10;"

# Filter by column
sqlite3 dev.db "SELECT * FROM users WHERE email = 'example@example.com';"

# Count records
sqlite3 dev.db "SELECT COUNT(*) FROM users;"

# Delete a specific record
sqlite3 dev.db "DELETE FROM users WHERE name = 'Kirby';"

# Delete all records
sqlite3 dev.db "DELETE FROM users;"
```

## Notes

- `dev.db` is created automatically in the project root on first run
- `dev.db` is gitignored — do not commit it
- All scripts share the same `dev.db` unless `engine` in `src/db.py` is changed
