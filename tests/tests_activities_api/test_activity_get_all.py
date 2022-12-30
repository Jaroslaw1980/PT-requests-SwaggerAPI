from pytest import mark

@mark.usefixtures("get_all_activities_method")
class TestsGetActivitiesGETALL:

    @mark.activity
    @mark.regression
    def test_get_all_activities(self, get_all_activities_method):
        self.code = get_all_activities_method.status_code
        assert self.code == 200

    @mark.activity
    @mark.regression
    def test_get_all_activities_should_return_list_of_activities(self, get_all_activities_method):
        json_response = get_all_activities_method.json()
        assert isinstance(json_response, list)

    @mark.activity
    @mark.regression
    def test_get_all_activities_should_return_proper_header_api(self, get_all_activities_method):
        assert get_all_activities_method.headers['api-supported-versions'] == '1.0'

    @mark.activity
    @mark.regression
    def test_get_all_activities_should_return_proper_header_server(self, get_all_activities_method):
        assert get_all_activities_method.headers['Server'] == 'Kestrel'

    @mark.activity
    @mark.regression
    def test_get_all_activities_should_return_proper_header_transfer_encoding(self, get_all_activities_method):
        assert get_all_activities_method.headers['Transfer-Encoding'] == 'chunked'

    @mark.activity
    @mark.regression
    def test_get_all_activities_should_return_proper_header_content_type(self, get_all_activities_method):
        assert get_all_activities_method.headers['Content-Type'] == 'application/json; charset=utf-8; v=1.0'
