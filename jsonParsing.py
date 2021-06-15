import json

# parse json data into variable courses
courses = '{"name": "Vy Hoang", "languages": ["Java", "Python"]}'

# loads methos parse json string and it returns dic
dict_courses = json.loads(courses)
# print(type(dict_courses)) # check type of json string
print(dict_courses)
print(dict_courses['name'])  # access value from key 'name'

# get the first language
list_language = dict_courses['languages']
# print(type(list_language)) # check type of language value
print(list_language[0])

# **** Parse json content file
with open('C:\\Udemy\\API Python\\courses.json') as f:
    # convert json data into dict obj called data
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'])  # access courses content in json file
    print(data['courses'][1])  # access course at index 1
    print(data['courses'][1]['title'])  # access value of key 'title' of indext 1
    print(data['dashboard']['website'])
    # all code to access by index just for simple data

    # more complex access item in json file not by index
    # get price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
        # print(course)
        if course['title'] == 'RPA':
            print("price of course RPA: ", course['price'])
            # validate data from json
            assert course['price'] == 45

# Compare two Json files in Python
with open('C:\\Udemy\\API Python\\courses1.json') as fi:
    data2 = json.load(fi)
    assert data == data2

