import time
from src.db import SessionLocal, User, engine
from sqlalchemy import insert


def generate_user_info(count: int):
    return [
        {
            "name": f"User {i}",
            "email": f"user_{i}_{int(time.time())}@example.com",
            "is_active": True,
        }
        for i in range(count)
    ]


def bulk_insert_with_core(data_list: list):
    with engine.begin() as conn:
        conn.execute(insert(User), data_list)


def main():
    target_count = 1000
    users_to_create = generate_user_info(target_count)

    start_time = time.time()

    try:
        bulk_insert_with_core(users_to_create)
        duration = time.time() - start_time
        print(f"Inserted {target_count} records successfully.")
        print(f"Time taken: {duration:.2f} seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
