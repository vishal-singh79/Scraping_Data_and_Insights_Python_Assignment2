import pandas as pd
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def transform_users(raw_data):
    records = []

    for user in raw_data:
        records.append({
            "user_id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "zipcode": user.get("address", {}).get("zipcode"),
            "company_name": user.get("company", {}).get("name")
        })

    df = pd.DataFrame(records)
    logging.info("Transformation completed")
    return df
