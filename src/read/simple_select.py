from db import SessionLocal, User
from sqlalchemy import select


def get_all_users():
    with SessionLocal() as session:
        stmt = select(User).order_by(User.id.desc())
        results = session.execute(stmt).scalars().all()

        print(f"--- All Users ({len(results)}) ---")
        for user in results:
            print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")
        return results


def get_user_by_id(user_id: int):
    with SessionLocal() as session:
        stmt = select(User).where(User.id == user_id)
        user = session.execute(stmt).scalars().one_or_none()

    if user:
        print(f"--- User Found ---")
        print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")
    else:
        print(f"--- User Not Found: {user_id} ---")
    return user


if __name__ == "__main__":
    get_all_users()
    get_user_by_id(1)
