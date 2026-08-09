import mysql.connector
from dotenv import load_dotenv
from utils.exceptions import ConfigurationError
from config import db_host, db_port, db_username, db_password, db_name

try:

    # Create Database Connection
    conn = mysql.connector.connect(
        host=db_host,
        port=db_port,
        username=db_username,
        password=db_password,
        database=db_name,
    )

    # Test Connection
    if conn.is_connected():
        print("Database Connected Successfully...")


except mysql.connector.Error as e:
    print(f"Database Connection Failed: {e}")

finally:
    # Close Connection
    if "conn" in locals() and conn.is_connected():
        conn.close()
        print("Database Connection closed.")
