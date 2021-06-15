import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'}, )
# print(reponse.text)
# print(type(reponse.text))
#
# dict_response = json.loads(reponse.text)
# print(type(dict_response))

json_response = response.json()
print(type(json_response))

# check status code, headers
print('status code: ', response.status_code)
assert response.status_code == 200

print('headers:', response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve book details with ISBN RGHCC
for actualBook in json_response:
    # print(actualBook) # this is a dict
    if actualBook['isbn'] == 'fefrewe2':
        print(actualBook)
        break

expectedBook = {
    'book_name': 'Learn Appium Automation with Python',
    'isbn': 'fefrewe2',
    'aisle': '22345'
}
assert actualBook == expectedBook
