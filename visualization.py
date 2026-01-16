import matplotlib.pyplot as plt

from types import SimpleNamespace
from normalize_text import process_file

# Defining our normalization args, these can be hardcoded to whatever normalization args you want for visualizing
args = SimpleNamespace(
    lowercase=True,
    stem=False,
    lemmatize=False,
    stopwords=True,
    myopt=True
)

# Normalizing and processing sample file, and unpacking tuples into list of tokens sand their counts
counted_tokens = process_file("pg1257.txt", args)
tokens, counts = zip(*counted_tokens)

# Data visualization logic
plt.figure()
plt.bar(tokens[:25], counts[:25], align="center")

plt.xlabel("Tokens")
plt.ylabel("Counts")
plt.title("Normalized Token Counts in The Three Musketeers")

plt.xticks(rotation=25, ha="right", fontsize=8)
plt.grid(axis="y", alpha=0.5)

plt.show()
