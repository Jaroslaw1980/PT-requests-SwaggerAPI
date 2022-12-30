from base_method.base_method import setup_request_method
from pytest import fixture
import json
import jsonpath
import requests

from resources.api_url.authors_api_url import *
from resources.headers.authors_api_headers import AuthorsHeaders

### Group of fixtures used to build right request methods ###
@fixture
def add_author():
    url = api_url_authors
    header = AuthorsHeaders.header_post
    json_file = "C:/Projects/APIAutomationPython/resources/json_data/authors_json/json_add_author.json"
    return setup_request_method(requests_method="post", json_file=json_file,
                                url=url, header=header)

@fixture
def get_response_id(add_author):
    json_text = add_author.text
    json_request = json.loads(json_text)
    json_id = jsonpath.jsonpath(json_request, 'id')
    return json_id[0]
@fixture
def delete_author(get_response_id):
    url = api_url_not_post_authors + str(get_response_id)
    return setup_request_method(requests_method="delete", url=url)
@fixture
def get_all_authors():
    url = api_url_not_post_authors
    header = AuthorsHeaders.header_get_all
    return setup_request_method(requests_method="get", url=url, header=header)
@fixture
def get_author(get_response_id):
    url = api_url_not_post_authors + str(get_response_id)
    header = AuthorsHeaders.header_get
    return setup_request_method(requests_method="get", url=url, header=header)
@fixture
def get_book_id(add_author):
    json_text = add_author.text
    json_request = json.loads(json_text)
    json_id_book = jsonpath.jsonpath(json_request, 'idBook')
    return json_id_book[0]
@fixture
def get_book_by_bookid(get_book_id):
    get_book_id = get_book_id
    url = api_url_get_book_by_id + str(get_book_id)
    header = AuthorsHeaders.header_get
    return requests.get(url=url, headers=header)
