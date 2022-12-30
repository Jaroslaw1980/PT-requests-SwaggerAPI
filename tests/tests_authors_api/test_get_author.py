from pytest import mark
from base_method.json_loader import get_data_from_json

@mark.usefixtures("author_get_method")
class TestsGetAuthor:

    @mark.authors
    @mark.regression
    def test_get_response_should_have_correct_id(self, author_get_method):
        response_id = get_data_from_json(author_get_method, 'id')
        assert response_id == 1

    @mark.authors
    @mark.regression
    def test_get_response_should_have_correct_idbook(self, author_get_method):
        response_title = get_data_from_json(author_get_method, 'idBook')
        assert response_title == 1

    @mark.authors
    @mark.regression
    def test_get_respone_should_have_correct_firstname(self, author_get_method):
        response_name = get_data_from_json(author_get_method, 'firstName')
        assert response_name == 'First Name 1'
