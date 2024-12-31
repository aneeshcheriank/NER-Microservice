"""
Extract entties from wikipedia articles
"""
import json

from .wiki import search_wiki
from .engine import entity_recognition

def ner(page, do_print=False):
    """
    Extract entities from a wiki article
    input: query(string)
    output: entities(dict)
    """

    content = search_wiki(page)
    entities = entity_recognition(content)

    if do_print:
        print(json.dumps(entities, indent=2))

    return entities

def write_json(data, filename="output.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    query = "Benjamin Netanyahu"
    entities = ner(query, do_print=True)
    write_json(entities)