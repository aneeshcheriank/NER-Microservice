import spacy

nlp = spacy.load("en_core_web_sm")


def entity_recognition(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = [ent.text]
        else:
            # need to check the label is already in the list
            if ent.text not in entities[ent.label_]:
                entities[ent.label_].append(ent.text)

    return entities
