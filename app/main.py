from fastapi import FastAPI
from app.routes import book_route
from app.config.database import Base,engine

# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI app
app = FastAPI(
    title="Books API",
    description="CRUD API using FastAPI and PostgreSQL",
    version="1.0.0"
)

app.include_router(book_route.router)
