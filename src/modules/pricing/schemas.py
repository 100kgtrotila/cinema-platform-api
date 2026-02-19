from decimal import Decimal
from typing import NewType
from uuid import UUID

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
    name: str | None  = Field(default=None, min_length=3, max_length=64, description="Pricing name")

class PricingResponse(PricingBase, ORMBaseSchema):
    id: PricingId


# PRICING ITEMS
class PricingItemBase(BaseModel):
    price: Decimal = Field(..., gt=1, description="Price")
    pricing_id: PricingId = Field(...)
    seat_type_id: SeatTypeId = Field(...)
    day_of_week: int = Field(ge=1, le=7, description="Day of week")
    start_time: AwareDatetime = Field(...)
    end_time: AwareDatetime = Field(...)

class PricingItemCreate(PricingItemBase):
    pass

class PricingItemUpdate(BaseModel):
    price: Decimal | None = Field(default=None, gt=1, description="Price")
    pricing_id: PricingId | None = Field(default=None)
    seat_type_id: SeatTypeId | None = Field(default=None)
    day_of_week: int | None = Field(default=None, ge=1, le=7, description="Day of week")
    star_time: AwareDatetime | None = Field(default=None)
    end_time: AwareDatetime | None = Field(default=None)

class PricingItemResponse(PricingItemBase, ORMBaseSchema):
    id: PricingItemId