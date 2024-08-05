from pymongo.collection import Collection
from fastapi import HTTPException, status
from bson import ObjectId

from models.admin_user import AdminUser
from schemas.admin_user import AdminUserCreate

class AdminUserService:
    def __init__(self, admin_users_collection: Collection):
        self.admin_users_collection = admin_users_collection

    async def create_admin_user(self, user_data: AdminUserCreate) -> AdminUser:
        # Create a new admin user
        new_admin_user = AdminUser(credentials=user_data.credentials)

        # Insert the admin user into the database
        result = await self.admin_users_collection.insert_one(new_admin_user.dict(by_alias=True))
        new_admin_user.id = str(result.inserted_id)

        return new_admin_user

# Dependency Injection: Instantiate AdminUserService with admin_users_collection
from database import db

admin_user_service = AdminUserService(admin_users_collection=db.get_collection("admin_users"))
