from decimal import Decimal
from uuid import UUID

from sqlalchemy import Numeric, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.types import uuid_pk, created_at
from db.models.enums import TransactionTypeEnum
from db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[uuid_pk]
    wallet_id: Mapped[UUID] = mapped_column(ForeignKey("wallets.id"), nullable=False)
    type: Mapped[TransactionTypeEnum] = mapped_column(Enum(TransactionTypeEnum), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    created_at: Mapped[created_at]

    wallet: Mapped["Wallet"] = relationship("Wallet", back_populates="transactions")