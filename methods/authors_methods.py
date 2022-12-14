import requests
import json
import jsonpath

from resources.api_url.authors_api_url import *
from resources.headers.authors_api_headers import AuthorsHeaders


class AuthorsApiMethod:
    api_url_post_authors = api_url_authors
    api_url_not_post_authors = api_url_not_post_authors
    api_url_get_book_by_id = api_url_get_book_by_id
    authors_post_header = AuthorsHeaders.header_post
    authors_get_header = AuthorsHeaders.header_get
    authors_get_all_header = AuthorsHeaders.header_get_all

    json_file = "C:/Projects/APIAutomationPython/resources/json_data/authors_json/json_add_author.json"

    def post_method(self):
        file = open(self.json_file)
        json_request = json.loads(file.read())

        post_method_response = requests.post(url=self.api_url_post_authors, json=json_request,
                                             headers=self.authors_post_header)
        return post_method_response

    def get_id(self):
        json_text = self.post_method().text
        json_request = json.loads(json_text)
        json_id = jsonpath.jsonpath(json_request, 'id')
        return json_id[0]

    def get_book_id(self):
        json_text = self.post_method().text
        json_request = json.loads(json_text)
        json_id_book = jsonpath.jsonpath(json_request, 'idBook')
        return json_id_book[0]

    def get_method(self):
        get_id = self.get_id()
        url = self.api_url_not_post_authors + str(get_id)
        return requests.get(url=url, headers=self.authors_get_header)

    def get_all_method(self):
        return requests.get(url=self.api_url_post_authors, headers=self.authors_get_all_header)

    def get_delete_method(self):
        get_id = self.get_id()
        url = self.api_url_not_post_authors + str(get_id)
        return requests.delete(url=url)

    def get_book_by_bookid(self):
        get_book_id = self.get_book_id()
        url = self.api_url_get_book_by_id + str(get_book_id)
        return requests.get(url=url, headers=self.authors_get_header)
