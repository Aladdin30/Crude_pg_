from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.settings import Settings
settings=Settings()

engine= create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False,
                            autocommit=False,
                            bind=engine)
Base = declarative_base()


