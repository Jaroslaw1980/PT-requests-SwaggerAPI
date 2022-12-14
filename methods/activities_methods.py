from pytest import fixture
import requests
import json
import jsonpath

from resources.api_url.activities_api_url import *
from resources.headers.activities_api_headers import ActivitiesHeader


class ActivitiesApiMethod:
    api_url_activities = api_url_post_activity
    api_url_not_post_activities = api_url_not_post_activities
    header_post = ActivitiesHeader.header_post
    header_get_data = ActivitiesHeader.header_get_data
    header_get_all_data = ActivitiesHeader.header_get_all
    json_file = "C:/Projects/APIAutomationPython/resources/json_data/activities_json/json_add_activitie.json"

    def post_method(self):
        file = open(self.json_file)
        json_request = json.loads(file.read())

        post_method_response = requests.post(url=self.api_url_activities, json=json_request, headers=self.header_post)
        return post_method_response

    def get_id(self):
        json_text = self.post_method().text
        json_request = json.loads(json_text)
        json_id = jsonpath.jsonpath(json_request, 'id')
        return json_id[0]

    def get_method(self):
        get_id = self.get_id()
        url = self.api_url_not_post_activities + str(get_id)
        return requests.get(url=url, headers=self.header_get_data)

    def get_all_method(self):
        return requests.get(url=self.api_url_activities, headers=self.header_get_all_data)

    def get_delete_method(self):
        get_id = self.get_id()
        url = self.api_url_not_post_activities + str(get_id)
        return requests.delete(url=url)
