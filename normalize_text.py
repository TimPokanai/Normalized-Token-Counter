import re
import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument(
    "normalizations", 
    nargs="*",
    choices=["lowercase"],
    help="Token normalization options: lowercase"
    )
parser.add_argument("filename", help="The path to the input plain text file")

args = parser.parse_args()

def tokenize(plain_text):
    tokens = re.split(r'\W+', plain_text)
    return tokens

def normalize(tokens, normalizations):
    for norm_type in normalizations:
        if norm_type =="lowercase":
            tokens = [t.lower() for t in tokens]
    return tokens

def count_tokens(tokens):
    return Counter(tokens).most_common()

def process_file(filename, normalizations):
    try:
        with open(args.filename, 'r', encoding='utf-8') as file:
            text = file.read()

            tokens = tokenize(text)
            tokens = normalize(tokens, normalizations)

            return count_tokens(tokens)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

tokens_counts = process_file(args.filename, args.normalizations)
print(tokens_counts[0:25])
