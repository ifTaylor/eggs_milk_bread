from app.database.database_client import DatabaseClient
from app.route_helpers.books.add_book import add_book
from flask import Blueprint, request, render_template, jsonify


books_bp = Blueprint('books', __name__)


@books_bp.route('/api/add_book', methods=['GET', 'POST'])
def add_book_route():
    print('Made it')
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        if title is not None and author is not None and year is not None:
            book_entry = {
                'title': title,
                'author': author,
                'year': year
            }

            database_client = DatabaseClient()
            client = database_client.connect()
            add_book(client['library_db']['books'], book_entry)
            database_client.close()

            return jsonify({'message': 'Book added successfully'}), 200

        else:
            error_message = 'Invalid or missing data'
            return jsonify({'message': 'Book added successfully'}), 200
    else:
        return jsonify({'message': 'Book added successfully'}), 200
