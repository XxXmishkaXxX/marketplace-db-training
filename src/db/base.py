from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


from db.config_db import settings


engine = create_async_engine(settings.DATABASE_URL_ASYNC, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

sync_engine = create_engine(settings.DATABASE_URL_SYNC)
sync_session = sessionmaker(
    sync_engine, expire_on_commit=False
)

class Base(DeclarativeBase):
    type_annotation_map = {}