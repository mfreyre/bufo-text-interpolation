from utils.file_readers import get_phrases_from_file

def get_emoji_phrase_dict():
    emoji_names = get_phrases_from_file('emoji-names.txt')

    phrase_to_emoji_name = {}
    for e in emoji_names:
        phrase = e.replace('bufo', '').replace('-', ' ').strip()
        phrase_to_emoji_name[phrase] = e

    print(phrase_to_emoji_name)


def get_bufo_phrases(nlp, filename):
    phrases = get_phrases_from_file(filename)
    bufo_emoji_docs = {}
    for phrase in phrases:
        doc = nlp(phrase)
        bufo_emoji_docs[phrase] = doc
    return bufo_emoji_docs

def get_user_phrases(nlp):
    user_phrases = ['I am so happy', 'I am happy']
    user_phrase_docs = [nlp(phrase) for phrase in user_phrases]
    return user_phrase_docs