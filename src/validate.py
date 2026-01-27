import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_users(df):
    initial_count = len(df)

    # Duplicate user_id
    df = df.drop_duplicates(subset="user_id")

    # Email must contain @
    df = df[df["email"].str.contains("@", na=False)]

    # City must not be null
    df = df[df["city"].notna()]

    # Zipcode length >= 5
    df = df[df["zipcode"].astype(str).str.len() >= 5]

    rejected = initial_count - len(df)
    logging.info(f"Rejected {rejected} invalid records")

    return df






















# def validate_users(df):
#     initial_count = len(df)

#     # Remove duplicate users
#     df = df.drop_duplicates(subset="user_id")

#     # Valid email check
#     df = df[df["email"].str.contains("@", na=False)]

#     # City must exist
#     df = df[df["city"].notna()]

#     # Zipcode length validation
#     df = df[df["zipcode"].astype(str).str.len() >= 5]

#     rejected = initial_count - len(df)
#     logging.info(f"Rejected {rejected} invalid records")

#     return df













# # import logging

# # logging.basicConfig(
# #     filename="logs/pipeline.log",
# #     level=logging.INFO,
# #     format="%(asctime)s - %(levelname)s - %(message)s"
# # )

# # def validate_users(df):
# #     initial_count = len(df)

# #     # Duplicate user_id
# #     df = df.drop_duplicates(subset="user_id")

# #     # Email must contain @
# #     df = df[df["email"].str.contains("@", na=False)]

# #     # City must not be null
# #     df = df[df["city"].notna()]

# #     # Zipcode length >= 5
# #     df = df[df["zipcode"].astype(str).str.len() >= 5]

# #     final_count = len(df)
# #     rejected = initial_count - final_count

# #     logging.info(f"Validation completed. Rejected {rejected} records")

# #     return df
