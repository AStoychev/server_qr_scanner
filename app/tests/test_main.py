import pytest

@pytest.mark.asyncio
async def test_root(test_app):
    """
    Tests the root endpoint of the application.
    """
    response = await test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI MongoDB Application!"}
