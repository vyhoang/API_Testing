import requests

from payLoad import *
from utilities.configurations import *
from utilities.resources import *


# --- put all code for config below in configurations.py
# and then call its method:
# create config object to read properties file
# config = configparser.ConfigParser()
# config.read('utilities/properties.ini')
# ---------------------------------------------#

# customize addBook and deleteBook automation from files in utilities package and file payLoad
# url = getConfig()['API']['endpoint']
# headers = {"Content-
# application/json"}
#
# add a book
# addBook = ApiResources.addBook
# addBook_response = requests.post(url + addBook, json=addBookPayLoad(isbn='vytestabc'), headers=headers,)
#
# # display the added book info
# print(addBook_response.json())
# response_json = addBook_response.json()
# # print(type(response_json))
###########################################################

# Connect to sql DB using methods in payLoad and Add book
url = getConfig()['API']['endpoint']
headers = {"Content-Type": "application/json"}

addBook = ApiResources.addBook
query = 'select * from Books'
addBook_response = requests.post(url + addBook, json=addBookPayLoad("vyH", "asasa"), headers=headers,)

print("Response message: ", addBook_response.json())
response_json = addBook_response.json()
print("type of json data:", type(response_json))

# # retrieve bookId created
bookId = response_json['ID']
print('book id: ', bookId)
#
# Delete book id
# deleteBook = ApiResources.deleteBook
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
        "ID": bookId
    }, headers={"Content-Type": "application/json"},)

# # check response delete book should be done with code 200
assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

# # display message when book is deleted successfully
print(res_json['msg'])
assert res_json['msg'] == "book is successfully deleted"


# Authentication
# url_gitHub = 'https://api.github.com/user'
# github_response = requests.get(url_gitHub, verify=False, auth=(auth_gitLogin()))
# print(github_response.status_code)
#
# url_gitHub2 = 'https://api.github.com/user/repos'
# response = requests.get(url_gitHub2, auth=(auth_gitLogin()))
# print(response.status_code)

