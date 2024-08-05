from typing import List, Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    code: str
    credentials: str


class UserUpdate(BaseModel):
    visited_places: Optional[List[str]] = None


class UserResponse(BaseModel):
    code: str
    credentials: str
    registration_date: str
    count_visited_places: int
    visited_places: List[str]