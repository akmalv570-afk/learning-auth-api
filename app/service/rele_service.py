from sqlalchemy.orm import Session

from app.repo.role_repo import get_role_by_name,create_role as create_role_in_db


def create_role(db:Session,role_name:str):
    db_role = get_role_by_name(db,role_name)
    if not db_role:
       return create_role_in_db(db,name=role_name)
    return db_role
