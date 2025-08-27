from uuid import UUID, uuid4
from typing import Annotated

from sqlalchemy.orm import mapped_column
from sqlalchemy import String




uuid_pk = Annotated[UUID, mapped_column(primary_key=True, default=uuid4)]
str256_not_null = Annotated[str, mapped_column(String(256), nullable=False)]
str500 = Annotated[str, 500]




map = {
    str500: String(500)
    }