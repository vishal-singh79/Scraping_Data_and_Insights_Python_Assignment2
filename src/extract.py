import requests
import json
import logging
from pathlib import Path

# Logging setup
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://jsonplaceholder.typicode.com/users"
RAW_PATH = Path("data/raw/users_raw.json")

def extract_users():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        RAW_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(RAW_PATH, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"Extracted {len(data)} records from API")
        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API extraction failed: {e}")
        raise
