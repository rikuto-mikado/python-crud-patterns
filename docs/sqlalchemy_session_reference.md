# SQLAlchemy Session Reference

## Imports (from `db.py`)

```python
from db import SessionLocal, Base, engine
```

| Name | Type | Description |
|------|------|-------------|
| `SessionLocal` | `sessionmaker` | Factory that creates a new Session. Use with `with SessionLocal() as session:` |
| `Base` | `DeclarativeBase` | Base class for all ORM models |
| `engine` | `Engine` | The underlying DB connection. Used for `create_all` etc. |

---

## Session Methods

| Method | Description |
|--------|-------------|
| `session.add(obj)` | Stage a new or modified object for INSERT/UPDATE |
| `session.add_all([obj1, obj2])` | Stage multiple objects at once |
| `session.commit()` | Persist all staged changes to the DB |
| `session.rollback()` | Undo all staged changes since last commit |
| `session.refresh(obj)` | Reload object state from DB (e.g. to get auto-generated `id`) |
| `session.flush()` | Send staged SQL to DB without committing (within same transaction) |
| `session.get(Model, id)` | Fetch a single record by primary key |
| `session.delete(obj)` | Stage an object for DELETE |
| `session.execute(stmt)` | Run a SQLAlchemy Core statement (e.g. `select()`, `insert()`) |
| `session.scalars(stmt)` | Like `execute()` but returns ORM objects directly |
| `session.merge(obj)` | Upsert: attach a detached object, inserting or updating as needed |
| `session.expunge(obj)` | Detach an object from the session without deleting it |

---

## Common Patterns

```python
# Single insert
with SessionLocal() as session:
    session.add(obj)
    session.commit()
    session.refresh(obj)  # needed to read auto-generated fields

# Bulk insert
with SessionLocal() as session:
    session.add_all([obj1, obj2, obj3])
    session.commit()

# Query
from sqlalchemy import select
with SessionLocal() as session:
    stmt = select(User).where(User.email == "a@example.com")
    user = session.scalars(stmt).first()
```

---

## Base / Engine Utilities

| Method | Description |
|--------|-------------|
| `Base.metadata.create_all(engine)` | Create all tables defined by models if they don't exist |
| `Base.metadata.drop_all(engine)` | Drop all tables (useful for testing) |
