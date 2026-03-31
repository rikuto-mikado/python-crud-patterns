from src.db import engine, User
from sqlalchemy.dialects.sqlite import insert


def run_upsert(name, email):
    with engine.begin() as conn:
        stmt = insert(User).values(name=name, email=email)

        upsert_stmt = stmt.on_conflict_do_update(
            index_elements=["email"], set_=dict(name=name, is_active=True)
        )

        conn.execute(upsert_stmt)
        print(f"Upsert executed for: {email}")


if __name__ == "__main__":
    run_upsert("Rikuto_Rikuto", "rikutorikuto@example.com")
