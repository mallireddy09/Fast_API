import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus
from constants import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT
from urllib.parse import quote_plus

DB_USER = quote_plus(os.getenv("DB_USER"))
DB_PASS = quote_plus(os.getenv("DB_PASS"))

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost:5433/Recommendations"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


