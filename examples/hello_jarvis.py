"""
Bước đầu tiên: kiểm tra Jarvis hoạt động với Ollama (local, miễn phí).
First step: verify Jarvis works using Ollama (local, no API key needed).

Requirements:
    1. Install Ollama: https://ollama.com
    2. Pull a model: ollama pull llama3.2
    3. Run: uv run python examples/hello_jarvis.py

To use Claude instead, set ANTHROPIC_API_KEY in .env and change the import below.
"""

from tools.llm.ollama_client import ask, list_models
from tools.utils.console import print_error, print_info, print_response, print_success

if __name__ == "__main__":
    print_info("Checking available Ollama models...")
    models = list_models()

    if not models:
        print_error("No Ollama models found. Is Ollama running?")
        print_info("Start Ollama, then run: ollama pull llama3.2")
    else:
        print_success(f"Models available: {', '.join(models)}")
        print_info(f"Sending test message to {models[0]}...")

        response = ask(
            "Xin chao! Hay gioi thieu ban than ban trong 2 cau ngan gon bang tieng Viet.",
            model=models[0],
            system="Ban la JARVIS -- tro ly AI thong minh, ngan gon, va huu ich.",
        )

        print_response(response, title=f"JARVIS ({models[0]})")
