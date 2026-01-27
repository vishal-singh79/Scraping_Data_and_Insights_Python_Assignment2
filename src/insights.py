
import sqlite3
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_PATH = "db/users.db"

def run_insights():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    queries = {
        "Total Valid Users": """
            SELECT COUNT(*) 
            FROM users
        """,

        "Users Per City": """
            SELECT city, COUNT(*) 
            FROM users
            GROUP BY city
        """,

        "Users with Zipcode Length < 5": """
            SELECT COUNT(*) 
            FROM users
            WHERE LENGTH(zipcode) < 5
        """
    }

    print("\n================ SQL INSIGHTS =================")

    for title, query in queries.items():
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"\n{title}")
        print("-" * (len(title) + 4))

        for row in results:
            # If only one column (COUNT), print nicely
            if len(row) == 1:
                print(f"{row[0]}")
            else:
                print("", row)

    print("\n==============================================")

    conn.close()
    logging.info("SQL insights executed and printed to terminal")
























# import sqlite3
# import logging

# logging.basicConfig(
#     filename="logs/pipeline.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# DB_PATH = "db/users.db"

# def run_insights():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     queries = {
#         "Total Users": "SELECT COUNT(*) FROM users",
#         "Users per City": "SELECT city, COUNT(*) FROM users GROUP BY city",
#         "Email Domains": """
#             SELECT SUBSTR(email, INSTR(email, '@') + 1) AS domain, COUNT(*)
#             FROM users
#             GROUP BY domain
#         """
#     }

#     for title, query in queries.items():
#         cursor.execute(query)
#         result = cursor.fetchall()
#         print(f"\n{title}:")
#         for row in result:
#             print(row)

#     conn.close()
#     logging.info("SQL insights executed")

