import requests


def print_response_information(response):
    print response.status_code, '\n'
    print response.headers['content-type'], '\n'
    print response.content, '\n'


def get_request(host, uri, params, **kwargs):
    get_response = requests.get(host + uri, params=params)
    print_response_information(get_response)
    return get_response

