from fastapi import APIRouter
from app.schemas.admin_user import AdminUserCreate, AdminUserResponse
from app.services.admin_user_service import admin_user_service

router = APIRouter()

@router.post("/register", response_model=AdminUserResponse)
async def register_admin_user(user: AdminUserCreate):
    return await admin_user_service.create_admin_user(user)
