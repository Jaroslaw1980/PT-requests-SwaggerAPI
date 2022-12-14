import pytest
from pytest import fixture

from methods.authors_methods import AuthorsApiMethod


class TestsDeleteAuthor:

    @fixture
    def set_up(self):
        self.get_delete_method = AuthorsApiMethod().get_delete_method()

    @pytest.mark.activity
    @pytest.mark.regression
    def test_delete_response_should_have_correct_status_code(self, set_up):
        assert self.get_delete_method.status_code == 200
