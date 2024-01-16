from suggest_bufo import get_top_N_similarities


def main():
    N = 5
    phrase = "i am so happy"
    get_top_N_similarities(N, phrase)

if __name__ == '__main__':
    main()