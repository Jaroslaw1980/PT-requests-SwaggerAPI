from pytest import mark

@mark.usefixtures("activities_delete_method")
class TestsDeleteAuthor:

    @mark.activity
    @mark.regression
    def test_delete_response_should_have_correct_status_code(self, activities_delete_method):
        assert activities_delete_method.status_code == 200
