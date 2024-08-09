import pytest
from unittest.mock import AsyncMock, MagicMock
from pymongo.results import InsertOneResult

from app.services.admin_user_service import AdminUserService
from app.models.admin_user import AdminUser
from app.schemas.admin_user import AdminUserCreate

@pytest.mark.asyncio
async def test_create_admin_user():
    # Arrange
    # Mock the admin_users_collection
    mock_collection = AsyncMock()

    # Mock the insert_one method to return a mock result with an inserted_id
    mock_insert_result = MagicMock(spec=InsertOneResult)
    mock_insert_result.inserted_id = "mocked_inserted_id"
    mock_collection.insert_one.return_value = mock_insert_result

    # Create an instance of AdminUserService with the mocked collection
    admin_user_service = AdminUserService(admin_users_collection=mock_collection)

    # Create a test AdminUserCreate instance
    user_data = AdminUserCreate(
        credentials="admin_cred",
        registration_date="2024-08-09"
    )

    # Act
    new_admin_user = await admin_user_service.create_admin_user(user_data)

    # Assert
    # Check that the insert_one method was called with the correct data
    mock_collection.insert_one.assert_awaited_once_with({
        "credentials": "admin_cred",
        "registtration_date": "2024-08-09"
    })

    # Check that the new_admin_user has the expected id
    assert new_admin_user.id == "mocked_inserted_id"

    # Check that the returned object is an instance of AdminUser
    assert isinstance(new_admin_user, AdminUser)

    # Check that the credentials and registration_date are set correctly
    assert new_admin_user.credentials == "admin_cred"
    assert new_admin_user.registtration_date == "2024-08-09"
