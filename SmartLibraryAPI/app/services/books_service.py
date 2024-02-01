# services/books_service.py

from ..models.books import Book
from .. import db

class BookService:
    @staticmethod
    def create_book(data):
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def update_book(book, data):
        for key, value in data.items():
            setattr(book, key, value)
        db.session.commit()
        return book

    @staticmethod
    def delete_book(book):
        db.session.delete(book)
        db.session.commit()

    # 批次處理
    @staticmethod
    def create_batch_books(batch_data):
        new_books = [Book(**data) for data in batch_data]
        db.session.add_all(new_books)
        db.session.commit()
        return new_books
