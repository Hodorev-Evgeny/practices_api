import pytest
from api.main import app
from httpx import AsyncClient, ASGITransport
from fastapi import HTTPException


@pytest.mark.asyncio
async def test_add_correct_book():
    test_book = {
        'author': 'Ivan Chaikovsky',
        'title': 'Museam',
        'about_book': 'This in perfect'
    }

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        responses = await ac.post("/add_book", json=test_book)

        assert responses.status_code == 200

        data = responses.json()
        assert data == {'status': 'success', 'message': 'Book added successfully!'}

@pytest.mark.asyncio
async def test_add_incorrect_book():
    test_book = {
        'author': 'Ivan Chaikovsky',
        'title': 'Museam',
        'about_book': 'This in perfect' * 200
    }
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        responses = await ac.post("/add_book", json=test_book)

        assert responses.status_code == 500