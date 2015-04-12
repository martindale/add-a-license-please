# Built-in imports
import json
import os
import random

# Third-party dependencies
import dataset
import requests

# Custom imports
import config


# Bot constants
SEARCH_PARAMS = {'q': 'stars:"<5 AND >1"', 'sort': 'updated'}


# Gloabl variable init
db = None
if os.environ.get('PYTHON_ENV', None) is 'production':
    db = dataset.connect(config.db['prod'])
else:
    db = dataset.connect(config.db['dev'])

table = db['repos']


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


def get_readme_content(contents):
    '''Returns the content (file) object that represents a README file.

    Arguments:
        contents: The list of dict contents as returned by Github
    '''
    for content_file in contents:
        if content_file['name'].lower().startswith('readme'):
            return content_file
    return None


def file_is_license(contents_obj):
    '''Return True iff passed Github content is a license file

    Arguments:
        contents_obj: One dict as returned from repo content
    '''
    if contents_obj.type is not 'file':
        return False

    file_name = contents_obj['name'].lower()
    return True if file_name.startswith('license') else False


def readme_has_license(readme_obj):
    '''Return True iff the passed content obj has "license" in content.

    readme_obj: One dict as returned from repo content which is the readme
    '''
    if readme_obj is None or readme_obj.type is not 'file':
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


def has_seen_repo(repo_id):
    '''Return True if we have previously seen this repo.

    Arguments:
        repo_id: The repo id given by Github API
    '''
    repo = table.find_one(repo_id=repo_id)
    return bool(repo)


def create_issue(author_repo):
    '''Creates an issue requesting the user to add a license.

    Arguments:
        author_repo: "author/repo". example: karan/projects
    '''
    issue_body = '%s\n\n%s' % (random.choice(config['issue']['body']),
                               config['issue']['call_to_action'])
    body = {
        'title': random.choice(config['issue']['titles']),
        'body':
    }
    result = make_request('/repos/%s/contents' % (author_repo,), 'post',
                           body=body)
    return result


def main():
    # TODO handle exceptions
    repos = get_search_results()

    for repo in repos:
        # TODO: For every search repo, check in db if already processed
        if has_seen_repo(repo['id']):
            continue

        # Get the files in this repo
        # TODO: Handle exceptions
        repo_contents = get_repo_contents(repo['full_name'])

        found_license = False
        # Check to see if there's a license file in the repo
        for repo_file in repo_contents:
            if file_is_license(repo_file):
                # Has a license, log in db and skip
                table.insert(dict(repo_id=repo['id'],
                                  repo_name=repo['name'],
                                  repo_full_name=repo['full_name'],
                                  has_license=True,
                                  license_file=repo_file['name'],
                                  raw_repo_dump=json.dumps(repo)))
                found_license = False
                break

        if found_license:
            break

        # No explicit license file, check if readme has license info
        readme_content_obj = get_readme_content(repo_contents)
        if readme_has_license(readme_content_obj):
            # Has a license, log in db and skip
            table.insert(dict(repo_id=repo['id'],
                              repo_name=repo['name'],
                              repo_full_name=repo['full_name'],
                              has_license=True,
                              license_file=readme_content_obj['name'],
                              raw_repo_dump=json.dumps(repo)))
        else:
            # Create an issue and log it in the database
            result = create_issue(repo['full_name'])
            issue_url = result.get('html_url', None)
            table.insert(dict(repo_id=repo['id'],
                              repo_name=repo['name'],
                              repo_full_name=repo['full_name'],
                              has_license=False,
                              issue_url=issue_url,
                              raw_repo_dump=json.dumps(repo)))


if __name__ == '__main__':
    main()
