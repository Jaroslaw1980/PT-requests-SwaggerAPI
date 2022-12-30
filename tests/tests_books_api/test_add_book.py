from pytest import mark

@mark.usefixtures("books_add_method")
class TestsAddBook:

    @mark.books
    @mark.regression
    def test_add_book_should_return_proper_status_code(self, books_add_method):
        self.code = books_add_method.status_code
        assert self.code == 200
