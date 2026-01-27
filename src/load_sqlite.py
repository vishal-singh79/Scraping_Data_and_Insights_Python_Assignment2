import sqlite3
import logging
from pathlib import Path

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_PATH = Path("db/users.db")

def load_to_sqlite(df):
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT,
            city TEXT,
            zipcode TEXT,
            company_name TEXT
        )
    """)

    df.to_sql("users", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    logging.info("Data inserted into SQLite database")
