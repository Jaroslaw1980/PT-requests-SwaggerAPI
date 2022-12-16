import json
import jsonpath
from pytest import mark


@mark.usefixtures("activities_add_method")
class TestsAddAcitivityPOST:

    @mark.activity
    @mark.regression
    def test_add_activity_should_return_proper_response_code(self, activities_add_method):
        assert activities_add_method.status_code == 200

    @mark.activity
    @mark.regression
    def test_add_activity_should_return_proper_id(self, activities_add_method):
        response_json = json.loads(activities_add_method.text)
        id_field_content = jsonpath.jsonpath(response_json, "id")
        assert id_field_content[0] == 17

    @mark.activity
    @mark.regression
    def test_add_activity_should_return_proper_title_field(self, activities_add_method):
        response_json = json.loads(activities_add_method.text)
        title_field_content = jsonpath.jsonpath(response_json, "title")
        assert title_field_content[0] == 'Cycling'
