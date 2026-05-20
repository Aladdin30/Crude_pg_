from app.models.book_model import Book
class BookRepository:
    def __init__(self,db):
        self.db=db
        
    def create_book(self, book:Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def get_book_by_id(self,book_id:int):
        return self.db.query(Book).filter(Book.id == book_id).first()
    
    def update_book(self,book_id:int,book:Book):
        new_book= self.db.query(Book).filter(Book.id == book_id).first()
        if not new_book:
            return None
        new_book.title = book.title
        new_book.auther = book.auther
        new_book.available = book.available

        self.db.commit()
        self.db.refresh(new_book)

        return new_book

    def get_all_books(self):
        return self.db.query(Book).all()

    def delete_book(self,book_id:int):
        del_book=self.db.query(Book).filter(Book.id == book_id).first()
        if not del_book:
            return None
        self.db.delete(del_book)
        self.db.commit()
        return {"message": f"sucessfully deleted book with id {book_id}"}
