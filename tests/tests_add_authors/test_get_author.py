import json
import jsonpath
import pytest
from methods.authors_methods import AuthorsApiMethod


class TestsGetAuthor:

    @pytest.fixture()
    def set_up(self):
        self.get_get_method = AuthorsApiMethod().get_method()

    @pytest.mark.authors
    @pytest.mark.regression
    def test_get_response_should_have_correct_id(self, set_up):
        response = self.get_get_method.text
        response_json = json.loads(response)
        response_id = jsonpath.jsonpath(response_json, 'id')
        assert response_id[0] == 1

    @pytest.mark.authors
    @pytest.mark.regression
    def test_get_response_should_have_correct_idbook(self, set_up):
        response = self.get_get_method.text
        response_json = json.loads(response)
        response_title = jsonpath.jsonpath(response_json, 'idBook')
        assert response_title[0] == 1

    @pytest.mark.authors
    @pytest.mark.regression
    def test_get_respone_should_have_correct_firstname(self, set_up):
        response = self.get_get_method.text
        response_json = json.loads(response)
        response_status = jsonpath.jsonpath(response_json, 'firstName')
        assert response_status[0] == 'First Name 1'
