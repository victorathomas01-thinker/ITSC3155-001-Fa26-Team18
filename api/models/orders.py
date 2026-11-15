from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True, index=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)
    customer_name = Column(String(100), nullable=True)  # compatible with skeleton routes
    description = Column(String(300), nullable=True)
    order_date = Column(DateTime, nullable=False, server_default=func.now())
    tracking_number = Column(String(60), unique=True, nullable=True)
    order_status = Column(String(30), nullable=False, default="pending")
    fulfillment_method = Column(String(20), nullable=True)
    delivery_address = Column(String(300), nullable=True)
    total_price = Column(Numeric(10, 2), nullable=False, default=0)
    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
    reviews = relationship("Review", back_populates="order")
    __table_args__ = (CheckConstraint("total_price >= 0", name="ck_order_total"),)
