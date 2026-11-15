from sqlalchemy import Column, Integer, String, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=False)
    price = Column(Numeric(10, 2), nullable=False, default=0)
    calories = Column(Integer, nullable=True)
    food_category = Column(String(80), nullable=True)
    description = Column(String(500), nullable=True)
    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")
    reviews = relationship("Review", back_populates="sandwich")
    __table_args__ = (CheckConstraint("price >= 0", name="ck_sandwich_price"), CheckConstraint("calories IS NULL OR calories >= 0", name="ck_sandwich_calories"))
