from methods.authors_methods import AuthorsApiMethod
from pytest import fixture, mark


class TestsGetBookById:

    @fixture()
    def set_up(self):
        self.get_book_method = AuthorsApiMethod().get_book_by_bookid()

    @mark.authors
    @mark.regression
    def test_get_all_activities(self, set_up):
        self.code = self.get_book_method.status_code
        assert self.code == 200

    @mark.authors
    @mark.regression
    def test_get_all_activities_should_return_list_of_activities(self, set_up):
        json_response = self.get_book_method.json()
        assert isinstance(json_response, list)
