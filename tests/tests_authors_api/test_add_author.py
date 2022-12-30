from pytest import mark
from base_method.json_loader import get_data_from_json

@mark.usefixtures("author_add_method")
class TestsAddAuthorPOST:

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_response_code(self, author_add_method):
        assert author_add_method.status_code == 200

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_id(self, author_add_method):
        id_field_content = get_data_from_json(author_add_method, 'id')
        assert id_field_content == 1

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_bookid(self, author_add_method):
        title_field_content = get_data_from_json(author_add_method, 'idBook')
        assert title_field_content == 1
