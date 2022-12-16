from pytest import mark


@mark.usefixtures("get_all_books_method")
class TestsGetAllBooks:

    def test_get_all_books_should_return_proper_response_code(self, get_all_books_method):
        self.code = get_all_books_method.status_code
        assert self.code == 200
