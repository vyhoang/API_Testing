import requests


def after_scenario(context, scenario):
    # add tag library in bookAPI.feature
    # and intergrate tag in this hool
    # to solv HOOK_ERROR issue with bookId not in Context object
    if "library" in scenario.tags:
        response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
            "ID": context.bookId
        }, headers={"Content-Type": "application/json"},)

        # check response delete book should be done with code 200
        assert response.status_code == 200
        res_json = response.json()

        # display message when book is deleted successfully
        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
