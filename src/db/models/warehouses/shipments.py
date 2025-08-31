from uuid import UUID
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column


from db.base import Base
from models.enums import ShipmentStatus
from models.types import uuid_pk



class Shipment(Base):
    __tablename__ = "shipments"

    id: Mapped[uuid_pk]
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"), nullable=False)
    warehouse_id: Mapped[UUID] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
    status: Mapped[ShipmentStatus] = mapped_column(Enum(ShipmentStatus), nullable=False)

    warehouse: Mapped["Warehouse"] = relationship(back_populates="shipments")
    order: Mapped["Order"] = relationship(back_populates="shipments")
    courier: Mapped["Courier"] = relationship(back_populates="shipments")

