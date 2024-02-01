# routes/books_routes.py

from ..controllers.books_controller import books_blueprint

def register_books_routes(app):
    app.register_blueprint(books_blueprint)
