from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.auth_schemas import SingUpDto, TokenResponse, LoginDto
from app.schemas.user_schema import UserResponse
from app.service.auth_service import sing_up,login

router = APIRouter(prefix="/auth",tags=["auth"])


@router.post("/singup",response_model=UserResponse)
def handle_singup(data:SingUpDto,db:Session = Depends(get_db)):
    return sing_up(db,sing_up_dto=data)

@router.post("/login",response_model=TokenResponse)
def handle_singup(data:LoginDto,db:Session = Depends(get_db)):
    return login(db,login_dto=data)