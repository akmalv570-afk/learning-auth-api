from pydantic import BaseModel

class SingUpDto(BaseModel):
    username:str
    password:str

class LoginDto(BaseModel):
    username:str
    password:str
class TokenResponse(BaseModel):
        access_token:str
        refresh_token:str
