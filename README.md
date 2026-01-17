# Normalized Token Counter

## 1. What you will find in this repository

After extracting the ZIP file, your directory should look like this:

Normalized-Token-Counter/ <br>
├── .gitignore <br>
├── normalize_text.py <br>
├── pg1257.txt <br>
├── README.md <br>
├── Sample Output.png <br>
└── visualization.py <br>

The file pg1257.txt is required to run visualization.py as written. You may replace it with any UTF-8 encoded .txt file and modify the code in visualization.py to reflect the new .txt file.

## 2. Setting up the environment

### Step 1: Create and setup a new Conda environment

- Open a terminal, cd into the directory "Normalized-Token-Counter", and run: `conda create -n MYENV python=3.14.2`

- Active the environment: `conda activate MYENV`

### Step 2: Install required packages

- Install the required dependencies using conda: `conda install -n MYENV matplotlib nltk`

## 3. File descriptions

- The script normalize_text.py reads a plain-text file, normalizes the text using non-alphabetic delimiters, applies normalization type(s), counts token occurences, and returns the list of tokens and their counts as well as displays the first and last 25 tokens by frequency to the terminal. Supported normalization options include: (-lowercase, -stem, -lemmatize, -stopwords, -myopt)

- The script visualization.py uses `process_file()` from normalize_text.py, hardcodes normalization options, and generates a log-scaled bar chart of the top 25 tokens and their counts. The output is saved as Sample Output.png.

## 4. Running the scripts

### Running normalize_text.py from the terminal

- Basic usage: `python normalize_text.py <filename> [options]`
- Example: `python normalize_text.py pg1257.txt -lowercase -lemmatize -myopt`
- If you need more detailed help: `python normalize_text.py -h`

### Running visualization.py from the terminal

- First ensure the input plain-text file exists in the same directory where normalization.py and visualization.py are
- Usage: `python visualization.py`

## 5. Customizing input for the scripts

### normalize_text.py

- Simply replace the old .txt file in the same directory with the new one you want to normalize/process (ensure its UTF-8 encoded)

### visualization.py

- To change the input file, follow the above step for normalize_text.py and change the name of the input file in the `process_file()` call
- To change the normalization arguments, modify the boolean values in the `args` variable at the top of the script
