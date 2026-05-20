from app.repositories.book_repository import BookRepository
from app.models.book_model import Book
class BookService:
    def __init__(self,db):
        self.repository= BookRepository(db)

    def create_book_service(self,book:Book):
        return self.repository.create_book(book)

    def get_all_books_service(self):
        return self.repository.get_all_books()

    def get_book_by_id_service(self,book_id:int):
        result=self.repository.get_book_by_id(book_id)
        if result is None:
            return None
        return result


    def update_book_service(self,book_id:int,book:Book):
        result=self.repository.get_book_by_id(book_id)
        if result is None:
            return None
        return self.repository.update_book(book_id,book)

    def delete_book_service(self,book_id:int):
        result=self.repositoryget_book_by_id(book_id)
        if result is None:
            return None
        return self.repositorydelete_book(book_id)