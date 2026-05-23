"""
Ví dụ: Load prompt từ thư viện và dùng với Claude.
Example: Load a prompt from the library and use it with Claude.

Usage:
    uv run python examples/prompt_from_library.py
"""

from tools.llm.claude_client import ask
from tools.utils.console import print_response, print_info
from tools.utils.file_utils import read_prompt


def run_code_review_example() -> None:
    sample_code = """
def calculate_discount(price, discount):
    result = price - price * discount / 100
    return result

prices = [100, 200, 300]
for p in prices:
    print(calculate_discount(p, 20))
"""

    prompt_template = read_prompt("code_review", category="coding")
    prompt = prompt_template.replace("{{LANGUAGE}}", "Python").replace("{{CODE}}", sample_code)

    print_info("Running code review prompt...")
    response = ask(prompt, system="Bạn là senior Python engineer.")
    print_response(response, title="Code Review — JARVIS")


if __name__ == "__main__":
    run_code_review_example()
