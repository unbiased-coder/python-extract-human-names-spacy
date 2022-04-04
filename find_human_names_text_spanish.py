import spacy

spanish_nlp = spacy.load('es_core_news_sm')

text = '''
El nombre de esta persona es John Smith y tiene una amiga llamada Joanna Williams.
'''

spacy_parser = spanish_nlp(text)

for entity in spacy_parser.ents:
    print(f'Found: {entity.text} of type: {entity.label_}')

