import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from bson import ObjectId
from app.main import app
from app.schemas.admin_user import AdminUserCreate, AdminUserResponse

client = TestClient(app)

@pytest.mark.asyncio
async def test_register_admin_user_success():
    mock_admin_user = AdminUserResponse(
        id=str(ObjectId()),
        credentials="admin123",
        registtration_date="2024-08-10"
    )

    user_data = AdminUserCreate(
        credentials="admin123",
        registration_date="2024-08-10"
    )

    with patch("app.services.admin_user_service.AdminUserService.create_admin_user", new=AsyncMock(return_value=mock_admin_user)):
        response = client.post("/register", json=user_data.dict())

    assert response.status_code == 200
    assert response.json() == mock_admin_user.dict()

@pytest.mark.asyncio
async def test_register_admin_user_already_exists():
    user_data = AdminUserCreate(
        credentials="admin123",
        registration_date="2024-08-10"
    )

    with patch("app.services.admin_user_service.AdminUserService.create_admin_user", new=AsyncMock(side_effect=HTTPException(status_code=400, detail="User already exists"))):
        response = client.post("/register", json=user_data.dict())

    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}
