# controllers/books_controller.py

from flask import Blueprint, request, jsonify
from ..services.books_service import BookService

books_blueprint = Blueprint('books', __name__, url_prefix='/api/books')

@books_blueprint.route('/', methods=['POST'])
def create_book():
    data = request.json
    new_book = BookService.create_book(data)
    return jsonify(new_book.serialize()), 201

@books_blueprint.route('/', methods=['GET'])
def get_all_books():
    print('Test Get book')
    books = BookService.get_all_books()
    return jsonify([book.serialize() for book in books])

@books_blueprint.route('/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = BookService.get_book_by_id(book_id)
    if book:
        return jsonify(book.serialize())
    return jsonify({'message': 'Book not found'}), 404

@books_blueprint.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if book:
        data = request.json
        updated_book = BookService.update_book(book, data)
        return jsonify(updated_book.serialize())
    return jsonify({'message': 'Book not found'}), 404

@books_blueprint.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = BookService.get_book_by_id(book_id)
    if book:
        BookService.delete_book(book)
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'}), 404

# 批次處理
@books_blueprint.route('/batch', methods=['POST'])
def create_batch_books():
    batch_data = request.json
    new_books = BookService.create_batch_books(batch_data)
    return jsonify([book.serialize() for book in new_books]), 201
