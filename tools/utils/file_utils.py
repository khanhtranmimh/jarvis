"""Common file I/O helpers used across Jarvis tools."""

from __future__ import annotations

from pathlib import Path


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_text(path: str | Path, content: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def read_prompt(name: str, category: str = "") -> str:
    """Load a prompt template from the prompts/ directory by name."""
    base = Path(__file__).parent.parent.parent / "prompts"
    candidates = [
        base / category / f"{name}.md",
        base / f"{name}.md",
    ]
    for path in candidates:
        if path.exists():
            return path.read_text(encoding="utf-8")
    raise FileNotFoundError(f"Prompt '{name}' not found in prompts/{category}/")
