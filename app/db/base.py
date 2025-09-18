from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import create_engine

from app.config import DATABASE_URL


class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)