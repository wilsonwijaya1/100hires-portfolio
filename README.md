# 100Hires Portfolio Submission

## Overview
This repository documents a hiring-process submission for 100Hires, completed using an AI-assisted workflow. It includes an installable Python tool, setup notes, and the problems encountered during setup.

## Installed Tools
- Cursor IDE (`C:\Users\Wilson\AppData\Local\Programs\cursor\`)
- Cursor add-ons: Claude Code, Codex
- Git for Windows with Windows Credential Manager
- GitHub CLI
- Python 3.11 (`requests`, `beautifulsoup4`, `urllib3`, `click`, `rich`)

## Steps Completed
1. Verified Cursor IDE is installed and launchable.
2. Confirmed Git user identity is configured.
3. Created local repository and project files.
4. Created public GitHub repo: `https://github.com/wilsonwijaya1/100hires-portfolio`
5. Linked local repo to remote, committed, and pushed to `main`.
6. Opened repository in Cursor.

## Issues Encountered and Resolution
- Remote repo was empty when first created.
  Resolved by writing the submission files locally and pushing to GitHub.
- Initial browsing flow to create the repo was slower than direct Git/CLI setup.
  Resolved by switching to local CLI completion instead of relying only on browser automation.

## Project: Local SEO Audit Tool
Why this project:
- Demonstrates practical execution relevant to Digital Strategist / SEO roles.
- Shows ability to design, build, and ship a runnable CLI tool.
- Shows systematic handling of problems and delivering finished output.

What it does:
- Takes a page URL and produces a concise SEO health snapshot.
- Checks common on-page issues: title, meta description, headings, content depth, and link detection.
- Presents results in readable text or JSON-compatible structured output.

Files:
- `seo-audit/cli.py`
- `requirements.txt`

Run:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python seo-audit/cli.py audit https://example.com
```

## Repo
- Local: `C:\Users\Wilson\100hires-portfolio`
- Remote: `https://github.com/wilsonwijaya1/100hires-portfolio`

## Author
Wilson Wijaya
