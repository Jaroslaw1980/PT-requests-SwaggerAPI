import json
import jsonpath
from pytest import mark, fixture


from methods.activities_methods import ActivitiesApiMethod


class TestsGetActivity:

    @fixture
    def set_up(self):
        self.get_get_method = ActivitiesApiMethod().get_method()

    @mark.activity
    @mark.regression
    def test_get_response_should_have_correct_id(self, set_up):
        response = self.get_get_method.text
        response_json = json.loads(response)
        response_id = jsonpath.jsonpath(response_json, 'id')
        assert response_id[0] == 17

    @mark.activity
    @mark.regression
    def test_get_response_should_have_correct_title(self, set_up):
        response = self.get_get_method.text
        response_json = json.loads(response)
        response_title = jsonpath.jsonpath(response_json, 'title')
        assert response_title[0] == "Activity 17"

    @mark.activity
    @mark.regression
    def test_get_respone_should_have_correct_status(self, set_up):
        response = self.get_get_method.text
        response_json = json.loads(response)
        response_status = jsonpath.jsonpath(response_json, 'completed')
        assert response_status[0] == False
