import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import String, NUMERIC, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.common.models import Base


class Pricing(Base):
    __tablename__ = "pricing"

    name: Mapped[str] = mapped_column(String(150), unique=True)

class PricingItem(Base):
    __tablename__ = "pricing_items"

    price: Mapped[Decimal] = mapped_column(NUMERIC)
    pricing_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pricing.id"))
    seat_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("seat_types.id"))
    day_of_week: Mapped[int] = mapped_column(Integer)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))