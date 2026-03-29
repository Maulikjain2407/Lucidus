from pathlib import Path

directory=Path(__file__).resolve().parent
file_path=directory/"unprocessed_data.txt"

def file_loader(file_path):
    with file_path.open("r") as f:
        data=f.read()
    return data

file_loader(file_path=file_path)