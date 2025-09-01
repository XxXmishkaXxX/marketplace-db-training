from uuid import UUID
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column


from db.base import Base
from db.models.types import uuid_pk, str256_not_null


class Courier(Base):
    __tablename__ = "couriers"

    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    name: Mapped[str256_not_null]
    transport: Mapped[str256_not_null]
    rating: Mapped[float] = mapped_column(Float, nullable=True)

    user: Mapped["User"] = relationship(back_populates="courier_profile")
    assignments: Mapped[list["CourierAssignment"]] = relationship(back_populates="courier")