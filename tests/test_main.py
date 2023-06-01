import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()["users"]) == 3

def test_get_user():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe"}

    response = client.get("/user/4")
    assert response.status_code == 200
    assert response.json() == {"message": "User not found"}

if __name__ == "__main__":
    import pytest
    pytest.main()
