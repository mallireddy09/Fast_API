import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "yourpassword")
DB_NAME = os.getenv("DB_NAME", "Recommendations")
DB_PORT = os.getenv("DB_PORT", "5432")

DEBUG = os.getenv("DEBUG", "true").lower() == "true"