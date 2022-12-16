import jsonpath
from pytest import mark

from base_method.json_loader import get_data_from_json


@mark.usefixtures("activities_add_method", "activities_delete_method", "activities_get_method")
class TestsAddActivity:

    @mark.activity
    @mark.regression
    def test_check_added_activity_status_code(self, activities_add_method):
        assert activities_add_method.status_code == 200

    @mark.activity
    @mark.regression
    def test_check_if_activity_is_completed(self, activities_add_method):
        completed = get_data_from_json(activities_add_method, 'completed')
        assert completed == True

    @mark.activity
    @mark.regression
    def test_check_if_activity_is_added(self, activities_get_method):
        assert activities_get_method.status_code == 200

    @mark.activity
    @mark.regression
    def test_check_if_activity_is_deleted(self, activities_delete_method):
        assert activities_delete_method.status_code == 200
