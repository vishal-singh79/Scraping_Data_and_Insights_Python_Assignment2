import logging
from pathlib import Path

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

CSV_PATH = Path("data/processed/users_clean.csv")

def save_to_csv(df):
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CSV_PATH, index=False)
    logging.info("Clean data saved to CSV")
