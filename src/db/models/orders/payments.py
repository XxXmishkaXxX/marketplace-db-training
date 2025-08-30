from uuid import UUID
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.types import uuid_pk, str64_not_null, created_at
from models.enums import PaymentStatusEnum



class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[uuid_pk]
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[PaymentStatusEnum] = mapped_column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.pending, nullable=False)
    provider: Mapped[str64_not_null]
    created_at: Mapped[created_at]

    order: Mapped["Order"] = relationship("Order", back_populates="payments")
    refunds: Mapped[list["Refund"]] = relationship("Refund", back_populates="payment", cascade="all, delete-orphan")
