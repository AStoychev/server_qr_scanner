import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from bson import ObjectId
from app.main import app
from app.schemas.user import UserCreate, UserResponse

client = TestClient(app)


@pytest.mark.asyncio
async def test_register_user_success():
    mock_user = UserResponse(
        id=str(ObjectId()),
        code="12345",
        credentials="user123",
        registtration_date="2024-08-10",
        visited_places=[],
        count_visited_places=0,
    )

    user_data = UserCreate(
        code="12345", credentials="user123", registration_date="2024-08-10"
    )

    with patch(
        "app.services.user_service.UserService.create_user",
        new=AsyncMock(return_value=mock_user),
    ):
        response = client.post("/user/register", json=user_data.dict())

    assert response.status_code == 200
    assert response.json() == mock_user.dict()


@pytest.mark.asyncio
async def test_get_user_success():
    mock_user = UserResponse(
        id=str(ObjectId()),
        code="12345",
        credentials="user123",
        registtration_date="2024-08-10",
        visited_places=[],
        count_visited_places=0,
    )

    user_id = str(ObjectId())

    with patch(
        "app.services.user_service.UserService.get_user",
        new=AsyncMock(return_value=mock_user),
    ):
        response = client.get(f"/user/{user_id}")

    assert response.status_code == 200
    assert response.json() == mock_user.dict()


@pytest.mark.asyncio
async def test_get_all_visited_places_success():
    visited_places = ["Place A", "Place B"]
    user_id = str(ObjectId())

    with patch(
        "app.services.user_service.UserService.get_all_visited_places",
        new=AsyncMock(return_value=visited_places),
    ):
        response = client.get(f"/user/{user_id}/getall")

    assert response.status_code == 200
    assert response.json() == visited_places


@pytest.mark.asyncio
async def test_delete_all_visited_places_success():
    mock_user = UserResponse(
        id=str(ObjectId()),
        code="12345",
        credentials="user123",
        registtration_date="2024-08-10",
        visited_places=[],
        count_visited_places=0,
    )

    user_id = str(ObjectId())

    with patch(
        "app.services.user_service.UserService.delete_all_visited_places",
        new=AsyncMock(return_value=mock_user),
    ):
        response = client.delete(f"/user/{user_id}/deleteall")

    assert response.status_code == 200
    assert response.json() == mock_user.dict()
