import enum


class OrderStatusEnum(enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    completed = "completed"
    cancelled = "cancelled"
    refunded = "refunded"


class PaymentStatusEnum(enum.Enum):
    pending = "pending"
    success = "success"
    failed = "failed"


class RefundStatusEnum(enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    processed = "processed"


class WarehouseType(enum.Enum):
    MAIN = "main"
    PICKUP = "pickup"
    PARTNER = "partner"


class ShipmentStatus(enum.Enum):
    COLLECTED = "collected"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
