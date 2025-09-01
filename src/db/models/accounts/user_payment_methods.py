from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, Boolean, ForeignKey
from datetime import date
from uuid import UUID

from db.base import Base
from db.models.types import uuid_pk, str256_not_null

class UserPaymentMethod(Base):
    __tablename__ = "user_payment_methods"

    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)

    payment_type: Mapped[str256_not_null]
    provider: Mapped[str256_not_null]
    account_number_masked: Mapped[str256_not_null]
    expiration_date: Mapped[date] = mapped_column(Date, nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="payment_methods")
