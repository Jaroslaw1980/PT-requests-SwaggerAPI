from pytest import fixture
from pytest import mark

from methods.authors_methods import AuthorsApiMethod


class TestsDeleteAuthor:

    @fixture
    def set_up(self):
        self.get_delete_method = AuthorsApiMethod().get_delete_method()

    @mark.activity
    @mark.regression
    def test_delete_response_should_have_correct_status_code(self, set_up):
        assert self.get_delete_method.status_code == 200
