import re
import argparse
from collections import Counter

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

# We need to download our lists of words for lemmatization and stop words
nltk.download("wordnet", quiet=True)
nltk.download("stopwords", quiet=True)

# Converting list of stopwords into a set for quicker lookup
STOPWORDS = set(stopwords.words("english"))

lemma = WordNetLemmatizer()
stem = PorterStemmer()

# Here we split our text string by non-alphabetic characters, ensuring no empty "" tokens are saved
def tokenize(plain_text):
    return [t for t in re.split(r"\W+", plain_text) if t]

# Here we conditionally apply normalization options based on args
def normalize(tokens, args):
    if args.lowercase:
        tokens = [t.lower() for t in tokens]
    if args.stopwords:
        tokens = [t for t in tokens if t not in STOPWORDS]
    if args.myopt:
        tokens = [t for t in tokens if not (len(t) == 1 and t.isalpha())]
    if args.stem:
        tokens = [stem.stem(t) for t in tokens]
    if args.lemmatize:
        tokens = [lemma.lemmatize(t) for t in tokens]
    return tokens

# Use Counter() objectect to count token occurences and filter by most to least common
def count_tokens(tokens):
    return Counter(tokens).most_common()

# Try to open and read plain text file, tokenize the string text, normalize tokens, return sorted tokens by occurences
def process_file(filename, args):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            tokens = tokenize(text)
            normalized_tokens = normalize(tokens, args)

            tokens_counts = count_tokens(normalized_tokens)
            print(tokens_counts[0:25])
            return tokens_counts
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    parser = argparse.ArgumentParser()

    # If we run this script from terminal, we allow it to be run with all of the below arguments
    parser.add_argument("filename", help="The path to the input plain text file")
    parser.add_argument("-lowercase", action="store_true", help="Lowercase normalization")
    parser.add_argument("-stem", action="store_true", help="Stemming normalization")
    parser.add_argument("-lemmatize", action="store_true", help="Lemmatization normalization")
    parser.add_argument("-stopwords", action="store_true", help="Stopwords normalization")
    parser.add_argument("-myopt", action="store_true", help="Single character normalization")

    args = parser.parse_args()

    tokens_counts = process_file(args.filename, args)

# main function runs if we run this script from terminal
if __name__ == "__main__":
    main()
