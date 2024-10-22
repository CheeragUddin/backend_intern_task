from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "email": "john@example.com", "mobile": "1234567890"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
