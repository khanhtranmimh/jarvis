"""
Ví dụ: So sánh response từ nhiều model khác nhau.
Example: Compare responses from multiple models.

Usage:
    uv run python examples/multi_model_compare.py
"""

import os

from tools.utils.console import console, print_info
from rich.table import Table


QUESTION = "Giải thích khái niệm 'prompt engineering' trong 2 câu ngắn gọn bằng tiếng Việt."


def compare_claude_models() -> None:
    from tools.llm.claude_client import ask

    models = [
        ("claude-haiku-4-5-20251001", "Claude Haiku 4.5 (Fast)"),
        ("claude-sonnet-4-6", "Claude Sonnet 4.6 (Balanced)"),
    ]

    table = Table(title="Claude Model Comparison", show_lines=True)
    table.add_column("Model", style="cyan", width=25)
    table.add_column("Response", style="white")

    for model_id, label in models:
        print_info(f"Querying {label}...")
        response = ask(QUESTION, model=model_id, max_tokens=200)
        table.add_row(label, response.strip())

    console.print(table)


if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY in .env first")
    else:
        compare_claude_models()
