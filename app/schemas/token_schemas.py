from typing import List

from pydantic import BaseModel


class TokenData(BaseModel):
    user_id:int
    username:str
    roles:List[str]