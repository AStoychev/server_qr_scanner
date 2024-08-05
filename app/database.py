import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client[DATABASE_NAME]
users_collection = database["users"]
admin_users_collections = database["admin_users"]


def get_user_collections():
    return users_collection


def get_admin_user_collection():
    return admin_users_collections
