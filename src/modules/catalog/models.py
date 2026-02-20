from datetime import datetime

from pgvector import Vector
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Numeric, Boolean, DateTime, ForeignKey

from src.common.models import Base
from decimal import Decimal

from src.modules.catalog.enums import MovieStatus, SessionStatus
from src.modules.pricing.models import Pricing


class Movie(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(String(128))
    slug: Mapped[str] = mapped_column(String(32), nullable=True)

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

    session: Mapped[Session] = relationship(back_populates="movies")

class Genre(Base):
    __tablename__ = "genres"

    external_id: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(String(64))
    slug: Mapped[str] = mapped_column(String(32), nullable=True)

class Hall(Base):
    __tablename__ = "halls"

    name: Mapped[str] = mapped_column(String(64))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    total_capacity: Mapped[int] = mapped_column(Integer)

    session: Mapped[Session] = relationship(back_populates="halls")

class Session(Base):
    __tablename__ = "sessions"

    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[SessionStatus] = mapped_column(Integer, default=0)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    hall_id: Mapped[int] = mapped_column(ForeignKey("halls.id"))
    pricing_id: Mapped[int] = mapped_column(ForeignKey("pricing.id"))

    movies: Mapped[Movie] = relationship(back_populates="sessions")
    hall: Mapped[Hall] = relationship(back_populates="sessions")
    pricing: Mapped[Pricing] = relationship(back_populates="sessions")





