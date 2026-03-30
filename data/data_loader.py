from configs.configs import UNPROCESSED_DATA_PATH, PROCESSED_DATA_PATH

def file_loader():
    if not UNPROCESSED_DATA_PATH.exists():
        raise FileNotFoundError(f"{UNPROCESSED_DATA_PATH} not found")

    return UNPROCESSED_DATA_PATH.read_text(encoding="utf-8")

def save_processed_data(tokens):
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_PATH.write_text(" ".join(tokens), encoding="utf-8")