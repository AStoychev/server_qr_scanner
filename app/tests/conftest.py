import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from app.database import MongoDB

# Test database URL
TEST_MONGO_URI = "mongodb://localhost:27017/test_database"
TEST_DATABASE_NAME = "test_database"

@pytest.fixture(scope="module")
async def mongo_client():
    """
    Fixture to set up the MongoDB client for testing.
    """
    client = AsyncIOMotorClient(TEST_MONGO_URI)
    yield client
    client.drop_database(TEST_DATABASE_NAME)
    await client.close()

@pytest.fixture(scope="module")
async def mongo_db(mongo_client):
    """
    Fixture to set up the MongoDB instance for testing.
    """
    return MongoDB(TEST_MONGO_URI, TEST_DATABASE_NAME)


# import pytest
# from motor.motor_asyncio import AsyncIOMotorClient
# from fastapi.testclient import TestClient
# from httpx import AsyncClient
# from main import app

# DATABASE_URL = "mongodb://localhost:27017/test_database"

# @pytest.fixture(scope="module")
# async def test_app():
#     client = AsyncIOMotorClient(DATABASE_URL)
#     database = client.test_database

#     app.mongodb_client = client
#     app.database = database

#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         yield ac

#     client.drop_database("test_database")
#     await client.close()
