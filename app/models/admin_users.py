from pydantic import BaseModel, Field


class AdminUser(BaseModel):
    credentials: str = Field(..., description="Admin user's credentials")
    date_register: str = Field(..., description="Registration date in string format")
