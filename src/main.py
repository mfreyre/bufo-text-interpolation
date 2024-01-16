import argparse
from suggest_bufo import get_top_N_similarities


def main():
    parser = argparse.ArgumentParser(description="Get top N similar bufo phrases.")
    parser.add_argument('phrase', type=str, help='Phrase to compare')
    parser.add_argument('N', type=int, help='Number of top similar phrases to return')

    # Parse arguments
    args = parser.parse_args()

    # Get values
    phrase = args.phrase
    N = args.N

    # Call the function with command line arguments
    get_top_N_similarities(N, phrase)

if __name__ == '__main__':
    main()