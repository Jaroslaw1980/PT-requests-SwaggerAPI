import json
import jsonpath
from pytest import fixture
from pytest import mark

from methods.authors_methods import AuthorsApiMethod


class TestsAddAuthorPOST:

    @fixture
    def set_up(self):
        self.get_post_method = AuthorsApiMethod().post_method()

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_response_code(self, set_up):
        assert self.get_post_method.status_code == 200

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_id(self, set_up):
        response_json = json.loads(self.get_post_method.text)
        id_field_content = jsonpath.jsonpath(response_json, "id")
        assert id_field_content[0] == 1

    @mark.authors
    @mark.regression
    def test_add_author_should_return_proper_bookid(self, set_up):
        response_json = json.loads(self.get_post_method.text)
        title_field_content = jsonpath.jsonpath(response_json, "idBook")
        assert title_field_content[0] == 1
