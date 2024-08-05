from pydantic import BaseModel
from typing import Optional

class AdminUserCreate(BaseModel):
    credentials: str
    

class AdminUserResponse(BaseModel):
    # id: Optional[str]
    credentials: str
    # registration_date: str
