import nltk
from nltk.corpus import wordnet as wn
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

# Example usage
with open('emoji-names.txt', 'r') as file:
    phrases = [line.strip() for line in file]

with open('emojis-dict.txt', 'w') as file:
    for phrase in phrases:
        test_phrase = phrase.replace('bufo', '').replace('-', ' ').strip()
        related_phrases = generate_related_phrases(test_phrase)
        print(f"testing {test_phrase} and received results {related_phrases}")
        file.write(f"{phrase} : {related_phrases}\n")
