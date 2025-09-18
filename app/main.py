import uvicorn
from fastapi import FastAPI
from app.api import auth_api,user_api,deps
from app.db.base import Base, engine, Session
from app.schemas.auth_schemas import SingUpDto
from app.service.auth_service import add_admin

Base.metadata.create_all(engine)
app = FastAPI()

# with Session() as session:
#     add_admin(session,SingUpDto(username="akmal",password="admin "))

app.include_router(auth_api.router)
app.include_router(user_api.router)

uvicorn.run(app)