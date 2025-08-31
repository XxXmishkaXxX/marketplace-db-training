from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Float

from db.base import Base
from models.types import uuid_pk, str256_not_null
from models.warehouses.warehouses_deliveryzones import warehouses_deliveryzones


class DeliveryZone(Base):
    __tablename__ = "delivery_zones"

    id: Mapped[uuid_pk]
    city: Mapped[str256_not_null]
    region: Mapped[str256_not_null]
    country: Mapped[str256_not_null]
    delivery_cost: Mapped[float] = mapped_column(Float, nullable=False)

    warehouses: Mapped[list["Warehouse"]] = relationship(
        "Warehouse",
        secondary=warehouses_deliveryzones,
        back_populates="delivery_zones"
    )
