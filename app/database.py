import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
url = os.getenv("DATABASE_URL")

def get_engine():
    Engine = create_engine(url)
    return Engine;

def get_session():
    Engine = get_engine()
    Session = sessionmaker(bind=Engine)
    return Session

def get_base():
    Base = declarative_base()
    return Base

engine = get_engine()
session = get_session()
base = get_base()

print("Database connection established")
print(engine)
print(session)
print(base)
