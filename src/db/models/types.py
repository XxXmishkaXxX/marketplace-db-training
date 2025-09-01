from uuid import UUID, uuid4
from typing import Annotated
from datetime import datetime

from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Date
from db.base import Base




uuid_pk = Annotated[UUID, mapped_column(primary_key=True, default=uuid4)]
created_at = Annotated[datetime, mapped_column(Date, default=datetime.utcnow)] 

str256_not_null = Annotated[str, mapped_column(String(256), nullable=False)]
str500_not_null = Annotated[str, mapped_column(String(500), nullable=False)]
str64_not_null = Annotated[str, mapped_column(String(64), nullable=False)]
str32_not_null = Annotated[str, mapped_column(String(32), nullable=False)]
str500 = Annotated[str, 500]
str256 = Annotated[str, 256]
str128 = Annotated[str, 128]
str64 = Annotated[str, 64]


Base.type_annotation_map = {
    str500: String(500),
    str256: String(256),
    str128: String(128),
    str64: String(64)
    }