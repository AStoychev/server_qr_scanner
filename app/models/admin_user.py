from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime, timezone


class AdminUser(BaseModel):
    id: Optional[str]
    credentials: str = Field(..., description="User's credentials")
    registtration_date: datetime

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }


# from models.base import BaseDBModel

# class AdminUser(BaseDBModel):
#     credentials: str

