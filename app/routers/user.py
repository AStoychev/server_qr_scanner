from fastapi import APIRouter, HTTPException, status
from typing import List

from models.users import User
from schemas.user import UserCreate, UserUpdate, UserResponse
from database import users_collection

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    existing_user = await users_collection.find_one({"code": user.code})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist!")

    new_user = User (
        id="",
        code=user.code,
        credentials=user.credentials,
    )

    user = await users_collection.insert_one(new_user.dict())
    new_user.id = str(user.inserted_id)

    return new_user


@router.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await users_collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return user


@router.get("/user/{user_id}/getall", response_model=List[str])
async def get_all_visited_places(user_id: str):
    user = await users_collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    return user["visited_places"]


@router.delete("/user/{user_id}/deleteall", response_model=UserResponse)
async def delete_all_visited_places(user_id: str):
    user = await users_collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")

    update_data = {"visited_places": [], "count_visited_places": 0}
    await users_collection.update_one({"_id": user_id}, {"set": update_data})

    update_user = await users_collection.find_one({"_id": user_id})
    return update_user