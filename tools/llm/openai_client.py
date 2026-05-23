"""Thin wrapper around the OpenAI SDK with sensible defaults."""

from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set. Copy .env.example → .env and fill it in.")
    return OpenAI(api_key=api_key)


def ask(
    prompt: str,
    *,
    model: str = "gpt-4o",
    max_tokens: int = 4096,
    system: str = "You are a helpful assistant.",
    **kwargs: Any,
) -> str:
    """Send a single prompt and return the text response."""
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
