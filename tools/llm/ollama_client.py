"""Ollama client — runs local LLMs, no API key required.

Install Ollama: https://ollama.com
Pull a model:  ollama pull llama3.2
"""

from __future__ import annotations

from typing import Any

from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
DEFAULT_MODEL = "llama3.2"


def get_client() -> OpenAI:
    return OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")


def ask(
    prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    max_tokens: int = 4096,
    system: str = "You are a helpful assistant.",
    **kwargs: Any,
) -> str:
    """Send a prompt to a local Ollama model and return the text response."""
    client = get_client()
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        **kwargs,
    )
    return response.choices[0].message.content or ""


def list_models() -> list[str]:
    """Return names of locally available Ollama models."""
    import httpx

    try:
        resp = httpx.get("http://localhost:11434/api/tags", timeout=5)
        resp.raise_for_status()
        return [m["name"] for m in resp.json().get("models", [])]
    except Exception:
        return []
