def get_phrases_from_file(filename):
    with open(filename, 'r') as file:
        phrases = [line.strip() for line in file]
    return phrases