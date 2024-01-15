from utils.file_readers import get_phrases_from_file

def get_emoji_phrase_dict():
    emoji_names = get_phrases_from_file('emoji-names.txt')

    phrase_to_emoji_name = {}
    for e in emoji_names:
        phrase = e.replace('bufo', '').replace('-', ' ').strip()
        phrase_to_emoji_name[phrase] = e

    print(phrase_to_emoji_name)