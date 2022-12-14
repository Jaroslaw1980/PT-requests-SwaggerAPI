import requests
import json
import jsonpath
import pytest
from pytest import mark

# api_url_post_activity = "https://fakerestapi.azurewebsites.net//api/v1/Activities"
# header_post = {"Content-Type": "application/json; v=1.0"}
# file = open("C:/Projects/APIAutomationPython/json_data/activities_json/json_add_activitie.json")
# json_add_activity = file.read()
# json_request = json.loads(json_add_activity)
#
# add_activity_response = requests.post(url=api_url_post_activity, json=json_request, headers=header_post)
#
# print(add_activity_response.text)

api_url_get_activity = "https://fakerestapi.azurewebsites.net//api/v1/Activities"
header_post = {'accept': 'text/plain; v=1.0'}

get_activity_response = requests.get(url=api_url_get_activity, headers=header_post)

print(type(get_activity_response))

header = get_activity_response.headers
print(header)
print(type(header))

print(header['Server'])



