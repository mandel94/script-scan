import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, sessionmaker

# CONNECT TO THE DATABASE

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

