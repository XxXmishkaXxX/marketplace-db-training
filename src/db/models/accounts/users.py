from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
from .users_roles import users_roles

#types
from typing import List
from datetime import datetime
from sqlalchemy import Boolean, Date
from sqlalchemy_utils import PasswordType, EmailType, PhoneNumberType
from models.types import uuid_pk, str256_not_null


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    name: Mapped[str256_not_null]
    email: Mapped[str] = mapped_column(EmailType, nullable=False, index=True)
    phone_number: Mapped[str] = mapped_column(PhoneNumberType(region="RU"), nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(
        PasswordType(schemes=['bcrypt'], deprecated='auto'),
        nullable=False
    )
    date_of_birth: Mapped[Date] = mapped_column(Date, nullable=True)
    created_at: Mapped[datetime] = mapped_column(Date, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(Date, default=datetime.utcnow, onupdate=datetime.utcnow)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    

    #N:M
    roles: Mapped[List["Role"]] = relationship(
        "Role",
        secondary=users_roles,
        back_populates="users"
    )

    #1:M
    addresses: Mapped[List["UserAddress"]] = relationship(
        "UserAddress",
        back_populates="users",
        cascade="all, delete-orphan"
    )
    sessions: Mapped[List["UserSession"]] = relationship(
        "UserSession",
        back_populates="users",
        cascade="all, delete-orphan"
    )
    payment_methods: Mapped[List["UserPaymentMethod"]] = relationship(
        "UserPaymentMethod",
        back_populates="users",
        cascade="all, delete-orphan"
    )