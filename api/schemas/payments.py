from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    transaction_status: str = "pending"
    amount: Decimal = Field(ge=0)
    transaction_reference: Optional[str] = None
    card_last_four: Optional[str] = Field(default=None, pattern=r"^\d{4}$")

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    transaction_status: Optional[str] = None
    transaction_reference: Optional[str] = None

class Payment(PaymentBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
