from src.db import SessionLocal, User
from sqlalchemy.exc import SQLAlchemyError


def run_atomic_transaction():
    """
    Wrap multiple insert operations in a single transaction.
    If any operation fails (e.g. a constraint violation on the second insert),
    all previous operations in the transaction are rolled back.
    """
    with SessionLocal() as session:
        with session.begin():
            try:
                user = User(name="Kirby", email="kirby@example.com")
                session.add(user)

                # Either ValueError or SQLAlchemyError works here — both trigger a rollback the same way
                raise ValueError("Simulated Error")

            except Exception as e:
                print(f"Transaction failed unexpectedly: {e}")
                raise  # Here's to ensure the transaction is rolled back


if __name__ == "__main__":
    run_atomic_transaction()
