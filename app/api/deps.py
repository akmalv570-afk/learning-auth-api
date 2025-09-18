from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer

from app.db.base import Session
from app.schemas.token_schemas import TokenData
from app.security.jwt_utils import verify_access_token

security = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(token:str = Depends(security)):
    return verify_access_token(token)

def is_admin(current_user:TokenData = Depends(get_current_user)):
    if "ADMIN" not in current_user.roles:
        raise HTTPException(status_code=403,detail="U are not allowed")
    return current_user

def get_db():
    db = Session()
    try:
        yield db
    finally:db.close()