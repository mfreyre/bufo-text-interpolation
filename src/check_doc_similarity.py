import spacy
import re
from utils.file_readers import get_phrases_from_file
from utils.phrasers import get_emoji_phrase_dict
# nlp = spacy.load("en_core_web_lg")
nlp = spacy.load("en_core_web_md")


doc1 = nlp(u'the person wear red T-shirt')
doc2 = nlp(u'this person is walking')
doc3 = nlp(u'the boy wear red T-shirt')


print(doc1.similarity(doc2)) 
print(doc1.similarity(doc3))
print(doc2.similarity(doc3)) 


text = "my cat, who is named toast, is very silly."

# TODO: break into phrases around clauses and sentence ends
# MVP: break on punctuation marks . and ,

split_text = re.split(r'[,.]+', text)

# The split function leaves trailing spaces, which we can remove with strip()
split_text = [s.strip() for s in split_text if s.strip()]

print(split_text)



get_emoji_phrase_dict()

