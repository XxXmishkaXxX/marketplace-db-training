import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context
from db.base import Base
from db.config_db import settings

from db.models.accounts.users import User
from db.models.accounts.roles import Role
from db.models.accounts.users_roles import users_roles
from db.models.accounts.user_addresses import UserAddress
from db.models.accounts.user_payment_methods import UserPaymentMethod
from db.models.accounts.user_sessions import UserSession
from db.models.catalogs.products import Product, ProductImage
from db.models.catalogs.products_attributes import products_attributes
from db.models.catalogs.attributes import Attribute
from db.models.catalogs.categories import Category
from db.models.catalogs.products_categories import products_categories

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

database_url = settings.DATABASE_URL
if database_url:
    config.set_section_option('alembic', 'sqlalchemy.url', database_url)
else:
    raise ValueError("DATABASE_URL environment variable not set.")

target_metadata = Base.metadata


# -----------------------------
# универсальный render_item для sqlalchemy_utils
# -----------------------------
def render_item(type_, obj, autogen_context):
    if type_ == "type" and obj.__class__.__module__.startswith("sqlalchemy_utils."):
        autogen_context.imports.add(f"import {obj.__class__.__module__}")
        if hasattr(obj, "choices"):
            return f"{obj.__class__.__module__}.{obj.__class__.__name__}(choices={obj.choices})"
        return f"{obj.__class__.__module__}.{obj.__class__.__name__}()"
    return False


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_item=render_item,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_item=render_item,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
