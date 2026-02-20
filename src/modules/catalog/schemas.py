from typing import NewType
from uuid import UUID

from pydantic import BaseModel, Field, AwareDatetime

from src.common.schemas import ORMBaseSchema
from src.modules.catalog.enums import MovieStatus

#CUSTOM UUIDS
MovieId = NewType("MovieId", UUID)
GenreId = NewType("GenreId", UUID)
HallId = NewType("HallId", UUID)
SessionId = NewType("SessionId", UUID)
TechnologyId = NewType("TechnologyId", UUID)
SeatId = NewType("SeatId", UUID)
SeatTypeId = NewType("SeatTypeId", UUID)


# MOVIE SCHEMAS
class MovieBase(BaseModel):
    external_id: int | None = Field(default=None, description="TMDB ID")
    title: str = Field(..., min_length=1, max_length=128, description="Movie title")
    duration_minutes: int = Field(..., ge=2, description="Movie duration")
    rating: float = Field(..., ge=0.0, le=10.0, description="Movie rating")
    poster_url: str | None = Field(default=None)
    trailer_url: str | None = Field(default=None)
    backdrop_url: str | None = Field(default=None)
    description: str = Field(..., min_length=32, max_length=512, description="Movie description")
    release_year: int = Field(..., gt=0)
    cast: list[str]
    is_deleted: bool = Field(default=False)
    status: MovieStatus = Field(default=MovieStatus.COMING_SOON)
    slug: str | None = Field(default=None, min_length=1, max_length=32)

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    external_id: int | None = Field(default=None, description="TMDB ID")
    title: str | None = Field(default=None, min_length=1, max_length=128, description="Movie title")
    duration_minutes: int | None = Field(default=None, gt=1, description="Movie duration")
    rating: float | None = Field(default=None, ge=0.0, description="Movie rating")
    poster_url: str | None = Field(default=None)
    trailer_url: str | None = Field(default=None)
    backdrop_url: str | None = Field(default=None)
    description: str | None = Field(default=None, min_length=32, max_length=512, description="Movie description")
    release_year: int | None = Field(default=None, gt=0)
    cast: list[str] | None = Field(default=None)
    is_deleted: bool | None = Field(default=None)
    status: MovieStatus | None = Field(default=None)
    slug: str | None = Field(default=None, min_length=1, max_length=32)

class MovieResponse(MovieBase, ORMBaseSchema):
    id: MovieId


# MOVIE GENRES
class GenreBase(BaseModel):
    external_id: int | None = Field(default=None, description="TMDB ID")
    name: str = Field(..., min_length=3, max_length=64, description="Genre name")
    slug: str | None = Field(default=None, min_length=1, max_length=32)

class GenreCreate(GenreBase):
    pass

class GenreUpdate(BaseModel):
    external_id: int | None = Field(default=None, description="TMDB ID")
    name: str | None = Field(default=None, min_length=3, max_length=64, description="Genre name")
    slug: str | None = Field(default=None, min_length=1, max_length=32)

class GenreResponse(GenreBase, ORMBaseSchema):
    id: GenreId


# HALLS
class HallBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=64, description="Hall name")
    is_active: bool = Field(default=True)
    total_capacity: int = Field(..., gt=6, description="Hall capacity")

class HallCreate(HallBase):
    pass

class HallUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=64, description="Hall name")
    is_active: bool | None = Field(default=None)
    total_capacity: int | None = Field(default=None, gt=6, description="Hall capacity")

class HallResponse(HallBase, ORMBaseSchema):
    id: HallId


# SESSIONS
class SessionBase(BaseModel):
    start_time: AwareDatetime
    end_time: AwareDatetime
    status: SessionStatus = Field(default=SessionStatus.PLANNED)
    movie_id: MovieId
    hall_id: HallId
    pricing_id: PricingId

class SessionCreate(SessionBase):
    pass

class SessionUpdate(BaseModel):
    start_time: AwareDatetime | None = Field(default=None)
    end_time: AwareDatetime | None = Field(default=None)
    status: SessionStatus | None = Field(default=None)
    movie_id: MovieId | None = Field(default=None)
    hall_id: HallId | None = Field(default=None)
    pricing_id: PricingId | None = Field(default=None)

class SessionResponse(SessionBase, ORMBaseSchema):
    id: SessionId


# TECHNOLOGIES
class TechnologyBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=64, description="Technology name")
    type: str = Field(..., min_length=3, max_length=64, description="Technology type")

class TechnologyCreate(TechnologyBase):
    pass

class TechnologyUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=64, description="Technology name")
    type: str | None = Field(default=None, min_length=3, max_length=64, description="Technology type")

class TechnologyResponse(TechnologyBase, ORMBaseSchema):
    id: TechnologyId


#STEATS
class SeatBase(BaseModel):
    row_label: str = Field(..., min_length=1, max_length= 16, description="Row label")
    number: int = Field(..., ge=1, description="Seat number")
    grid_x: int = Field(...)
    grid_y: int = Field(...)
    status: SeatStatus = Field(default=SeatStatus.FREE)
    hall_id: HallId
    seat_type_id: SeatTypeId

class SeatCreate(SeatBase):
    pass

class SeatUpdate(BaseModel):
    row_label: str | None = Field(default=None, min_length=1, max_length= 16, description="Row label")
    number: int | None = Field(default=None, ge=1, description="Seat number")
    grid_x: int | None = Field(default=None)
    grid_y: int | None = Field(default=None)
    hall_id: HallId | None = Field(default=None)
    seat_type_id: SeatTypeId | None = Field(default=None)

class SeatResponse(SeatBase, ORMBaseSchema):
    id: SeatId


# SEAT TYPES
class SeatTypeBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=64, description="Seat Type name")
    description: str = Field(..., min_length=3, max_length=64, description="Seat Type type")

class SeatTypeCreate(SeatTypeBase):
    pass

class SeatTypeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=64, description="Seat Type name")
    description: str | None = Field(default=None, min_length=3, max_length=64, description="Seat Type type")

class SeatTypeResponse(SeatTypeBase, ORMBaseSchema):
    id: SeatTypeId
