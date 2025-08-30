from uuid import UUID
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.types import uuid_pk, created_at
from models.enums import RefundStatusEnum


class Refund(Base):
    __tablename__ = "refunds"

    id: Mapped[uuid_pk]
    payment_id: Mapped[UUID] = mapped_column(ForeignKey("payments.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[RefundStatusEnum] = mapped_column(Enum(RefundStatusEnum), default=RefundStatusEnum.pending, nullable=False)
    created_at: Mapped[created_at]

    payment: Mapped["Payment"] = relationship("Payment", back_populates="refunds")