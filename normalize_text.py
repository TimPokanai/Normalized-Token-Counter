import re
import argparse
from collections import Counter

def count_words(filename):
    try:
        with open(args.filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.split(r'\W+', text)
            sorted_words_list = Counter(words).most_common()
            return sorted_words_list
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="The path to the input plain text file")

args = parser.parse_args()

word_counts = count_words(args.filename)
print(word_counts)
