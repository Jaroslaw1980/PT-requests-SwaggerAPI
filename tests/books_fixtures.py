import json
import jsonpath
from pytest import fixture
from base_method.base_method import setup_request_method

### Group of fixtures used to build right request methods ###
@fixture
def add_book_method():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books"
    header_post = {"Content-Type": "application/json; v=1.0"}
    json_file = "C:/Projects/APIAutomationPython/resources/json_data/books_json/books.json"
    return setup_request_method(requests_method="post", json_file=json_file,
                                url=url, header=header_post)
@fixture
def get_response_id(add_book_method):
    json_text = add_book_method.text
    json_request = json.loads(json_text)
    json_id = jsonpath.jsonpath(json_request, 'id')
    return json_id[0]
@fixture
def delete_book_method(get_response_id):
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/" + str(get_response_id)
    header = {"accept": "text/plain; v=1.0"}
    return setup_request_method(requests_method="delete", url=url, header=header)
@fixture
def get_all_books_method():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books"
    header = {"accept": "text/plain; v=1.0"}
    return setup_request_method( requests_method="get", url=url, header=header)
