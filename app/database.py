import os
from dotenv import load_dotenv

import motor.motor_asyncio
from pymongo.collection import Collection

load_dotenv()

MONGO_DETAILS = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str) -> Collection:
        return self.db[collection_name]

db = MongoDB(MONGO_DETAILS, DATABASE_NAME)
