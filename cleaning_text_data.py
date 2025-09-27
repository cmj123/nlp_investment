import os
import random 

from nltk.corpus import stopwords

random.seed(1)

# Get a list of all MD&A files
MDA_FILES = os.listdir("data/mda/")

# Remove cache file from list of files
MDA_FILES = [file for file in MDA_FILES if file != ".DS_Store"]

# Create a randon index
random_file_idx = random.randint(0, len(MDA_FILES)-1)
random_file = MDA_FILES[random_file_idx]

def clean_my_text(mda_file):
    """Returns cleaned text data"""
    # Get stopwords
    stopwords_nltk = set(stopwords.words('english'))

    # Get the file data
    with open(f"data/mda/{mda_file}") as file:
        mda_text = file.read()

    cleaned_words = [word.lower() for word in mda_text.split() if word.isalpha() and word not in stopwords_nltk]

    return cleaned_words


clean_words = clean_my_text(random_file)
print(clean_words)

