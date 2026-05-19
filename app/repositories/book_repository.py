from models.book_model import Book

def create_book(db, book:Book) -> Book:
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book_by_id(db,book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()
 
def update_book(db,book_id:int,book:Book):
    new_book= db.query(Book).filter(Book.id == book_id).first()
    new_book.title = book.title
    new_book.auther = book.auther
    new_book.available = book.available

    db.commit()
    db.refresh(new_book)

    return new_book

def get_all_books(db):
    return db.query(Book).all()

def delete_book(db,book_id:int):
    del_book=db.query(Book).filter(Book.id == book_id).first()
    db.delete(del_book)
    db.commit()
    return {"message": f"sucessfully deleted book with id {book_id}"}
