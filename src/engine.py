import spacy

nlp = spacy.load("en_core_web_sm")


def entity_recognition(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = [ent.text]
        else:
            entities[ent.label_].append(ent.text)

    return entities
