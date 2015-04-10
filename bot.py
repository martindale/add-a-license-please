# Built-in imports


# Third-party dependencies
from pymongo import MongoClient
import requests


# Custom imports
import config


client = MongoClient('localhost', 23467)
db = client.add_a_license_db


def make_request(endpoint, req_type='get', headers={}, params={}, body={}):
    '''Make a HTTP request and return JSON response

    Arguments:
        endpoint: Github endpoint to hit
        req_type: HTTP request type
        headers: Any custom headers that must be sent
        params: 'get' query parameters
        body: 'post' body content
    '''

    if not headers.has_key('Authorization'):
        headers['Authorization'] = ('token %s' % config.github['access_token'])

    url = config.github['base_url'] + endpoint

    if req_type is 'get':
        r = requests.get(url, headers=headers, params=params)
    elif req_type is 'post':
        r = requests.post(url, headers=headers, payload=body)

    try:
        return r.json()
    except e:
        # TODO log this
        return None


def get_search_results():
    params = {'q': 'stars:"<5 AND >1"', 'sort': 'updated'}
    r = make_request('/search/repositories', params=params)
    print r['items'][0]['full_name']


def main():
    get_search_results()


if __name__ == '__main__':
    main()
