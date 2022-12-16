import jsonpath
from pytest import mark


@mark.usefixtures("activities_add_method", "activities_delete_method", "activities_get_method")
class TestsAddActivity:

    @mark.activity
    @mark.regression
    def test_check_added_activity_status_code(self, activities_add_method):
        assert activities_add_method.status_code == 200

    @mark.activity
    @mark.regression
    def test_check_if_activity_is_completed(self, activities_add_method):
        json_text = activities_add_method.text
        completed = jsonpath.jsonpath(json_text, 'completed')
        assert completed == False

    @mark.activity
    @mark.regression
    def test_check_if_activity_is_added(self, activities_get_method):
        assert activities_get_method.status_code == 200

    @mark.activity
    @mark.regression
    def test_check_if_activity_is_deleted(self, activities_delete_method):
        assert activities_delete_method.status_code == 200
