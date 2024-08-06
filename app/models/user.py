from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from datetime import datetime, timezone


class User(BaseModel):
    id: Optional[str]
    code: str
    credentials: str
    registtration_date: datetime
    count_visited_places: int = 0
    visited_places: List[str] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }

# from typing import List
# from models.base import BaseDBModel


# class User(BaseDBModel):
#     code: str
#     credentials: str
#     count_visited_places: int = 0
#     visited_places: List[str] = []
