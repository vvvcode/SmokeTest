import requests


def print_response_information(response):
    print response.status_code, '\n'
    print response.headers['content-type'], '\n'
    print response.content, '\n'


def get_request(host, uri, params, **kwargs):
    get_response = requests.get(host + uri, params=params)
    print_response_information(get_response)
    return get_response


# get: request with params can ues dictionary
get_response = get_request(host='https://appi.fengjr.com', uri='/app/api/v1/home/android', params={'v': '2.3'})
if get_response.status_code == 200:
    print 'pass'
else:
    print 'failed  ####  http code:', get_response.status_code

# response_post = requests.post('https://passport.fengjr.com/api/v3/userAddress/updateUserAddress/MYSELF',)
# print_response_information(response_post)
