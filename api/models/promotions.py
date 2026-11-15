from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_percent = Column(Numeric(5, 2), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    orders = relationship("Order", back_populates="promotion")
    __table_args__ = (CheckConstraint("discount_percent >= 0 AND discount_percent <= 100", name="ck_promotion_discount"),)
