import spacy
from utils.file_readers import get_phrases_from_file
from utils.phrasers import get_bufo_phrases, get_user_phrases

from collections import defaultdict




# Using defaultdict to store a list of similarity values for each bufo_phrase
def generate_similarity_dict(user_phrase_docs, bufo_emoji_docs):
    similarity_dict = defaultdict(list)

    for user_phrase_doc in user_phrase_docs:
        for bufo_phrase, bufo_doc in bufo_emoji_docs.items():
            similarity = user_phrase_doc.similarity(bufo_doc)
            similarity_dict[user_phrase_doc].append([bufo_phrase, similarity])
            
    return similarity_dict

def find_top_similarities(similarity_dict, top_n=3):
    top_similarities = {}
    for phrase, similarity_list in similarity_dict.items():
        # Sort the similarity list in descending order by similarity value and get top N
        top_similarities_for_phrase = sorted(similarity_list, key=lambda x: x[1], reverse=True)[:top_n]
        top_similarities[phrase] = top_similarities_for_phrase
    return top_similarities

def printTopNSimilarities(top_similarities):
    print("\n*******\n")
    for phrase, bufos in top_similarities.items():
        print(f"For {phrase}, we recommend bufos:")
        for bufo in bufos:
            print(f"{bufo[0]}")

def get_top_N_similarities(N, phrase, print=True):
    nlp = spacy.load("en_core_web_md")
    filename = 'emoji-names.txt'
    bufo_emoji_docs = get_bufo_phrases(nlp, filename)
    user_phrase_docs = get_user_phrases(nlp, [phrase])
    similarity_dict = generate_similarity_dict(user_phrase_docs, bufo_emoji_docs)
    top_similarities = find_top_similarities(similarity_dict, N)
    printTopNSimilarities(top_similarities)
    return top_similarities


