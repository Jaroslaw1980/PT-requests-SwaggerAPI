import json
import jsonpath
from pytest import mark


@mark.usefixtures("author_add_method")
class TestsAddAuthorPOST:

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_response_code(self, author_add_method):
        assert author_add_method.status_code == 200

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_id(self, author_add_method):
        response_json = json.loads(author_add_method.text)
        id_field_content = jsonpath.jsonpath(response_json, "id")
        assert id_field_content[0] == 1

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_bookid(self, author_add_method):
        response_json = json.loads(author_add_method.text)
        title_field_content = jsonpath.jsonpath(response_json, "idBook")
        assert title_field_content[0] == 1
