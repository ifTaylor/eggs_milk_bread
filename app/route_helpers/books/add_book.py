def add_book(book_collection, book_entry):
    book = {
        'title': book_entry['title'],
        'author': book_entry['author'],
        'year': book_entry['year']
    }
    result = book_collection.insert_one(book)
    print("Book added with ID:", result.inserted_id)
