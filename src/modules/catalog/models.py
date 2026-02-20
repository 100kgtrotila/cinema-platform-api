import uuid
from datetime import datetime
from decimal import Decimal

from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Numeric, Boolean, DateTime, ForeignKey

from src.common.models import Base
from src.modules.catalog.enums import MovieStatus, SessionStatus, SeatStatus
from src.modules.pricing.models import Pricing

class Movie(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(String(128))
    slug: Mapped[str | None] = mapped_column(String(32))

    external_id: Mapped[int | None] = mapped_column(Integer, unique=True)
    duration_minutes: Mapped[int] = mapped_column(Integer)
    rating: Mapped[Decimal] = mapped_column(Numeric(3,1))
    poster_url: Mapped[str | None] = mapped_column(String(500))
    trailer_url: Mapped[str | None]= mapped_column(String(500))
    backdrop_url: Mapped[str | None] = mapped_column(String(500))
    description: Mapped[str] = mapped_column(String)
    release_year: Mapped[int] = mapped_column(Integer)
    cast: Mapped[list[str]] = mapped_column(JSONB, default=list)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    status: Mapped[MovieStatus] = mapped_column(Integer, default=0)
    embedding: Mapped[list[float] | None] = mapped_column(Vector(768))

    sessions: Mapped[list["Session"]] = relationship(back_populates="movie")
    movie_genres: Mapped[list["MovieGenre"]] = relationship(back_populates="movie")

class Genre(Base):
    __tablename__ = "genres"

    external_id: Mapped[int | None] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(64))
    slug: Mapped[str | None] = mapped_column(String(32))

    movie_genres: Mapped[list["MovieGenre"]] = relationship(back_populates="genre")

class Hall(Base):
    __tablename__ = "halls"

    name: Mapped[str] = mapped_column(String(64))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    total_capacity: Mapped[int] = mapped_column(Integer)

    sessions: Mapped[list["Session"]] = relationship(back_populates="hall")
    seats: Mapped[list["Seat"]] = relationship(back_populates="hall")
    hall_technologies: Mapped[list["HallTechnology"]] = relationship(back_populates="hall")

class Session(Base):
    __tablename__ = "sessions"

    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[SessionStatus] = mapped_column(Integer, default=0)

    movie_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("movies.id"))
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("halls.id"))
    pricing_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("pricings.id"))

    movie: Mapped["Movie"] = relationship(back_populates="sessions")
    hall: Mapped["Hall"] = relationship(back_populates="sessions")
    pricing: Mapped["Pricing"] = relationship(back_populates="sessions")

class Technology(Base):
    __tablename__ = "technologies"

    name: Mapped[str] = mapped_column(String(64))
    type: Mapped[str] = mapped_column(String(64))

    hall_technologies: Mapped[list["HallTechnology"]] = relationship(back_populates="technology")

class Seat(Base):
    __tablename__ = "seats"

    row_label: Mapped[str] = mapped_column(String(16))
    number: Mapped[int] = mapped_column(Integer)
    grid_x: Mapped[int] = mapped_column(Integer)
    grid_y: Mapped[int] = mapped_column(Integer)
    status: Mapped[SeatStatus] = mapped_column(Integer, default=0)
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("halls.id"))
    seat_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("seat_types.id"))

    hall: Mapped["Hall"] = relationship(back_populates="seats")
    seat_type: Mapped["SeatType"] = relationship(back_populates="seats")

class SeatType(Base):
    __tablename__ = "seat_types"

    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(64))

    seats: Mapped[list["Seat"]] = relationship(back_populates="seat_type")

class HallTechnology(Base):
    __tablename__ = "hall_technologies"

    technology_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("technologies.id"))
    hall_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("halls.id"))

    hall: Mapped["Hall"] = relationship(back_populates="hall_technologies")
    technology: Mapped["Technology"] = relationship(back_populates="hall_technologies")

class MovieGenre(Base):
    __tablename__ = "movie_genres"

    movie_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("movies.id"))
    genre_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("genres.id"))

    movie: Mapped["Movie"] = relationship(back_populates="movie_genres")
    genre: Mapped["Genre"] = relationship(back_populates="movie_genres")