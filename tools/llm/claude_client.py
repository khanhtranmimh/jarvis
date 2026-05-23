"""Thin wrapper around the Anthropic SDK with sensible defaults."""

from __future__ import annotations

import os
from typing import Any

import anthropic
from dotenv import load_dotenv

load_dotenv()


def get_client() -> anthropic.Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError("ANTHROPIC_API_KEY not set. Copy .env.example → .env and fill it in.")
    return anthropic.Anthropic(api_key=api_key)


def ask(
    prompt: str,
    *,
    model: str = "claude-sonnet-4-6",
    max_tokens: int = 4096,
    system: str = "You are a helpful assistant.",
    **kwargs: Any,
) -> str:
    """Send a single prompt and return the text response."""
    client = get_client()
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": prompt}],
        **kwargs,
    )
    return message.content[0].text


def ask_with_cache(
    prompt: str,
    *,
    system: str = "You are a helpful assistant.",
    model: str = "claude-sonnet-4-6",
    max_tokens: int = 4096,
) -> str:
    """Same as ask() but caches the system prompt to save tokens on repeated calls."""
    client = get_client()
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=[
            {
                "type": "text",
                "text": system,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text
