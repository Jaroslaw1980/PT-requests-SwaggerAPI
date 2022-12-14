from pytest import fixture, mark
from pytest import fixture

from methods.authors_methods import AuthorsApiMethod


class TestsGetAuthorsGETALL:

    @fixture
    def set_up(self):
        self.get_all_method = AuthorsApiMethod().get_all_method()

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_status_code(self, set_up):
        self.code = self.get_all_method.status_code
        assert self.code == 200

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_list_of_authors(self, set_up):
        json_response = self.get_all_method.json()
        assert isinstance(json_response, list)

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_api(self, set_up):
        assert self.get_all_method.headers['api-supported-versions'] == '1.0'

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_server(self, set_up):
        assert self.get_all_method.headers['Server'] == 'Kestrel'

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_transfer_encoding(self, set_up):
        assert self.get_all_method.headers['Transfer-Encoding'] == 'chunked'

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_content_type(self, set_up):
        assert self.get_all_method.headers['Content-Type'] == 'application/json; charset=utf-8; v=1.0'