from sqlalchemy import Column, ForeignKey, Table

from db.base import Base


warehouses_deliveryzones = Table(
    "warehouses_deliveryzones",
    Base.metadata,
    Column("warehouse_id", ForeignKey("warehouses.id"), primary_key=True),
    Column("delivery_zone_id", ForeignKey("delivery_zones.id"), primary_key=True),
    extend_existing=True
)
