from uuid import UUID
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from db.base import Base
from db.models.types import uuid_pk


class OrderPayment(Base):
    __tablename__ = "orders_payments"

    id: Mapped[uuid_pk]
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"))
    payment_method_id: Mapped[UUID] = mapped_column(ForeignKey("user_payment_methods.id"))
    amount: Mapped[float] = mapped_column()
    paid_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    order: Mapped["Order"] = relationship("Order", back_populates="payments")
    payment_method: Mapped["UserPaymentMethod"] = relationship("UserPaymentMethod")
