from sqlalchemy import Column, ForeignKey, Integer, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=True)
    sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
    __table_args__ = (CheckConstraint("amount > 0", name="ck_detail_amount"),)
