# 100Hires Portfolio Submission

## Overview
This repository is my submission for the 100Hires hiring process. It documents the tools I installed, the steps I completed, the problems I encountered, and how I resolved them.

## Installed Tools
- Cursor IDE (`C:\Users\Wilson\AppData\Local\Programs\cursor\`)
- Cursor add-ons: Claude Code, Codex
- Git for Windows with Windows Credential Manager
- Python 3.11 with `requests`, `beautifulsoup4`, `urllib3`

## Steps Completed
1. Installed and verified Cursor IDE launchable from the terminal.
2. Confirmed Git user identity configured as `Wilson Wijaya <wilson.wijaya@cakrawala.ac.id>`.
3. Created local repo in `C:\Users\Wilson\100hires-portfolio` with:
   - `README.md`
   - `requirements.txt`
   - `seo-audit/sheet_request_dealer_relations.py`
4. Created public GitHub repo: `https://github.com/wilsonwijaya1/100hires-portfolio`
5. Linked local repo to GitHub remote and pushed to `main`.

## Issues Encountered and How They Were Resolved
- Empty remote repository: GitHub repo had no README at first fetch. I resolved this by writing an accurate README locally and pushing.
- Initial scraping workflow lacked robust error handling. I added timeout handling and explicit `requests.RequestException` handling.
- Browser automation for GitHub repo creation was not reliable from within the chat flow. I completed the setup using Git CLI directly.

## Project: Local SEO Audit Tool
Implemented as `seo-audit/sheet_request_dealer_relations.py`:
- Accepts a target page URL.
- Fetches page HTML with timeout and error handling.
- Extracts visible text and filters by keywords (`Sheet Request`, `Dealer`, `Part`).

Run:
```bash
pip install -r requirements.txt
python seo-audit/sheet_request_dealer_relations.py
```

## Repo
- Local: `C:\Users\Wilson\100hires-portfolio`
- Remote: `https://github.com/wilsonwijaya1/100hires-portfolio`

## Author
Wilson Wijaya
