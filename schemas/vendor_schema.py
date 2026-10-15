from datetime import datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel,ConfigDict,EmailStr,Field

class VendorCreate(BaseModel):
    business_name:str = Field(min_length=2,max_length=150)
    email:EmailStr
    phone:str = Field(min_length=7,max_length=30)
    business_category:str = Field(min_length=2,max_length=150)
    commission_rate:Decimal = Field(default = Decimal("10.00"),ge=0,le=100,max_digits=5,decimal_places=2) 


class VendorRead(BaseModel):
    id:int
    business_name:str
    email: EmailStr
    phone:str
    buniness_category:str
    commission_rate:Decimal
    status: Literal["pending", "approved", "rejected", "suspended"]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
