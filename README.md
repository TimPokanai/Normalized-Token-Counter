1. What you will find in this repository

After extracting the ZIP file, your directory should look like this:

Normalized-Token-Counter/
├── .gitignore
├── normalize_text.py
├── pg1257.txt
├── README.md
├── Sample Output.png
└── visualization.py

The file pg1257.txt is required to run visualization.py as written. You may replace it with any UTF-8 encoded .txt file and modify the code in visualization.py to reflect the new .txt file.

2. Setting up the environment

Step 1: Create and setup a new Conda environment

- Open a terminal, cd into the directory "Normalized-Token-Counter", and run: conda create -n MYENV python=3.14.2

- Active the environment: conda activate MYENV

Step 2: Install required packages

- Install the required dependencies using conda: conda install -n MYENV matplotlib nltk

3. File descriptions

- The script normalize_text.py reads a plain-text file, normalizes the text using non-alphabetic delimiters, applies normalization type(s), counts token occurences, and returns the list of tokens and their counts as well as displays the first and last 25 tokens by frequency to the terminal. Supported normalization options include: (-lowercase, -stem, -lemmatize, -stopwords, -myopt)

- The script visualization.py uses process_file() from normalize_text.py, hardcodes normalization options, and generates a log-scaled bar chart of the top 25 tokens and their counts. The output is saved as Sample Output.png.

4. Running the scripts
