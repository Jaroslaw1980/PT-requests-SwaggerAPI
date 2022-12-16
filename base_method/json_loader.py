import json
import jsonpath


def get_data_from_json(method, value):
    json_text = method.text
    json_request = json.loads(json_text)
    json_value = jsonpath.jsonpath(json_request, value)
    return json_value[0]
