github = dict(
    client_id = '',
    client_secret = '',
    access_token = '',
    base_url = 'https://api.github.com'
)

db = dict(
    prod = 'sqlite:///<db_name>.db',
    dev = 'sqlite:///<db_name>.db'
)

issue = dict(
    titles = [
        'Please add a license',
        'License missing from repo',
        'Project is not open source without a license file',
        'Add a license file'
    ],
    body = [
        ('Without a license, this project isn\'t open source and no one can '
         'use the code.'),
        ('This repo is missing a license. Without a license, all code is '
         'copyright the author and may not be used by anyone else.')
    ],
    call_to_action = ('Please use something like http://choosealicense.com/ '
                      'to decide what license to use. I recommend MIT or GPL.'
                      '\n\n'
                      'A PSA called [**Add a License Please**]'
                      '(https://github.com/karan/add-a-license-please)')
)
