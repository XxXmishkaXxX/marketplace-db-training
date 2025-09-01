from uuid import UUID
from datetime import datetime
from sqlalchemy import ForeignKey, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from db.models.types import uuid_pk
from db.models.enums import OrderStatusEnum


class OrderStatusHistory(Base):
    __tablename__ = "order_status_history"

    id: Mapped[uuid_pk]
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"), nullable=False)
    status: Mapped[OrderStatusEnum] = mapped_column(Enum(OrderStatusEnum), nullable=False)
    changed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="status_history")
