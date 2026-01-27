from src.extract import extract_users
from src.transform import transform_users
from src.validate import validate_users
from src.load_csv import save_to_csv
from src.load_sqlite import load_to_sqlite
from src.insights import run_insights

def main():
    raw_data = extract_users()
    df_transformed = transform_users(raw_data)
    df_validated = validate_users(df_transformed)
    save_to_csv(df_validated)
    load_to_sqlite(df_validated)
    run_insights()

if __name__ == "__main__":
    main()
