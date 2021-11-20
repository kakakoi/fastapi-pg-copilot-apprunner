import starlette.status
import pytest
from httpx import AsyncClient
import os
os.environ['TESTING'] = 'True'
from backend.main import app, engine, metadata


@pytest.fixture
async def async_client() -> AsyncClient:
    # テスト用に非同期HTTPクライアントを返却
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_and_read(async_client):
    response = await async_client.post("/notes/", json={"title": "テスト title", "text": "test text", "completed": "true"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["title"] == "テスト title"
    assert response_obj["text"] == "test text"

    response = await async_client.get("/notes/")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 1
    assert response_obj[0]["title"] == "テスト title"
    assert response_obj[0]["text"] == "test text"
    assert response_obj[0]["completed"] is True