from uuid import UUID
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from db.models.types import uuid_pk, created_at
from db.models.enums import RefundStatusEnum


class Refund(Base):
    __tablename__ = "refunds"

    id: Mapped[uuid_pk]
    payment_id: Mapped[UUID] = mapped_column(ForeignKey("user_payment_methods.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[RefundStatusEnum] = mapped_column(Enum(RefundStatusEnum), default=RefundStatusEnum.pending, nullable=False)
    created_at: Mapped[created_at]

    payment: Mapped["UserPaymentMethod"] = relationship("PaymeUserPaymentMethod", back_populates="refunds")