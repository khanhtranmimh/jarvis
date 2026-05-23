"""
Chat loop đơn giản với Ollama — chạy local, không cần API key.
Simple interactive chat loop with a local Ollama model.

Usage:
    uv run python examples/ollama_chat.py
    uv run python examples/ollama_chat.py --model mistral
"""

import argparse

from tools.llm.ollama_client import DEFAULT_MODEL, get_client, list_models
from tools.utils.console import console, print_error, print_info, print_response, print_success


def chat(model: str) -> None:
    client = get_client()
    history: list[dict] = []
    system = "Ban la JARVIS -- tro ly AI thong minh cua Iron Man. Tra loi ngan gon, huu ich."

    print_success(f"JARVIS online | model: {model} | go 'exit' de thoat")
    console.rule()

    while True:
        try:
            user_input = input("\nBan: ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "thoat"):
            break

        history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system}, *history],
            max_tokens=2048,
        )
        reply = response.choices[0].message.content or ""
        history.append({"role": "assistant", "content": reply})

        print_response(reply, title="JARVIS")

    print_info("JARVIS offline. Tam biet!")


def main() -> None:
    models = list_models()
    if not models:
        print_error("Ollama chua chay hoac chua co model nao.")
        print_info("Chay: ollama pull llama3.2")
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=models[0], choices=models)
    args = parser.parse_args()

    chat(args.model)


if __name__ == "__main__":
    main()
