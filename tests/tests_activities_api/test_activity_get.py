import json
import jsonpath
from pytest import mark

from base_method.json_loader import get_data_from_json


@mark.usefixtures("get_activity_method")
class TestsGetActivity:

    @mark.activity
    @mark.regression
    def test_get_response_should_have_correct_id(self, get_activity_method):
        response_id = get_data_from_json(get_activity_method, 'id')
        assert response_id == 1

    @mark.activity
    @mark.regression
    def test_get_response_should_have_correct_title(self, get_activity_method):
        response_title = get_data_from_json(get_activity_method, 'title')
        assert response_title == "Activity 1"

    @mark.activity
    @mark.regression
    def test_get_respone_should_have_correct_status(self, get_activity_method):
        response_status = get_data_from_json(get_activity_method, 'completed')
        assert response_status == False
