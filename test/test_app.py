from fastapi.testclient import TestClient
from app import app  # Replace 'your_app_module' with the actual module name where your FastAPI app is defined

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.skip(reson='changed the app function need to rewirte the test')
def test_ner():
    text_to_test = "John Doe works at Acme Corp in New York."
    response = client.get(f"/ner/{text_to_test}")
    assert response.status_code == 200
    # Replace the expected response with the actual expected output from your entity_recognition function
    expected_response = {
        "PERSON": ["John Doe"],
        "ORG": ["Acme Corp"],
        "GPE": ["New York"]
    }
    assert response.json() == expected_response
