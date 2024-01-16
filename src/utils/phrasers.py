from utils.file_readers import get_phrases_from_file

def get_emoji_phrase_dict():
    emoji_names = get_phrases_from_file('emoji-names.txt')

    phrase_to_emoji_name = {}
    for e in emoji_names:
        phrase = e.replace('bufo', '').replace('-', ' ').strip()
        phrase_to_emoji_name[phrase] = e



def get_bufo_phrases(nlp, filename):
    emoji_names = get_phrases_from_file(filename)
    names_to_phrases = {p : p.replace('bufo','').replace('-', ' ') for p in emoji_names}
    bufo_emoji_docs = {}
    for emoji_name, phrase in names_to_phrases.items():
        doc = nlp(phrase)
        bufo_emoji_docs[emoji_name] = doc
    return bufo_emoji_docs

def get_user_phrases(nlp, phrases):
    return [nlp(phrase) for phrase in phrases]