import nltk
from nltk.corpus import wordnet as wn
from utils.file_readers import get_phrases_from_file
#nltk.download('wordnet')

def generate_related_phrases(phrase):
    words = phrase.split('py-')
    related_phrases = []

    for word in words:
        # Find synonyms using WordNet
        synonyms = set()
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())

        # Generate phrases by replacing the current word with its synonyms
        for synonym in synonyms:
            if synonym != word:
                new_phrase = phrase.replace(word, synonym)
                related_phrases.append(new_phrase.replace('_', ' '))

    return related_phrases

phrases = get_phrases_from_file('emoji-names.txt')

with open('emojis-dict.txt', 'w') as file:
    for phrase in phrases:
        test_phrase = phrase.replace('bufo', '').replace('-', ' ').strip()
        related_phrases = generate_related_phrases(test_phrase)
        print(f"testing {test_phrase} and received results {related_phrases}")

        if not related_phrases:
            test_phrase = test_phrase.split(" ")[0]
            print(f"empty results, testing {test_phrase} and received results {related_phrases}")
        file.write(f"{phrase} : {related_phrases}\n")


# TODO :
# offer_syns = wn.synonyms('offers')
#  offer_syns_flat = [item for row in offer_syns for item in row]
# remove from offer syns all references ot "offer"