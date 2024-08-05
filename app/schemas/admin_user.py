from pydantic import BaseModel


class AdminUserCreate(BaseModel):
    credentials: str


class AdminUserResponse(BaseModel):
    credentials: str
    registration_date: str
