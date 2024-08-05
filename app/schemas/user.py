from typing import List, Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    id: Optional[str]
    code: str
    credentials: str
    


class UserResponse(BaseModel):
    id: Optional[str]
    code: str
    credentials: str
    # registration_date: str
    count_visited_places: int
    visited_places: List[str]


class UserUpdate(BaseModel):
    visited_places: Optional[List[str]] = None