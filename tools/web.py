"""Web search and HTTP tools — no API key required for search."""

from __future__ import annotations

import json

import httpx


def web_search(query: str, max_results: int = 5) -> str:
    """Search the web via DuckDuckGo and return top results."""
    try:
        from ddgs import DDGS

        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))

        if not results:
            return "No results found."

        lines = []
        for i, r in enumerate(results, 1):
            lines.append(f"[{i}] {r['title']}\n    {r['href']}\n    {r['body'][:200]}")
        return "\n\n".join(lines)

    except ImportError:
        return "duckduckgo-search not installed. Run: uv add duckduckgo-search"
    except Exception as e:
        return f"Search error: {e}"


def http_get(url: str) -> str:
    """Perform an HTTP GET request and return the response (text, truncated)."""
    try:
        response = httpx.get(url, timeout=10, follow_redirects=True)
        response.raise_for_status()
        content = response.text[:3000]
        return f"Status: {response.status_code}\n\n{content}"
    except Exception as e:
        return f"HTTP error: {e}"


def http_get_json(url: str) -> str:
    """Perform an HTTP GET and return pretty-printed JSON."""
    try:
        response = httpx.get(url, timeout=10, follow_redirects=True)
        response.raise_for_status()
        data = response.json()
        return json.dumps(data, indent=2, ensure_ascii=False)[:3000]
    except Exception as e:
        return f"Error: {e}"
