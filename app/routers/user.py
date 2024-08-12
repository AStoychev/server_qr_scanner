from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from schemas.user import UserCreate, UserResponse
from services.user_service import user_service

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    return await user_service.create_user(user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    return await user_service.get_user(user_id)

@router.get("/{user_id}/getall", response_model=List[str])
async def get_all_visited_places(user_id: str):
    return await user_service.get_all_visited_places(user_id)

@router.delete("/{user_id}/deleteall", response_model=UserResponse)
async def delete_all_visited_places(user_id: str):
    return await user_service.delete_all_visited_places(user_id)