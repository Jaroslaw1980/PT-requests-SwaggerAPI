import json
import jsonpath
import pytest
from pytest import fixture

from methods.activities_methods import ActivitiesApiMethod


class TestsAddAcitivityPOST:

    @fixture
    def set_up(self):
        self.get_post_method = ActivitiesApiMethod().post_method()

    @pytest.mark.activity
    @pytest.mark.regression
    def test_add_activity_should_return_proper_response_code(self, set_up):
        assert self.get_post_method.status_code == 200

    @pytest.mark.activity
    @pytest.mark.regression
    def test_add_activity_should_return_proper_id(self, set_up):
        response_json = json.loads(self.get_post_method.text)
        id_field_content = jsonpath.jsonpath(response_json, "id")
        assert id_field_content[0] == 17

    @pytest.mark.activity
    @pytest.mark.regression
    def test_add_activity_should_return_proper_title_field(self, set_up):
        response_json = json.loads(self.get_post_method.text)
        title_field_content = jsonpath.jsonpath(response_json, "title")
        assert title_field_content[0] == 'Cycling'
