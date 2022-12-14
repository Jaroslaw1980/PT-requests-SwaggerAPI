import pytest

from methods.activities_methods import ActivitiesApiMethod
from pytest import fixture


class TestsGetActivitiesGETALL:

    @fixture
    def set_up(self):
        self.get_all_method = ActivitiesApiMethod().get_all_method()

    @pytest.mark.activity
    @pytest.mark.regression
    def test_get_all_activities(self, set_up):
        self.code = self.get_all_method.status_code
        assert self.code == 200

    @pytest.mark.activity
    @pytest.mark.regression
    def test_get_all_activities_should_return_list_of_activities(self, set_up):
        json_response = self.get_all_method.json()
        assert isinstance(json_response, list)

    @pytest.mark.activity
    @pytest.mark.regression
    def test_get_all_activities_should_return_proper_header_api(self, set_up):
        assert self.get_all_method.headers['api-supported-versions'] == '1.0'

    @pytest.mark.activity
    @pytest.mark.regression
    def test_get_all_activities_should_return_proper_header_server(self, set_up):
        assert self.get_all_method.headers['Server'] == 'Kestrel'

    @pytest.mark.activity
    @pytest.mark.regression
    def test_get_all_activities_should_return_proper_header_transfer_encoding(self, set_up):
        assert self.get_all_method.headers['Transfer-Encoding'] == 'chunked'

    @pytest.mark.activity
    @pytest.mark.regression
    def test_get_all_activities_should_return_proper_header_content_type(self, set_up):
        assert self.get_all_method.headers['Content-Type'] == 'application/json; charset=utf-8; v=1.0'
