from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment
DATABASE_URL = os.getenv('DATABASE_URL')

# Create an SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    # might be needed for connecting to cloud db
    # connect_args={
    #     "sslmode": "require"
    # }
    )

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for your models
Base: DeclarativeMeta = declarative_base()

# Create tables in the database
def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized!")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
if __name__ == "__main__":
    init_db()