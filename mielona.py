import requests
import json
import jsonpath
import pytest
from pytest import mark
from tests.books_fixtures import *

url = "https://fakerestapi.azurewebsites.net/api/v1/Books"
header_post = {"Content-Type": "application/json; v=1.0"}
json_file = "C:/Projects/APIAutomationPython/resources/json_data/books_json/books.json"
response = setup_request_method(json_file=json_file, requests_method="post",
                                url=url, header=header_post)

json_text = response.text
json_request = json.loads(json_text)
json_id = jsonpath.jsonpath(json_request, 'id')
id_final = json_id[0]

url_delete = "https://fakerestapi.azurewebsites.net/api/v1/Books/"
url_proper = url_delete + str(id_final)
print(url_proper)
header = {"accept": "text/plain; v=1.0"}
respons_delete = setup_request_method(url=url_proper, header=header, requests_method="delete")
print(respons_delete.status_code)
