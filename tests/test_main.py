from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_hello_world():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Hello World"
    assert data["status"] == "success"


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"