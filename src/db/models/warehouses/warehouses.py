from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column


from db.base import Base
from models.types import uuid_pk, str256_not_null
from models.enums import WarehouseType
from models.warehouses.warehouses_deliveryzones import warehouses_deliveryzones


class Warehouse(Base):
    __tablename__ = "warehouses"

    id: Mapped[uuid_pk]
    name: Mapped[str256_not_null]
    address: Mapped[str256_not_null]
    type: Mapped[WarehouseType] = mapped_column(Enum(WarehouseType), nullable=False)

    stocks: Mapped[list["Stock"]] = relationship(back_populates="warehouse")
    shipments: Mapped[list["Shipment"]] = relationship(back_populates="warehouse")
    delivery_zones: Mapped[list["DeliveryZone"]] = relationship(
        "DeliveryZone",
        secondary=warehouses_deliveryzones,
        back_populates="warehouses"
    )