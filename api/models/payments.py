from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    payment_type = Column(String(40), nullable=False)
    transaction_status = Column(String(40), nullable=False, default="pending")
    transaction_reference = Column(String(100), unique=True, nullable=True)
    card_last_four = Column(String(4), nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    order = relationship("Order", back_populates="payments")
    __table_args__ = (CheckConstraint("amount >= 0", name="ck_payment_amount"),)
