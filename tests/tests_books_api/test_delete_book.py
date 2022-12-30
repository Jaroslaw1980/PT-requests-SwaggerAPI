from pytest import mark

@mark.usefixtures("books_delete_method")
class TestsDeleteBook:

    @mark.books
    @mark.regression
    def test_get_all_books_should_return_proper_response_code(self, books_delete_method):
        self.code = books_delete_method.status_code
        assert self.code == 200
