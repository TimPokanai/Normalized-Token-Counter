After extracting the ZIP file, your directory should look like this:

Normalized-Token-Counter/
├── .gitignore
├── normalize_text.py
├── pg1257.txt
├── README.md
└── visualization.py

The file pg1257.txt is required to run visualization.py as written. You may replace it with any UTF-8 encoded .txt file and modify the code in visualization.py to reflect the new .txt file.

Setting up the environment

Step 1: Create and setup a new Conda environment

- Open a terminal, cd into the directory "Normalized-Token-Counter", and run: conda create -n MYENV python=3.14.2

- Active the environment: conda activate MYENV

Step 2: Install required packages

- Install the required dependencies using conda: conda install -n MYENV matplotlib nltk



normalize_text.py is the plain text normalization and processing script that can be invoked via command line, and is also called as a function in visualization.py

visualization.py is a script that visualizes tokens and their occurences on a bar plot using matplotlib

To run visualization.py, open the terminal in the directory where the two python scripts are located and simply type: python visualization.py
