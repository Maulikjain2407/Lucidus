from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"

UNPROCESSED_DATA_PATH = DATA_DIR / "unprocessed_data.txt"
PROCESSED_DATA_PATH = PROCESSED_DIR / "processed.txt"

stopwords = {
    "a","an","the","is","are","was","were","to","of","and","in","on",
    "for","with","this","that","it","as","by","at","from"
}

