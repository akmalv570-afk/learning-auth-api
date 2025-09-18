from typing import List

from pydantic import BaseModel


class UserCreate(BaseModel):
    username:str
    password:str


class RoleResponse(BaseModel):
    name:str

class UserResponse(BaseModel):
    id:int
    username:str
    roles:List[RoleResponse]

