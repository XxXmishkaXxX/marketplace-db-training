from decimal import Decimal
from uuid import UUID

from sqlalchemy import Numeric, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.types import uuid_pk, created_at
from db.models.enums import PayoutStatusEnum
from db.base import Base


class Payout(Base):
    __tablename__ = "payouts"

    id: Mapped[uuid_pk]
    seller_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[PayoutStatusEnum] = mapped_column(Enum(PayoutStatusEnum), default=PayoutStatusEnum.pending, nullable=False)
    created_at: Mapped[created_at]

    seller: Mapped["User"] = relationship("User")
