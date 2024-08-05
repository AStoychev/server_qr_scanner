from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, timezone


class User(BaseModel):
    id: str = Field(..., alias="_id")
    code: str
    credentials: str = Field(..., description="User's credentials")
    registration_date: datetime = Field(default_factory=datetime.now(timezone.utc))
    count_visited_places: int = 0
    visited_places: List[str] = []
    # registration_date: str = Field(..., description="Registration date in string format")
    # count_visited_places = int = Field(..., ge=0)
    # visited_places: List[str] = Field(default_factory=list)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
