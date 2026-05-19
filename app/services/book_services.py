from repositories.book_repository import create_book, get_all_books, get_book_by_id,update_book,delete_book
from models.book_model import Book

def create_book_service(db,book:Book):
    return create_book(db,book)

def get_all_books_service(db):
    return get_all_books(db)

def get_book_by_id_service(db,book_id:int):
    result=get_book_by_id(db,book_id)
    if result is None:
        return None
    return result


def update_book_service(db,book_id:int,book:Book):
    result=get_book_by_id(db,book_id)
    if result is None:
        return None
    return update_book(db,book_id,book)

def delete_book_service(db,book_id:int):
    result=get_book_by_id(db,book_id)
    if result is None:
        return None
    return delete_book(db,book_id)