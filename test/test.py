import sys
sys.path.append('../')

import unittest

import bot


license_obj = {
    "name": "LICENSE.md",
    "path": "LICENSE.md",
    "sha": "378233073e1bcc9e6b1ee8d7ec25c198760a897d",
    "size": 1078,
    "url": "https://api.github.com/repos/karan/Projects/contents/LICENSE.md?ref=master",
    "html_url": "https://github.com/karan/Projects/blob/master/LICENSE.md",
    "git_url": "https://api.github.com/repos/karan/Projects/git/blobs/378233073e1bcc9e6b1ee8d7ec25c198760a897d",
    "download_url": "https://raw.githubusercontent.com/karan/Projects/master/LICENSE.md",
    "type": "file",
    "_links": {
        "self": "https://api.github.com/repos/karan/Projects/contents/LICENSE.md?ref=master",
        "git": "https://api.github.com/repos/karan/Projects/git/blobs/378233073e1bcc9e6b1ee8d7ec25c198760a897d",
        "html": "https://github.com/karan/Projects/blob/master/LICENSE.md"
    }
}

not_license_obj = {
    "name": "NOT_LICENSE.md",
    "path": "NOT_LICENSE.md",
    "sha": "378233073e1bcc9e6b1ee8d7ec25c198760a897d",
    "size": 1078,
    "url": "https://api.github.com/repos/karan/Projects/contents/LICENSE.md?ref=master",
    "html_url": "https://github.com/karan/Projects/blob/master/LICENSE.md",
    "git_url": "https://api.github.com/repos/karan/Projects/git/blobs/378233073e1bcc9e6b1ee8d7ec25c198760a897d",
    "download_url": "https://raw.githubusercontent.com/karan/Projects/master/LICENSE.md",
    "type": "file",
    "_links": {
        "self": "https://api.github.com/repos/karan/Projects/contents/LICENSE.md?ref=master",
        "git": "https://api.github.com/repos/karan/Projects/git/blobs/378233073e1bcc9e6b1ee8d7ec25c198760a897d",
        "html": "https://github.com/karan/Projects/blob/master/LICENSE.md"
    }
}

readme_with_license = {
    "name": "README.md",
    "path": "README.md",
    "sha": "48a1c3a748d987f2ce4c1c76001405ffc3373b87",
    "size": 666,
    "url": "https://api.github.com/repos/karan/x-sarcasm/contents/README.md?ref=master",
    "html_url": "https://github.com/karan/x-sarcasm/blob/master/README.md",
    "git_url": "https://api.github.com/repos/karan/x-sarcasm/git/blobs/48a1c3a748d987f2ce4c1c76001405ffc3373b87",
    "download_url": "https://raw.githubusercontent.com/karan/x-sarcasm/master/README.md",
    "type": "file",
    "_links": {
        "self": "https://api.github.com/repos/karan/x-sarcasm/contents/README.md?ref=master",
        "git": "https://api.github.com/repos/karan/x-sarcasm/git/blobs/48a1c3a748d987f2ce4c1c76001405ffc3373b87",
        "html": "https://github.com/karan/x-sarcasm/blob/master/README.md"
    }
}

readme_without_license = {
    "name": "README.md",
    "path": "README.md",
    "sha": "343480ce0d9d983be92a4500dfcbc6447f1009f4",
    "size": 23171,
    "url": "https://api.github.com/repos/karan/Projects/contents/README.md?ref=master",
    "html_url": "https://github.com/karan/Projects/blob/master/README.md",
    "git_url": "https://api.github.com/repos/karan/Projects/git/blobs/343480ce0d9d983be92a4500dfcbc6447f1009f4",
    "download_url": "https://raw.githubusercontent.com/karan/Projects/master/README.md",
    "type": "file",
    "_links": {
        "self": "https://api.github.com/repos/karan/Projects/contents/README.md?ref=master",
        "git": "https://api.github.com/repos/karan/Projects/git/blobs/343480ce0d9d983be92a4500dfcbc6447f1009f4",
        "html": "https://github.com/karan/Projects/blob/master/README.md"
    }
}


class TestBotMethods(unittest.TestCase):

    def test_file_is_license(self):
        self.assertTrue(bot.file_is_license(license_obj))
        self.assertFalse(bot.file_is_license(not_license_obj))


    def test_readme_has_license(self):
        self.assertTrue(bot.readme_has_license(readme_with_license))
        self.assertFalse(bot.readme_has_license(readme_without_license))


if __name__ == '__main__':
    unittest.main()
