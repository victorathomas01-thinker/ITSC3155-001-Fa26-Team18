from sqlalchemy import Column, ForeignKey, Integer, Numeric, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), nullable=False)
    resource_id = Column(Integer, ForeignKey("resources.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")
    __table_args__ = (UniqueConstraint("sandwich_id", "resource_id", name="uq_recipe_ingredient"), CheckConstraint("amount > 0", name="ck_recipe_amount"))
