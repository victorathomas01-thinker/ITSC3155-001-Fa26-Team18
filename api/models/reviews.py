from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False, index=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    rating = Column(Integer, nullable=False)
    review_text = Column(String(1500), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    customer = relationship("Customer", back_populates="reviews")
    sandwich = relationship("Sandwich", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")
    __table_args__ = (CheckConstraint("rating >= 1 AND rating <= 5", name="ck_review_rating"),)
