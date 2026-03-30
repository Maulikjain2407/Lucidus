# Lucidus

Lucidus is a beginner-focused NLP (Natural Language Processing) project that implements core preprocessing techniques from scratch with an emphasis on conceptual clarity, modularity, and clean software design.

---

## Overview

This project builds a minimal NLP preprocessing pipeline that:

- Loads raw text data  
- Cleans and normalizes text  
- Tokenizes text into words  
- Removes stopwords  
- Saves processed output  

The goal is to understand how NLP preprocessing works internally rather than relying on high-level libraries.

---

## Approach

The project follows a modular pipeline architecture:

```
Raw Text → Load → Preprocess → Tokenize → Stopword Removal → Save
```

### Key Design Decisions

- **Path management using `pathlib`**  
  Avoids hardcoded paths and improves cross-platform compatibility  

- **Config-driven architecture**  
  All file paths and constants are centralized in `configs/configs.py`  

- **Separation of concerns**
  - `configs/` → configuration  
  - `data/` → file handling  
  - `core/` → preprocessing logic  

- **From-scratch implementation**  
  No external NLP libraries are used  

---

## Difficulties Faced and Resolutions

### 1. File Path Errors

**Problem:**  
`FileNotFoundError: unprocessed_data.txt not found`

**Cause:**  
Incorrect file path handling  

**Resolution:**
- Switched to `pathlib`  
- Centralized paths in `configs.py`  
- Used:
  ```
  Path(__file__).resolve().parent.parent
  ```

---

### 2. Function Design Mismatch

**Problem:**  
Inconsistent function interfaces across modules  

**Resolution:**
- Standardized function signatures  
- Maintained clear separation of responsibilities  

---

### 3. Project Structure Issues

**Problem:**  
Import errors and confusion across directories  

**Resolution:**
- Adopted a package-style structure  
- Used absolute imports (`from data...`, `from configs...`)  

---

## Results

- Built a working NLP preprocessing pipeline  
- Successfully cleaned and tokenized text  
- Removed stopwords effectively  
- Saved processed output to:

```
data/processed/processed.txt
```

### Example

**Input:**
```
Rome was not built in a day.
```

**Output:**
```
rome built day
```

---

## Learnings

### Technical

- Regex-based text cleaning using `re.sub`  
- Tokenization fundamentals  
- Stopword filtering using sets  
- File handling with `pathlib`  

### Software Engineering

- Modular design principles  
- Config-driven architecture  
- Debugging Python import systems  
- Structuring scalable projects  

---

## Project Structure

```
Lucidus/
├── configs/
│   ├── __init__.py
│   └── configs.py
├── core/
│   ├── __init__.py
│   ├── main.py
│   └── preprocessing.py
├── data/
│   ├── __init__.py
│   ├── unprocessed_data.txt
│   └── processed/
│       └── processed.txt
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/Maulikjain2407/Lucidus
cd Lucidus
```

### 2. Ensure Python is installed

Python 3.8 or above is recommended.

---

## How to Run

Run the project from the root directory:

```
python -m core.main
```

---

## Configuration

All paths and constants are defined in:

```
configs/configs.py
```

Example:

```python
DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"
```

---

## Output

Processed text is saved automatically to:

```
data/processed/processed.txt
```

---

## Goal

- Build strong NLP fundamentals  
- Understand preprocessing deeply  
- Avoid dependency on external libraries  
- Create a scalable base for future NLP projects  

---

## Naming

The name *Lucidus* comes from Latin, meaning *clear* or *bright*, reflecting clarity in understanding foundational NLP concepts.

---

## License

This project is intended for educational use.
