from typing import List, Optional
from pymongo.collection import Collection
from fastapi import HTTPException, status
from bson import ObjectId
from models.user import User
from schemas.user import UserCreate, UserUpdate

class UserService:
    def __init__(self, users_collection: Collection):
        self.users_collection = users_collection

    async def create_user(self, user_data: UserCreate) -> User:
        # Check if the user already exists
        existing_user = await self.users_collection.find_one({"code": user_data.code})
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        # Create a new user
        new_user = User(
            code=user_data.code,
            credentials=user_data.credentials,
        )

        # Insert the user into the database
        result = await self.users_collection.insert_one(new_user.dict(by_alias=True))
        new_user.id = str(result.inserted_id)

        return new_user

    async def get_user(self, user_id: str) -> Optional[User]:
        user_data = await self.users_collection.find_one({"_id": ObjectId(user_id)})
        # user_data = await self.users_collection.find_one({"_id": user_id})
        # print('USER: ', user_data)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
        return User(**user_data)

    async def get_all_visited_places(self, user_id: str) -> List[str]:
        user = await self.get_user(user_id)
        return user.visited_places

    async def delete_all_visited_places(self, user_id: str) -> User:
        user = await self.get_user(user_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        # Update the user's visited places and count
        update_data = {"visited_places": [], "count_visited_places": 0}
        updated_user = await self.users_collection.find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": update_data},
            return_document=True
        )

        if updated_user is None:
            raise ValueError(f"User with id {user_id} not found or update failed")

        return User(**updated_user)

# Dependency Injection: Instantiate UserService with users_collection
from database import db

user_service = UserService(users_collection=db.get_collection("users"))
