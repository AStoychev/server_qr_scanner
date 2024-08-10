import pytest
from unittest.mock import AsyncMock, MagicMock
from bson import ObjectId
from pymongo.results import InsertOneResult

from fastapi import HTTPException
from app.services.user_service import UserService
from app.models.user import User
from app.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_user_success():
    # Arrange
    mock_collection = AsyncMock()
    mock_collection.find_one.return_value = None  # No existing user
    mock_insert_result = MagicMock(spec=InsertOneResult)
    mock_insert_result.inserted_id = ObjectId()  # Mock an ObjectId
    mock_collection.insert_one.return_value = mock_insert_result

    user_service = UserService(users_collection=mock_collection)

    user_data = UserCreate(
        code="user123", credentials="password123", registration_date="2024-08-10"
    )

    # Act
    new_user = await user_service.create_user(user_data)

    # Assert
    assert new_user.code == "user123"
    assert new_user.credentials == "password123"
    assert new_user.registtration_date == "2024-08-10"
    assert new_user.id == str(mock_insert_result.inserted_id)
    mock_collection.insert_one.assert_awaited_once_with(new_user.dict(by_alias=True))


@pytest.mark.asyncio
async def test_create_user_already_exists():
    # Arrange
    mock_collection = AsyncMock()
    mock_collection.find_one.return_value = {"_id": ObjectId()}  # Existing user

    user_service = UserService(users_collection=mock_collection)

    user_data = UserCreate(
        code="user123", credentials="password123", registration_date="2024-08-10"
    )

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        await user_service.create_user(user_data)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "User already exists"


@pytest.mark.asyncio
async def test_get_user_success():
    # Arrange
    mock_collection = AsyncMock()
    user_id = ObjectId()
    mock_collection.find_one.return_value = {
        "_id": user_id,
        "code": "user123",
        "credentials": "password123",
        "registtration_date": "2024-08-10",
        "visited_places": [],
    }

    user_service = UserService(users_collection=mock_collection)

    # Act
    user = await user_service.get_user(str(user_id))

    # Assert
    assert user.id == str(user_id)
    assert user.code == "user123"
    assert user.credentials == "password123"
    assert user.registtration_date == "2024-08-10"
    mock_collection.find_one.assert_awaited_once_with({"_id": user_id})


@pytest.mark.asyncio
async def test_get_user_not_found():
    # Arrange
    mock_collection = AsyncMock()
    mock_collection.find_one.return_value = None  # No user found

    user_service = UserService(users_collection=mock_collection)

    user_id = str(ObjectId())

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        await user_service.get_user(user_id)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "User not found!"
    mock_collection.find_one.assert_awaited_once_with({"_id": ObjectId(user_id)})


@pytest.mark.asyncio
async def test_get_all_visited_places():
    # Arrange
    mock_collection = AsyncMock()
    user_id = ObjectId()
    mock_collection.find_one.return_value = {
        "_id": user_id,
        "code": "user123",
        "credentials": "password123",
        "registtration_date": "2024-08-10",
        "visited_places": ["place1", "place2"],
    }

    user_service = UserService(users_collection=mock_collection)

    # Act
    visited_places = await user_service.get_all_visited_places(str(user_id))

    # Assert
    assert visited_places == ["place1", "place2"]
    mock_collection.find_one.assert_awaited_once_with({"_id": user_id})


@pytest.mark.asyncio
async def test_delete_all_visited_places_success():
    # Arrange
    mock_collection = AsyncMock()
    user_id = ObjectId()
    mock_collection.find_one.return_value = {
        "_id": user_id,
        "code": "user123",
        "credentials": "password123",
        "registtration_date": "2024-08-10",
        "visited_places": ["place1", "place2"],
        "count_visited_places": 2,
    }
    updated_user_data = {
        "_id": user_id,
        "code": "user123",
        "credentials": "password123",
        "registtration_date": "2024-08-10",
        "visited_places": [],
        "count_visited_places": 0,
    }
    mock_collection.find_one_and_update.return_value = updated_user_data

    user_service = UserService(users_collection=mock_collection)

    # Act
    updated_user = await user_service.delete_all_visited_places(str(user_id))

    # Assert
    assert updated_user.visited_places == []
    assert updated_user.count_visited_places == 0
    mock_collection.find_one_and_update.assert_awaited_once_with(
        {"_id": user_id},
        {"$set": {"visited_places": [], "count_visited_places": 0}},
        return_document=True,
    )
