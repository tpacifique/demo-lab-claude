from fastapi.testclient import TestClient

from lab_claude.app.main import app

client = TestClient(app)


def test_docs_at_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json().get("status") == "ok"