import json
import jsonpath
from pytest import mark


@mark.usefixtures("author_get_method")
class TestsGetAuthor:

    @mark.authors
    @mark.regression
    def test_get_response_should_have_correct_id(self, author_get_method):
        response_json = json.loads(author_get_method.text)
        response_id = jsonpath.jsonpath(response_json, 'id')
        assert response_id[0] == 1

    @mark.authors
    @mark.regression
    def test_get_response_should_have_correct_idbook(self, author_get_method):
        response_json = json.loads(author_get_method.text)
        response_title = jsonpath.jsonpath(response_json, 'idBook')
        assert response_title[0] == 1

    @mark.authors
    @mark.regression
    def test_get_respone_should_have_correct_firstname(self, author_get_method):
        response_json = json.loads(author_get_method.text)
        response_status = jsonpath.jsonpath(response_json, 'firstName')
        assert response_status[0] == 'First Name 1'
