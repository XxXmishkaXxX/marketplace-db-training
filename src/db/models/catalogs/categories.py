from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from db.models.types import uuid_pk, str256_not_null
from db.base import Base
from db.models.catalogs.products_categories import products_categories



class Category(Base):
    __tablename__ = "categories"
    id: Mapped[uuid_pk]
    name: Mapped[str256_not_null]

    parent_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    parent: Mapped["Category"] = relationship("Category", remote_side=[id], backref="children") 

    products: Mapped[List["Product"]] = relationship("Product",
                                                     secondary=products_categories,
                                                     back_populates="categories")
