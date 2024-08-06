from pydantic import BaseModel
from typing import Optional

class AdminUserCreate(BaseModel):
    credentials: str
    registration_date: str
    

class AdminUserResponse(BaseModel):
    credentials: str
