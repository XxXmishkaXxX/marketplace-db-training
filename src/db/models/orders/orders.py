from uuid import UUID
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from db.models.types import uuid_pk, created_at
from db.models.enums import OrderStatusEnum


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[uuid_pk]
    buyer_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[OrderStatusEnum] = mapped_column(Enum(OrderStatusEnum), default=OrderStatusEnum.pending, nullable=False)
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[created_at]

    buyer: Mapped["User"] = relationship("User", back_populates="orders")
    items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    status_history: Mapped[list["OrderStatusHistory"]] = relationship("OrderStatusHistory", back_populates="order", cascade="all, delete-orphan")
    payments: Mapped[list["UserPaymentMethod"]] = relationship("UserPaymentMethod", back_populates="order")
    shipment: Mapped["Shipment"] = relationship(back_populates="order", uselist=False)
