from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_review_endpoint():
    response = client.post("/api/review", json={"language": "python", "code": "print('hello')"})
    assert response.status_code == 200
    assert "analysis" in response.json()