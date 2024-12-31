import json
import pytest
from src.ner import ner, write_json 

# Mock data
MOCK_CONTENT = "Benjamin Netanyahu is an Israeli politician."
MOCK_ENTITIES = {
    "PERSON": ["Benjamin Netanyahu"],
    "NORP": ["Israeli"]
}

# Test `ner` function
@pytest.mark.skip(reason="Need to troubleshoot")
def test_ner(monkeypatch, capsys):
    """
    Test the ner function.
    """
    # Mock the search_wiki and entity_recognition functions
    def mock_search_wiki(query):
        assert query == "Benjamin Netanyahu"
        return MOCK_CONTENT

    def mock_entity_recognition(content):
        assert content == MOCK_CONTENT
        return MOCK_ENTITIES

    # Apply the mocks
    monkeypatch.setattr("src.wiki.search_wiki", mock_search_wiki)
    monkeypatch.setattr("src.engine.entity_recognition", mock_entity_recognition)

    # Act
    entities = ner("Benjamin Netanyahu", do_print=False)
    
    # Capture printed output
    captured = capsys.readouterr()

    # Assert
    assert entities == MOCK_ENTITIES
    assert json.dumps(MOCK_ENTITIES, indent=2) in captured.out

# Test `write_json` function
def test_write_json(monkeypatch, tmp_path):
    """
    Test the write_json function.
    """
    # Arrange
    filename = tmp_path / "test_output.json"  # Use pytest's tmp_path fixture
    data = MOCK_ENTITIES

    # Act
    write_json(data, filename=filename)

    # Assert
    assert filename.exists()
    with open(filename, "r") as f:
        written_data = json.load(f)
    assert written_data == data
