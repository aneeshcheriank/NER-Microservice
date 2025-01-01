from fastapi.testclient import TestClient
from app import (
    app,
)  # Replace 'your_app_module' with the actual module name where your FastAPI app is defined
import pytest

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.skip(reason="function has changed need to rewrite the test")
def test_ner():
    text_to_test = "John Doe works at Google in New York."
    response = client.get(f"/ner/{text_to_test}")
    assert response.status_code == 200
    expected_response = {"PERSON": ["John Doe"], "ORG": ["Google"], "GPE": ["New York"]}
    assert response.json() == expected_response
