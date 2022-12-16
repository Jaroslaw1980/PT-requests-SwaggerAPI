import json
import requests


def setup_request_method(json_file=None, url=None, header=None, requests_method="get"):

    requests_method = requests_method.lower()

    if requests_method == "post":
        file = open(json_file)
        json_request = json.loads(file.read())
        return requests.post(url=url, json=json_request, headers=header)
    elif requests_method == "get":
        return requests.get(url=url, headers=header)
    elif requests_method == "delete":
        return requests.delete(url=url, headers=header)
