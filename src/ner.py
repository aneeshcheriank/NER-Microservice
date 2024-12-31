"""
Extract entties from wikipedia articles
"""
import json

from wiki import search_wiki
from engine import entity_recognition

def ner(page):
    """
    Extract entities from a wiki article
    input: query(string)
    output: entities(dict)
    """

    content = search_wiki(page)
    entities = entity_recognition(content)

    return entities

if __name__ == "__main__":
    print(
        json.dumps(
            ner("Donald Trump"),
            indent=2
        )
    )