import json
import jsonpath

# method for getting value from response json
def get_data_from_json(method, value):
    json_text = method.text
    json_response = json.loads(json_text)
    json_value = jsonpath.jsonpath(json_response, value)
    return json_value[0]
