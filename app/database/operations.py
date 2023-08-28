def add_book(collection, title, author, year):
    book = {
        'title': title,
        'author': author,
        'year': year
    }
    result = collection.insert_one(book)
    return result.inserted_id


def find_books_by_author(collection, author):
    query = {'author': author}
    books = collection.find(query)
    return [book['title'] for book in books]
