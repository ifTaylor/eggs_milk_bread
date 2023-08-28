from flask import Flask, g
from config import Config
from routes.books import books_bp
from routes.ping import ping_bp
from app.database.database_client import get_db_client


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(books_bp)
    app.register_blueprint(ping_bp)

    @app.before_request
    def before_request():
        g.db_client = get_db_client()

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db_client'):
            g.db_client.close()

    return app
