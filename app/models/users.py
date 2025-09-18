from sqlalchemy import String, Integer, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column, Column

from app.db.base import Base

users_roles = Table(
    "users_roles",
    Base.metadata,
    Column("user_id",Integer,ForeignKey("users.id")),
    Column("roles_id",Integer,ForeignKey("roles.id"))

)


class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer,primary_key = True)
    username:Mapped[str] = mapped_column(String,unique = True)
    password:Mapped[str] = mapped_column(String)

    roles:Mapped[list["Role"]] = relationship("Role",secondary=users_roles)

class Role(Base):

    __tablename__ = "roles"
    id:Mapped[int] = mapped_column(Integer,primary_key = True)
    name:Mapped[str] = mapped_column(String,unique = True)