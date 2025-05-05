from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

username = quote_plus("postgres")
password = quote_plus("MallI@09")

DATABASE_URL = f"postgresql://{username}:{password}@localhost:5433/Recommendations"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
