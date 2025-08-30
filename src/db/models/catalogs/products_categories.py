from sqlalchemy import Table, Column, ForeignKey
from db.base import Base



products_categories = Table(
    "products_categories", 
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
    extend_existing=True
)
