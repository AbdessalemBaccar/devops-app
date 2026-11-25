from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_item():
    response = client.get("/item/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "book"}


def test_item_not_found():
    response = client.get("/items/99")
    assert response.status_code == 404


def test_add():
    response = client.get("/add", params={"a": 2, "b": 3})
    assert response.json() == {"result": 5}
