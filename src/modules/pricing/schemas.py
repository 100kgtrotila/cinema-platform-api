from uuid import UUID
from decimal import Decimal

from mypy.types import NewType
from pydantic import BaseModel, Field, AwareDatetime

from src.common.schemas import ORMBaseSchema
from src.modules.catalog.schemas import SeatTypeId

PricingId = NewType("PricingId", UUID)
PricingItemId = NewType("PricingItemId", UUID)



# PRICING
class PricingBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=64, description="Pricing name")

class PricingCreate(PricingBase):
    pass

class PricingUpdate(BaseModel):
    name: str  = Field(..., min_length=3, max_length=64, description="Pricing name")

class PricingResponse(PricingBase, ORMBaseSchema):
    id: PricingId


# PRICING ITEMS
class PricingItemBase(BaseModel):
    price: Decimal = Field(..., gt=1, description="Price")
    pricing_id: PricingId = Field(...)
    seat_type_id: SeatTypeId = Field(...)
    day_of_week: int = Field(ge=1, le=7, description="Day of week")
    star_time: AwareDatetime = Field(...)
    end_time: AwareDatetime = Field(...)

class PricingItemCreate(PricingItemBase):
    pass

class PricingItemUpdate(BaseModel):
    price: Decimal = Field(default=None, gt=1, description="Price")
    pricing_id: PricingId = Field(default=None)
    seat_type_id: SeatTypeId = Field(default=None)
    day_of_week: int = Field(default=None, ge=1, le=7, description="Day of week")
    star_time: AwareDatetime = Field(default=None)
    end_time: AwareDatetime = Field(default=None)

class PricingItemResponse(PricingItemId, ORMBaseSchema):
    id: PricingItemId