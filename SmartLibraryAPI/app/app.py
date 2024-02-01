# app/app.py
from flask import Flask
from flask_migrate import Migrate
from .models import db
import subprocess


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/smartlibrary'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # 啟動 pg_ctl
    start_pg_ctl()

    db.init_app(app)
    migrate = Migrate(app, db)

    from .routes.books_routes import register_books_routes
    register_books_routes(app)

    @app.route('/')
    def index():
        return 'Hello, Smart Library API!'

    return app
def start_pg_ctl():
    # 在這裡執行啟動 pg_ctl 的指令
    subprocess.run(['pg_ctl', 'start', '-D', 'data'])
if __name__ == '__main__':
    create_app().run(debug=True)
