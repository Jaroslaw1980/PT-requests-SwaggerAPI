from pytest import mark
from base_method.json_loader import get_data_from_json

@mark.usefixtures("activities_add_method")
class TestsAddAcitivityPOST:

    @mark.activity
    @mark.regression
    def test_add_activity_should_return_proper_response_code(self, activities_add_method):
        assert activities_add_method.status_code == 200

    @mark.activity
    @mark.regression
    def test_add_activity_should_return_proper_id(self, activities_add_method):
        id_field_content = get_data_from_json(activities_add_method, 'id')
        assert id_field_content == 17

    @mark.activity
    @mark.regression
    def test_add_activity_should_return_proper_title_field(self, activities_add_method):
        title_field_content = get_data_from_json(activities_add_method, 'title')
        assert title_field_content == 'Cycling'
