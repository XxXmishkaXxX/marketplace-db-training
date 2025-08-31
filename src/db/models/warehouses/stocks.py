from uuid import UUID
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column


from db.base import Base


class Stock(Base):
    __tablename__ = "stock"

    warehouse_id: Mapped[UUID] = mapped_column(ForeignKey("warehouses.id"), primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    warehouse: Mapped["Warehouse"] = relationship(back_populates="stocks")
    product: Mapped["Product"] = relationship(back_populates="stocks")