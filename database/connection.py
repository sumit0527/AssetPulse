import mysql.connector
from dotenv import load_dotenv
import os

# load environment variables 
load_dotenv()

try:
    # Create Database Connection
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    # Test Connection
    if conn.is_connected():
        print("Database Connected Successfully...")

except mysql.connector.Error as err:
    print(f"Database Connection Failed: {err}")

finally:
    # Close Connection
    if "conn" in locals() and conn.is_connected():
        conn.close()
        print("Database Connection closed.")
