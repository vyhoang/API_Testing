import requests
from API_Testing.utilities.configurations import *

# --- put all code for config below in configurations.py
# and then call its method:
# create config object to read properties file
# config = configparser.ConfigParser()
# config.read('utilities/properties.ini')
# ---------------------------------------------#

# customize addBook and deleteBook automation from files in utilities package and file payLoad
# url = getConfig()['API']['endpoint']
# headers = {"Content-type": "application/json"}
#
# # add a book
# addBook = ApiResources.addBook
# addBook_response = requests.post(url + addBook, json=addBookPayLoad(isbn='vytestabc'), headers=headers,)
#
# # display the added book info
# print(addBook_response.json())
# response_json = addBook_response.json()
# # print(type(response_json))
#
# # retrieve bookId created
# bookId = response_json['ID']
# print('book id: ', bookId)
#
# # Delete book id
# deleteBook = ApiResources.deleteBook
# response_deleteBook = requests.post(url + deleteBook, json=addBookId(bookId=bookId), headers=headers,)
#
# # check response delete book should be done with code 200
# assert response_deleteBook.status_code == 200
# res_json = response_deleteBook.json()
#
# # display message when book is deleted successfully
# print(res_json['msg'])
# assert res_json['msg'] == "book is successfully deleted"

# Authentication
url = 'https://api.github.com/user'
github_response = requests.get(url, verify=False, auth=(gitLogin_auth()))
print(github_response.status_code)
print(github_response.text)

url2 = 'https://api.github.com/user/repos'
response = requests.get(url2, auth=(gitLogin_auth()))
print(response.status_code)
print(response.text)