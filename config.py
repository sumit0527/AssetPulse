import os
from utils.exceptions import ConfigurationError
from dotenv import load_dotenv

load_dotenv()

try:
    # Check environment variables
    db_host = os.getenv("DB_HOST")
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_port = os.getenv("DB_PORT")

    if not db_host or not db_username or not db_password or not db_name:
        raise ConfigurationError("Missing essential database environment variables")

except ConfigurationError as config_err:
    pass
