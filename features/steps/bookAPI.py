import requests
from behave import *

from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given("The book details which need to be added to library")
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad("ccadx", "010103121")


@when("We execute the AddBook PostAPI method")
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )


@then("Book is successfully added")
def step_impl(context):
    print(context.response.json())
    res_json = context.response.json()
    # retrieve bookId created
    context.bookId = res_json['ID']
    print(context.bookId)
    assert res_json["Msg"] == "successfully added"


@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad(isbn, aisle)


@given(u'I have gitHub auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = auth_gitLogin()


@when(u'I hit getRepo API of gitHub')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    # create statusCode variable to check any status code reponse: 200 or 404
    # and this step can be reused for any feature which checks status code
    print(context.response.status_code)
    assert context.response.status_code == statusCode
