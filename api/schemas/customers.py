from pydantic import BaseModel, ConfigDict
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
