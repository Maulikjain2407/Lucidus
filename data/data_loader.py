from configs.configs import UNPROCESSED_DATA_PATH

def file_loader():
    if not UNPROCESSED_DATA_PATH.exists():
        raise FileNotFoundError(f"{UNPROCESSED_DATA_PATH} not found")

    return UNPROCESSED_DATA_PATH.read_text(encoding="utf-8")