"""
Dealer Relations Sheet request scraper (workflow v1).
Maintainer: Hermes Agent workflow for 100Hires portfolio showcase.
"""

import requests
from bs4 import BeautifulSoup

TARGET_URL = "https://help.etamax.nl/dealer-service/sheet-request"  # confirm with live page as fallback
KEYWORDS = ["Sheet Request", "Dealer", "Part"]  # workbook clues

try:
    page = requests.get(TARGET_URL, timeout=20)
    page.raise_for_status()
except requests.RequestException as exc:
    raise SystemExit(f"Network error: {exc}")

soup = BeautifulSoup(page.text, "html.parser")
body_text = soup.get_text(separator="\n", strip=True)

matches = {}
for kw in KEYWORDS:
    hits = [line.strip() for line in body_text.splitlines() if kw.lower() in line.lower()]
    if hits:
        matches[kw] = hits

print(f"Checked: {TARGET_URL}")
print(f"Keyword hits: {len(matches)}")
for k, v in matches.items():
    print(f"{k!r}: {v[:5]}")
