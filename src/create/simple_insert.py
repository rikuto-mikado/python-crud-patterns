from src.db import SessionLocal, User
from sqlalchemy.exc import IntegrityError


def run_simple_insert():
    with SessionLocal() as session:
        try:
            new_user_info = User(name="Rikuto", email="example.com", is_active=True)

            session.add(new_user_info)
            session.commit()
            session.refresh(new_user_info)
            # info contains the result metadata; .id returns the auto-generated primary key of the inserted row
            print(f"Created User ID, {new_user_info.id}")

        except IntegrityError as e:
            session.rollback()
            # e.orig exposes the original DB-level error from the underlying driver (e.g. UNIQUE constraint)
            print(f"Failed to insert, {e.orig}")
        except Exception as e:
            session.rollback()
            print(f"An unexpected error occurred, {e}")


if __name__ == "__main__":
    run_simple_insert()
