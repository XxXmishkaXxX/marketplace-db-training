# src/db/models/__init__.py

# --- Accounts ---
from .accounts.users import User
from .accounts.roles import Role
from .accounts.users_roles import users_roles
from .accounts.user_addresses import UserAddress
from .accounts.user_sessions import UserSession
from .accounts.user_payment_methods import UserPaymentMethod

# --- Orders ---
from .orders.orders import Order
from .orders.orders_items import OrderItem
from .orders.orders_status_history import OrderStatusHistory
from .orders.refunds import Refund
from .orders.orders_payments import OrderPayment

# --- Catalogs ---
from .catalogs.products import Product, ProductImage
from .catalogs.attributes import Attribute
from .catalogs.categories import Category
from .catalogs.products_attributes import products_attributes
from .catalogs.products_categories import  products_categories 

# --- Finances ---
from .finances.wallets import Wallet
from .finances.invoices import Invoice
from .finances.payouts import Payout
from .finances.transactions import Transaction

# --- Warehouses ---
from .warehouses.warehouses import Warehouse
from .warehouses.couriers import Courier
from .warehouses.delivery_zones import DeliveryZone
from .warehouses.shipments import Shipment
from .warehouses.stocks import Stock
from .warehouses.warehouses_deliveryzones import warehouses_deliveryzones

