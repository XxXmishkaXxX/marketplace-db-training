from sqlalchemy import Table, Column, ForeignKey
from db.base import Base



products_attributes = Table(
    "products_attributes", 
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("attribute_id", ForeignKey("attributes.id"), primary_key=True),
    extend_existing=True
)
