from decimal import Decimal
from uuid import UUID

from sqlalchemy import Numeric, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.types import uuid_pk, created_at
from models.enums import InvoiceStatusEnum
from db.base import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[InvoiceStatusEnum] = mapped_column(Enum(InvoiceStatusEnum), default=InvoiceStatusEnum.pending, nullable=False)
    created_at: Mapped[created_at]

    user: Mapped["User"] = relationship("User", back_populates="invoices")