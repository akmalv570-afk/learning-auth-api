from sqlalchemy.orm import Session

from app.models.users import Role


def create_role(db:Session,name:str):
    db_role = Role(name=name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role_by_name(db:Session,role_name:str):
    return db.query(Role).filter_by(name = role_name).first()