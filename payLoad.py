def addBookPayLoad(isbn):
    body = {
        "name": "Test book for Vy",
        "isbn": isbn,
        "aisle": "222899",
        "author": "Vy H"
    }
    return body


def addBookId(bookId):
    body = {
        "ID": bookId
    }
    return body
