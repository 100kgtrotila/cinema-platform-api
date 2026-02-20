from pgvector import Vector
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Numeric, Boolean

from src.common.models import Base
from decimal import Decimal

from src.modules.catalog.enums import MovieStatus


class Movie(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(String)
    external_id: Mapped[int] | None = mapped_column(Integer, unique=True, nullable=True)
    duration_minutes: Mapped[int] = mapped_column(Integer)
    rating: Mapped[Decimal] = mapped_column(Numeric(3,1))
    poster_url: Mapped[str] | None = mapped_column(String(500), nullable=True)
    trailer_url: Mapped[str] | None= mapped_column(String(500), nullable=True)
    backdrop_url: Mapped[str] | None = mapped_column(String(500), nullable=True)
    description: Mapped[str] = mapped_column(String)
    release_year: Mapped[int] = mapped_column(Integer)
    cast: Mapped[list[str]] = mapped_column(JSONB, default=list)
    id_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    status: Mapped[MovieStatus] = mapped_column(Integer, default=0)
    embedding: Mapped[list[float]] = mapped_column(Vector(768), nullable=True)






