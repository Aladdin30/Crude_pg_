from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.services.book_services import BookService
from app.config.database import SessionLocal
from app.schemas import BookCreate,BookResponse
from app.models import Book
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
    bookservice =BookService(db)
    new_book=Book(
        title=book.title,
        auther=book.auther,
        available=book.available
    )
    return bookservice.create_book_service(new_book)

@router.get("/get_all_books",response_model=list[BookResponse])
def get_all_books(db:Session=Depends(get_db)):
    bookservice =BookService(db)
    return bookservice.get_all_books_service()

@router.get("/get_book_by_id/{book_id}",response_model=BookResponse)
def get_book_by_id(book_id:int,db:Session=Depends(get_db)):
    bookservice =BookService(db)
    result= bookservice.get_book_by_id_service(book_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return result

@router.put("/update_book/{book_id}",response_model=BookResponse)
def update_book(book_id:int,book:BookCreate,db:Session=Depends(get_db)):
    bookservice =BookService(db)
    result = bookservice.update_book_service(book_id,book)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return result

@router.delete("/delete_book/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db)):
    bookservice =BookService(db)
    result= bookservice.delete_book_service(book_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )
    return result


