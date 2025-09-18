from sqlalchemy.orm import Session
from app.models.users import User
from app.service.rele_service import create_role
from app.schemas.user_schema import UserCreate


def add_user(db:Session,user_create_dto:UserCreate):
    db_user = User(**user_create_dto.model_dump())
    db_user_role = create_role(db,"USER")
    db_user.roles.append(db_user_role)

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user

def add_admin(db:Session,user_create_dto:UserCreate):
    db_admin = User(**user_create_dto.model_dump())
    db_admin_role = create_role(db,"ADMIN")
    db_admin.roles.append(db_admin_role)

    db.add(db_admin)

    db.commit()

    db.refresh(db_admin)

    return db_admin

def get_user_by_username(db:Session,username:str):
    return db.query(User).filter_by(username=username).first()

