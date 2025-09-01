from uuid import UUID
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column


from db.base import Base
from db.models.enums import ShipmentStatus
from db.models.types import uuid_pk



class Shipment(Base):
    __tablename__ = "shipments"

    id: Mapped[uuid_pk]
    order_id: Mapped[UUID] = mapped_column(ForeignKey("orders.id"), nullable=False)
    courier_id: Mapped[UUID] = mapped_column(ForeignKey("couriers.id"), nullable=True)
    warehouse_id: Mapped[UUID] = mapped_column(ForeignKey("warehouses.id"), nullable=False)
    status: Mapped[ShipmentStatus] = mapped_column(Enum(ShipmentStatus), nullable=False)

    warehouse: Mapped["Warehouse"] = relationship(back_populates="shipments")
    order: Mapped["Order"] = relationship("Order", uselist=False)
    courier: Mapped["Courier"] = relationship("Courier", back_populates="shipments", uselist=False)

