from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from uuid import UUID

from db.base import Base
from models.types import uuid_pk, str256_not_null

class UserAddress(Base):
    __tablename__ = "users_adresses"
    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    city: Mapped[str256_not_null] 
    street: Mapped[str256_not_null]
    house_number: Mapped[str256_not_null]
    apartment: Mapped[str256_not_null]

    is_default: Mapped[bool] = mapped_column(default=False, nullable=False)

    user: Mapped["User"] = relationship(back_populates="users")