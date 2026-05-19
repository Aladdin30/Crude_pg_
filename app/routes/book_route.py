from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from services.book_services import (
    delete_book_service,
    create_book_service,
    get_all_books_service,
    get_book_by_id_service,
    update_book_service
)
from config.database import SessionLocal
from schemas.book_schame import BookCreate,BookResponse
from models.book_model import Book
router =APIRouter(
    prefix="/books",
    tags=["books"]
)
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/home_books")
def home_books():
    return {"message":"welcome to our books story"}

@router.post("/create_book",response_model=BookResponse)
def create_book(book:BookCreate,db:Session=Depends(get_db)):
    new_book=Book(
        title=book.title,
        auther=book.auther,
        available=book.available
    )
    return create_book_service(db,new_book)

@router.get("/get_all_books",response_model=list[BookResponse])
def get_all_books(db:Session=Depends(get_db)):
    return get_all_books_service(db)

@router.get("/get_book_by_id/{book_id}",response_model=BookResponse)
def get_book_by_id(book_id:int,db:Session=Depends(get_db)):
    result= get_book_by_id_service(db,book_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return result

@router.put("/update_book/{book_id}",response_model=BookResponse)
def update_book(book_id:int,book:BookCreate,db:Session=Depends(get_db)):
    
    result = update_book_service(db,book_id,book)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return result

@router.delete("/delete_book/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db)):
    result= delete_book_service(db,book_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return result


