from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
UNPROCESSED_DATA_PATH = DATA_DIR / "unprocessed_data.txt"

stopwords = {
    "a","an","the","is","are","was","were","to","of","and","in","on",
    "for","with","this","that","it","as","by","at","from"
}

