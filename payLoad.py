
# method to add book data
from utilities.configurations import *


def addBookPayLoad(isbn, aisle):
    body = {
        "name": "Test book by VH",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Julia H"
    }
    return body

# method to build payload from db
# Connect to sql and method getQuery from configurations file
def buildPayload(query):
    addBody = {}
    tpl = getQuery(query)
    addBody['name'] = tpl[0]
    addBody['isbn'] = tpl[1]
    addBody['aisle'] = tpl[2]
    addBody['author'] = tpl[3]
    return addBody

# method to add book id
# def addBookId(bookId):
#     body = {
#         "ID": bookId
#     }
#     return body
