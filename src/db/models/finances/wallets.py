from typing import List
from decimal import Decimal
from uuid import UUID

from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import CurrencyType

from models.types import uuid_pk
from db.base import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[uuid_pk]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0, nullable=False)
    currency: Mapped[str] = mapped_column(CurrencyType, default="RUB", nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="wallet", uselist=False)
    transactions: Mapped[List["Transaction"]] = relationship(
        "Transaction", back_populates="wallet", cascade="all, delete-orphan"
    )