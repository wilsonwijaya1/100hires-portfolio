"""Local SEO audit helper.

Usage:
  python cli.py audit https://example.com
  python cli.py audit https://example.com --limit 20 --json
"""

import re
import sys
from dataclasses import dataclass
from typing import List, Optional

import click
import requests
from bs4 import BeautifulSoup
from rich import print
from rich.table import Table


@dataclass
class AuditResult:
    url: str
    status: Optional[int]
    title: Optional[str]
    meta_description: Optional[str]
    headings: List[str]
    word_count: int
    link_count: int
    issues: List[str]


def fetch_page(url: str, timeout: int = 20) -> requests.Response:
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.RequestException as exc:
        raise click.ClickException(str(exc)) from exc


def analyze(html: str, url: str) -> AuditResult:
    soup = BeautifulSoup(html, "html.parser")

    title = (soup.title.string or "").strip() if soup.title else None
    description_tag = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
    meta_description = description_tag.get("content", "").strip() if description_tag else None

    headings: List[str] = []
    for tag in ["h1", "h2", "h3"]:
        headings.extend([h.get_text(strip=True) for h in soup.find_all(tag) if h.get_text(strip=True)])

    text = soup.get_text(separator=" ", strip=True)
    word_count = len(re.findall(r"\b\w+\b", text))
    link_count = len(soup.find_all("a"))

    issues: List[str] = []
    if not title:
        issues.append("Missing <title>")
    elif len(title) < 10:
        issues.append("Title is too short")
    if not meta_description:
        issues.append("Missing meta description")
    elif len(meta_description) < 25:
        issues.append("Meta description is too short")

    h1_tags = soup.find_all("h1")
    if len(h1_tags) == 0:
        issues.append("Missing <h1>")
    elif len(h1_tags) > 1:
        issues.append("Multiple <h1> tags")

    if word_count < 150:
        issues.append("Thin content")

    if link_count == 0:
        issues.append("No internal/external links")

    return AuditResult(
        url=url,
        status=None,
        title=title,
        meta_description=meta_description,
        headings=headings,
        word_count=word_count,
        link_count=link_count,
        issues=issues,
    )


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("url")
@click.option("--limit", default=10, show_default=True, help="Max headings to show")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON")
def audit(url: str, limit: int, as_json: bool) -> None:
    """Fetch a URL and print a simple SEO audit."""
    response = fetch_page(url)
    result = analyze(response.text, url)
    result.status = response.status_code

    issues = result.issues
    if not issues:
        print(f"[bold green]No critical issues[/bold green] for [link={url}]{url}[/link]")
    else:
        print("[bold red]Issues found:[/bold red]")
        for issue in issues:
            print(f"- {issue}")

    print()
    print(f"Status: {result.status}")
    print(f"Title: {result.title}")
    print(f"Meta description: {result.meta_description}")
    print(f"Word count: {result.word_count}")
    print(f"Links found: {result.link_count}")

    headings = result.headings[:limit]
    print()
    table = Table(title="Headings", show_lines=True)
    table.add_column("Tag", justify="left", style="cyan", no_wrap=True)
    table.add_column("Text", justify="left", style="white")
    for text in headings:
        if not text:
            continue
        inferred = "plain"
        if re.match(r"^#+\s", text):
            inferred = "markdown"
        table.add_row(inferred, str(text))

    print(table)


if __name__ == "__main__":
    main()
