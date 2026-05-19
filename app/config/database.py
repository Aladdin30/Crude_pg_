from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#db_url = "postgresql://postgres:1234@localhost:5432/book_db"
db_url = "postgresql://postgres:password@host.docker.internal:5432/book_db"
engine= create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False,
                            autocommit=False,
                            bind=engine)
Base = declarative_base()


