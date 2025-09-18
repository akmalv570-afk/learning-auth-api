from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.repo.user_repo import get_user_by_username
from app.schemas.auth_schemas import SingUpDto, LoginDto, TokenResponse
from app.repo import user_repo
from app.schemas.token_schemas import TokenData
from app.schemas.user_schema import UserCreate
from app.security.jwt_utils import create_access_token, create_refrash_token
from app.security.password_utils import hash_password, verifiy_password


def sing_up(db:Session,sing_up_dto:SingUpDto):
    db_user = get_user_by_username(db,username = sing_up_dto.username)
    if db_user:
        raise ValueError("Username is already exists")
    user_create = UserCreate(username=sing_up_dto.username,password=hash_password(sing_up_dto.password))
    return user_repo.add_user(db,user_create)

def add_admin(db:Session,sing_up_dto:SingUpDto):
    db_admin = get_user_by_username(db,username = sing_up_dto.username)
    if db_admin:
        raise ValueError("Username is already exists")
    user_create = UserCreate(username=sing_up_dto.username,password=hash_password(sing_up_dto.password))
    return user_repo.add_admin(db,user_create)

def login(db:Session,login_dto:LoginDto):
    db_user = get_user_by_username(db,username = login_dto.username)

    if not db_user or not verifiy_password(login_dto.password,db_user.password):
        raise HTTPException(status_code=401,detail="Username or Password is not valid")

    roles = [role.name for role in db_user.roles]

    access_token = create_access_token(TokenData(username=db_user.username,user_id=db_user.id,roles = roles))
    refresh_token = create_refrash_token(db_user.id)

    return TokenResponse(access_token=access_token,refresh_token=refresh_token)

