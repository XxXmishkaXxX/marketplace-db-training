from sqlalchemy import Table, Column, ForeignKey
from db.base import Base


users_roles = Table(
    "users_roles", 
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    extend_existing=True
)
