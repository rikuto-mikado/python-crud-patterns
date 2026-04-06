from db import SessionLocal, User
from sqlalchemy import select, or_, and_


def search_users(
    name_query: str = None, email_domain: str = None, active_only: bool = True
):
    with SessionLocal() as session:
        stmt = select(User)
