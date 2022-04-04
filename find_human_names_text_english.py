import spacy

english_nlp = spacy.load('en_core_web_sm')

text = '''
This is a sample text that contains the name Alex Smith who is one of the developers of this project.
You can also find the surname Jones here.
'''

spacy_parser = english_nlp(text)

for entity in spacy_parser.ents:
    print(f'Found: {entity.text} of type: {entity.label_}')

