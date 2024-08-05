from pydantic import BaseModel, Field
from datetime import datetime, timezone


class AdminUser(BaseModel):
    id: str = Field(..., alias="_id")
    credentials: str = Field(..., description="User's credentials")
    registration_date: datetime = Field(default_factory=datetime.now(timezone.utc))
    credentials: str = Field(..., description="Admin user's credentials")
    date_register: str = Field(..., description="Registration date in string format")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
