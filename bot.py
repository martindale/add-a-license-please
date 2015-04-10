# Built-in imports
import os

# Third-party dependencies
from pymongo import MongoClient
import requests

# Custom imports
import config


# Bot constants
SEARCH_PARAMS = {'q': 'stars:"<5 AND >1"', 'sort': 'updated'}


# Gloabl variable init
if os.environ.get('PYTHON_ENV', None) is 'production':
    client = MongoClient(config.db['prod'])
else:
    client = MongoClient(config.db['dev'])
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


def get_repo_contents(author_repo):
    '''Return the json/dict of repo contents

    Arguments:
        author_repo: "author/repo". example: karan/projects
    '''
    results = make_request('/repos/%s/contents' % (author_repo,))
    return results


def file_is_license(contents_obj):
    '''Return True iff passed Github content is a license file

    Arguments:
        contents_obj: One dict as returned from repo content
    '''
    if contents_obj.type is not 'file':
        return False

    file_name = contents_obj['name'].lower()
    return True if file_name.startswith('license')


def readme_has_license(readme_obj):
    '''Return True iff the passed content obj has "license" in content.

    readme_obj: One dict as returned from repo content which is the readme
    '''
    if readme_obj.type is not 'file':
        return False

    file_content_endpoint = readme_obj['url'].split(config.github.base_url)[1]
    headers = {'Accept': 'application/vnd.github.v3.raw'}

    readme_content = make_request(file_content_endpoint, headers=headers)
    readme_content = readme_content.lower()
    return readme_content.find("license") > -1


def get_search_results():
    '''Return a list of repos for the search.
    '''
    results = make_request('/search/repositories', params=SEARCH_PARAMS)
    return results.items


def main():
    repos = get_search_results()


if __name__ == '__main__':
    main()
