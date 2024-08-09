import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.collection import Collection
from app.database import MongoDB

# Specify the test collection name
TEST_COLLECTION_NAME = "test_collection"

@pytest.mark.asyncio
async def test_mongo_client_initialization(mongo_db):
    """
    Test to ensure MongoDB client initialization.
    """
    # Verify that the client is connected to the correct database
    assert isinstance(mongo_db.db, AsyncIOMotorDatabase)
    assert mongo_db.db.name == "test_database"

@pytest.mark.asyncio
async def test_get_collection(mongo_db):
    """
    Test to ensure get_collection returns a valid collection.
    """
    # Retrieve the test collection
    collection = mongo_db.get_collection(TEST_COLLECTION_NAME)
    assert isinstance(collection, Collection)
    assert collection.name == TEST_COLLECTION_NAME
