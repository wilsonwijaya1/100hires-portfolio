# 100Hires Portfolio Submission

## Overview
This repository showcases the submission for the 100Hires hiring challenge. It documents the tools used, steps taken, and how any issues were resolved.

## Installed Tools

- Python 3.11
- requests >= 2.31.0
- beautifulsoup4 >= 4.12.0
- urllib3 >= 2.0.0
- Git with credential helper (`manager-core`)

## Steps Completed

1. **Initialized repository**
   - Set remote to `https://github.com/wilsonwijaya1/100hires-portfolio.git`.
   - Switched branch to default `main`.

2. **Retrieved remote README**
   - Attempted to fetch `README.md` from the remote GitHub repository via the GitHub REST API (`GET /repos/wilsonwijaya1/100hires-portfolio/contents/README.md`).
   - Remote repository returned an empty state (HTTP 404), indicating no README was present.

3. **Prepared submission documents**
   - Created `requirements.txt` based on actual dependencies used in the project (`requests`, `beautifulsoup4`, `urllib3`).
   - Created `seo-audit/sheet_request_dealer_relations.py`, a scraper workflow that:
     - Requests a target URL with a 20-second timeout.
     - Raises a clear error on any network/HTTP issues.
     - Parses HTML with BeautifulSoup, extracts visible text, and filters lines by keywords.
     - Prints keyword-based matches so results can be inspected quickly.

4. **Wrote this final README**
   - Replaced the placeholder with an accurate README describing the real environment, files, and workflow steps.

## Issues Encountered and How They Were Resolved

- **Remote repository had no existing README**
  - The GitHub API returned HTTP 404 for the README path.
  - Resolved by checking the API response and preparing an accurate initial README from scratch rather than from remote content.

- **Initial scrape workflow did not include robust error handling**
  - Without a `try/except` around the HTTP request, any timeout or connection issue would stop the script abruptly.
  - Resolved by wrapping the request in a `try/except requests.RequestException` block, raising a clear `SystemExit` with the underlying network error message.

## Author

Wilson Wijaya
