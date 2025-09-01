from typing import List
from sqlalchemy.orm import Mapped, relationship


from db.models.types import uuid_pk, str32_not_null
from db.base import Base
from db.models.catalogs.products_attributes import products_attributes 




class Attribute(Base):
    __tablename__ = "attributes"

    id: Mapped[uuid_pk]
    key_name: Mapped[str32_not_null]
    value: Mapped[str32_not_null]

    products: Mapped[List["Product"]] = relationship("Product", 
                                                     secondary=products_attributes,
                                                     back_populates="attributes")
