import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app
# from app.main import app

DATABASE_URL = "mongodb://localhost:27017/test_database"

@pytest.fixture(scope="module")
async def test_app():
    client = AsyncIOMotorClient(DATABASE_URL)
    database = client.test_database

    app.mongodb_client = client
    app.database = database

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    client.drop_database("test_database")
    await client.close()
