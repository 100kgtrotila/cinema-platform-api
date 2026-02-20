import enum

class MovieStatus(str, enum.Enum):
    COMING_SOON = "coming_soon"
    NOW_PLAYING = "now_playing"
    ENDED = "ended"

