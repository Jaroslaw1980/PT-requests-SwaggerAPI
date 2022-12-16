from pytest import mark


@mark.usefixtures("get_book_by_id_method")
class TestsGetBookById:

    @mark.authors
    @mark.regression
    def test_get_all_activities(self, get_book_by_id_method):
        self.code = get_book_by_id_method.status_code
        assert self.code == 200

    @mark.authors
    @mark.regression
    def test_get_all_activities_should_return_list_of_activities(self, get_book_by_id_method):
        json_response = get_book_by_id_method.json()
        assert isinstance(json_response, list)
