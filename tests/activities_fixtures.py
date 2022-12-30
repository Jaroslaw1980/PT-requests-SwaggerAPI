from base_method.base_method import setup_request_method
from pytest import fixture
from base_method.json_loader import get_data_from_json
from resources.api_url.activities_api_url import *
from resources.headers.activities_api_headers import ActivitiesHeader

### Group of fixtures used to build right request methods ###

@fixture
def add_activity_method():
    url = api_url_post_activity
    header_post = ActivitiesHeader.header_post
    json_file = "C:/Projects/APIAutomationPython/resources/json_data/activities_json/json_add_activitie.json"
    return setup_request_method(requests_method="post", json_file=json_file,
                                url=url, header=header_post)
@fixture
def get_response_id(add_activity_method):
    return get_data_from_json(add_activity_method, 'id')
@fixture
def delete_activity_method(get_response_id):
    url = api_url_not_post_activities + str(get_response_id)
    return setup_request_method(requests_method="delete", url=url)
@fixture
def get_all_activities_method():
    url = api_url_not_post_activities
    header = ActivitiesHeader.header_get_all
    return setup_request_method(requests_method="get", url=url, header=header)
@fixture
def get_activity_method(get_response_id):
    url = api_url_not_post_activities + str(get_response_id)
    header = ActivitiesHeader.header_get_data
    return setup_request_method(requests_method="get", url=url, header=header)
