from flask import Blueprint


books_bp = Blueprint('books', __name__)


@books_bp.route('/add_book', methods=['GET', 'POST'])
def load():

    return 'Book added.'
