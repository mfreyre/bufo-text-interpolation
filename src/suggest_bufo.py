import spacy
from utils.file_readers import get_phrases_from_file

nlp = spacy.load("en_core_web_md")

phrases = get_phrases_from_file('emoji_sample_sm.txt')
print(phrases)

bufo_emoji_docs = {}
for phrase in phrases:
    doc = nlp(phrase)
    bufo_emoji_docs[phrase] = doc


user_phrases = ['I am so annoyed', 'I am shocked'];
user_phrase_docs = [nlp(phrase) for phrase in user_phrases]
for phrase in user_phrase_docs:
    for bufo_phrase, doc in bufo_emoji_docs:
        print(f"Comparing {phrase} to {bufo_phrase}")
        print(phrase.similarity(doc))


