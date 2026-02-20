import enum

class MovieStatus(str, enum.Enum):
    COMING_SOON = "coming_soon"
    NOW_PLAYING = "now_playing"
    ENDED = "ended"

class SessionStatus(str, enum.Enum):
    PLANNED = "planned"
    OPEN = "open"
    SOLD_OUT = "sold_out"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class SeatStatus(str, enum.Enum):
    FREE = "free"
    RESERVED = "reserved"
    BROKEN = "broken"

