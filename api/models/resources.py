from sqlalchemy import Column, Integer, String, Numeric, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False, default=0)
    unit = Column(String(30), nullable=False, default="units")
    recipes = relationship("Recipe", back_populates="resource")
    __table_args__ = (CheckConstraint("amount >= 0", name="ck_resource_amount"),)
