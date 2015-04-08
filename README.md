# add-a-license-please
A bot that crawls Github for projects without any license, and asks the owner to add a license.

### Flow

https://github.com/sigmavirus24/github3.py

1. Get repositories with at least 2 stars sorted by recently updated - https://developer.github.com/v3/search/#search-repositories
2. For every repository, check in contents if there's a `LICENSE{.*}` file - https://api.github.com/repos/dtrupenn/Tetris/contents . If yes, skip.
4. If not, get the `README{.*}` file - https://api.github.com/repos/dtrupenn/Tetris/contents
  - Get it's raw content: https://api.github.com/repos/karan/projects/contents/README.md
  - Check if there's license info there
  - If yes, skip
  - If not, move to 5.
5. Create an issue - https://developer.github.com/v3/issues/#create-an-issue
