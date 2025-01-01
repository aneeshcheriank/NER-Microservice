from fastapi.testclient import TestClient
from app import app
import pytest

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.skip(reason="changed the app function need to rewirte the test")
def test_ner():
    text_to_test = "John Doe works at Acme Corp in New York."
    response = client.get(f"/ner/{text_to_test}")
    assert response.status_code == 200
    expected_response = {
        "PERSON": ["John Doe"],
        "ORG": ["Acme Corp"],
        "GPE": ["New York"],
    }
    assert response.json() == expected_response
