import secrets
import hashlib
from uuid import UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey

from db.base import Base
from db.models.types import uuid_pk, str128, str64

class UserSession(Base):
    __tablename__ = "users_sessions"
    id: Mapped[uuid_pk]

    token_hash: Mapped[str] = mapped_column(nullable=False, unique=True)

    device_info: Mapped[str128 | None]
    ip_address: Mapped[str64 | None]
    expires_at: Mapped[datetime]

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="sessions")

    @staticmethod
    def generate_token() -> tuple[str, str]:
        """
        Создает новый токен и возвращает его вместе с хэшем для сохранения в БД.

        :return: (token_plain, token_hash)
        """
        token_plain = secrets.token_urlsafe(64)
        token_hash = hashlib.sha256(token_plain.encode()).hexdigest()
        return token_plain, token_hash