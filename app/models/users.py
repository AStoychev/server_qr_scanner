from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class User(BaseModel):
    code: str = Field()
    credentials: str = Field(..., description="Admin user's credentials")
    date_register: str = Field(..., description="Registration date in string format")
    count_visited_places = int = Field(..., ge=0)
    visited_places: List[str] = Field(default_factory=list)
