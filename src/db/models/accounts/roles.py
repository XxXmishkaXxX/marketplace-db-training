from typing import List
from db.base import Base
from sqlalchemy.orm import Mapped, relationship
from db.models.types import uuid_pk, str256_not_null, str500
from db.models.accounts.users_roles import users_roles

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[uuid_pk]
    name: Mapped[str256_not_null]
    description: Mapped[str500]

    users: Mapped[List["User"]] = relationship(
        "User",
        secondary=users_roles,
        back_populates="roles"
    )
     