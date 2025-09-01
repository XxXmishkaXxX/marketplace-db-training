from typing import List
from decimal import Decimal
from uuid import UUID

from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import CurrencyType


from db.models.types import uuid_pk, str256_not_null, str500_not_null
from db.base import Base
from db.models.catalogs.products_categories import products_categories
from db.models.catalogs.products_attributes import products_attributes


class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid_pk]
    seller_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)

    name: Mapped[str256_not_null]
    description: Mapped[str500_not_null]
    price: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    currency: Mapped[str] = mapped_column(CurrencyType, default='RUB', nullable=False)
    rating: Mapped[float] = mapped_column(default=0.0, nullable=False)
    stock: Mapped[int] = mapped_column(default=0, nullable=False)

    seller: Mapped["User"] = relationship("User", back_populates="products")
    images: Mapped[List["ProductImage"]] = relationship("ProductImage",
                                                        back_populates="product",
                                                        cascade="all, delete-orphan")
    categories: Mapped[List["Category"]] = relationship(
        "Category",
        secondary=products_categories,
        back_populates="product"
    )
    attributes: Mapped[List["Attribute"]] = relationship(
        "Attribute",
        secondary=products_attributes,
        back_populates="products"
    )
    stocks: Mapped[List["Stock"]] = relationship(
        "Stock",
        back_populates="product")



class ProductImage(Base):
    __tablename__ = "product_images"

    id: Mapped[uuid_pk]
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"), nullable=False)
    
    url: Mapped[str500_not_null]
    position: Mapped[int] = mapped_column(default=0, nullable=False)

    product: Mapped["Product"] = relationship("Product", back_populates="images")