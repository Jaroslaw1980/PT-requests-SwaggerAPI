from pytest import mark


@mark.usefixtures("author_get_all_method")
class TestsGetAuthorsGETALL:

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_status_code(self, author_get_all_method):
        self.code = author_get_all_method.status_code
        assert self.code == 200

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_list_of_authors(self, author_get_all_method):
        json_response = author_get_all_method.json()
        assert isinstance(json_response, list)

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_api(self, author_get_all_method):
        assert author_get_all_method.headers['api-supported-versions'] == '1.0'

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_server(self, author_get_all_method):
        assert author_get_all_method.headers['Server'] == 'Kestrel'

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_transfer_encoding(self, author_get_all_method):
        assert author_get_all_method.headers['Transfer-Encoding'] == 'chunked'

    @mark.authors
    @mark.regression
    def test_get_all_authors_should_return_proper_header_content_type(self, author_get_all_method):
        assert author_get_all_method.headers['Content-Type'] == 'application/json; charset=utf-8; v=1.0'
