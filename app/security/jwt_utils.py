from fastapi import HTTPException
from jose import jwt, ExpiredSignatureError, JWTError
from jose.constants import Algorithms

from app.config import ACCESS_TOKEN_EXPIRE_TIME_MINUTES, ACCESS_TOKEN_SECRET_KEY, REFRESH_TOKEN_SECRET_KEY,REFRESH_TOKEN_EXPIRE_TIME_DAY
from app.schemas.token_schemas import TokenData
from datetime import datetime, timezone,timedelta

ALGORITHM = Algorithms.HS256

def now():
    return datetime.utcnow()

def create_access_token(claim:TokenData):
    claim = claim.model_copy()

    sub = claim.user_id
    expires = now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME_MINUTES)
    issued_at = now()

    to_encode = claim.model_dump()
    to_encode.update({"exp":expires,"iat":issued_at})
    return  jwt.encode(to_encode,ACCESS_TOKEN_SECRET_KEY,ALGORITHM)

def create_refrash_token(user_id:int):
    sub = user_id
    expires = now() + timedelta(days=REFRESH_TOKEN_EXPIRE_TIME_DAY)
    issued_at = now()

    to_encode = {"exp":expires,"iat":issued_at,"sub":str(sub)}

    return jwt.encode(to_encode,REFRESH_TOKEN_SECRET_KEY,ALGORITHM)

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token,ACCESS_TOKEN_SECRET_KEY,ALGORITHM)
        if not payload.get("username") or not payload.get("user_id"):
            raise HTTPException(status_code=401,detail="Token is invalid")

        return TokenData(username=payload.get("username"),user_id=payload.get("user_id"),roles = payload.get("roles"))
    except ExpiredSignatureError:
        raise HTTPException(status_code=401,detail="Token is expired")
    except JWTError:
        raise HTTPException(status_code=401,detail="Token is invalide")








