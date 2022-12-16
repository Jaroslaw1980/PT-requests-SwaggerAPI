import json
import jsonpath
from pytest import mark


@mark.usefixtures("get_activity_method")
class TestsGetActivity:

    @mark.activity
    @mark.regression
    def test_get_response_should_have_correct_id(self, get_activity_method):
        response_json = json.loads(get_activity_method.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        assert response_id[0] == 1

    @mark.activity
    @mark.regression
    def test_get_response_should_have_correct_title(self, get_activity_method):
        response_json = json.loads(get_activity_method.text)
        response_title = jsonpath.jsonpath(response_json, 'title')
        assert response_title[0] == "Activity 1"

    @mark.activity
    @mark.regression
    def test_get_respone_should_have_correct_status(self, get_activity_method):
        response_json = json.loads(get_activity_method.text)
        response_status = jsonpath.jsonpath(response_json, 'completed')
        assert response_status[0] == False
