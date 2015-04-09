# Built-in imports


# Third-party dependencies
import requests

# Custom imports
import config


def make_request(endpoint, req_type='get', headers={}, body={}):
    '''Make a HTTP request
    '''

    if not headers.has_key('Authorization'):
        headers['Authorization'] = ('token %s' % config.github['access_token'])

    url = config.github['base_url'] + endpoint

    if req_type is 'get':
        r = requests.get(url, headers=headers)
    elif req_type is 'post':
        r = requests.post(url, headers=headers, payload=body)

    return r


r = make_request('/rate_limit')
print r.text
