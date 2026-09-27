"""Tests for Blog API."""

import pytest
from httpx import AsyncClient
from main import app, get_db
from sqlalchemy.ext.asyncio import AsyncSession

async def override_get_db():
    async with AsyncSession(engine) as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.get("/")
    assert resp.status_code == 200
    assert resp.json()["message"] == "Blog API"
