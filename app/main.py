import os
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional, List
from dotenv import load_dotenv

# from app.models.admin_users import AdminUser
# from app.models.users import User

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

app = FastAPI()

client = AsyncIOMotorClient(MONGODB_URI)
database = client[DATABASE_NAME]
collection = database["admin-users"]


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Server FastAPI is start"}
