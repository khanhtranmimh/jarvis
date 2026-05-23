"""
Bước đầu tiên: kiểm tra Jarvis hoạt động.
First step: verify Jarvis is set up correctly.

Usage:
    uv run python examples/hello_jarvis.py
"""

from tools.llm.claude_client import ask
from tools.utils.console import print_response, print_info

if __name__ == "__main__":
    print_info("Sending test message to Claude...")

    response = ask(
        "Xin chào! Hãy giới thiệu bản thân bạn trong 2 câu ngắn gọn bằng tiếng Việt.",
        system="Bạn là JARVIS — trợ lý AI thông minh, ngắn gọn, và hữu ích.",
    )

    print_response(response, title="JARVIS")
