from pytest import mark

@mark.usefixtures("author_delete_method")
class TestsDeleteActivity:

    @mark.authors
    @mark.regression
    def test_delete_response_should_have_correct_status_code(self, author_delete_method):
        assert author_delete_method.status_code == 200
