import jsonpath
import pytest
from pytest import fixture

from methods.activities_methods import ActivitiesApiMethod


class TestsAddActivity:

    @fixture
    def set_up(self):
        self.get_post_method = ActivitiesApiMethod().post_method()
        self.get_add_method = ActivitiesApiMethod().get_method()
        self.get_delete_method = ActivitiesApiMethod().get_delete_method()

    @pytest.mark.activity
    @pytest.mark.regression
    def test_check_added_activity_status_code(self, set_up):
        assert self.get_post_method.status_code == 200

    @pytest.mark.activity
    @pytest.mark.regression
    def test_check_if_activity_is_completed(self, set_up):
        json_text = self.get_post_method.text
        completed = jsonpath.jsonpath(json_text, 'completed')
        assert completed == False

    @pytest.mark.activity
    @pytest.mark.regression
    def test_check_if_activity_is_added(self, set_up):
        assert self.get_add_method.status_code == 200

    @pytest.mark.activity
    @pytest.mark.regression
    def test_check_if_activity_is_deleted(self, set_up):
        assert self.get_delete_method.status_code == 200
