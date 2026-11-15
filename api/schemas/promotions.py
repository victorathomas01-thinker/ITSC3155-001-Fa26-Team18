from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class PromotionBase(BaseModel):
    code: str
    discount_percent: Decimal = Field(ge=0, le=100)
    expires_at: datetime
    is_active: bool = True

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    discount_percent: Optional[Decimal] = Field(default=None, ge=0, le=100)
    expires_at: Optional[datetime] = None
    is_active: Optional[bool] = None

class Promotion(PromotionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
