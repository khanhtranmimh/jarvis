"""
Ví dụ chạy ReAct Agent với nhiều task khác nhau.
Demo of the ReAct agent solving different tasks.

Usage:
    uv run python examples/run_agent.py
    uv run python examples/run_agent.py --model qwen2.5:7b
"""

import argparse

from agents.react_agent import run
from tools.llm.ollama_client import list_models
from tools.utils.console import console, print_error, print_info, print_response, print_success

DEMO_TASKS = [
    "What is today's date and time?",
    "Calculate: (123 * 456) + (789 / 3)",
    "List the files in the current directory, then tell me how many there are.",
]


def main(model: str) -> None:
    print_success(f"JARVIS Agent ready | model: {model}")

    # Let user pick a task or type their own
    console.print("\n[bold]Demo tasks:[/bold]")
    for i, task in enumerate(DEMO_TASKS, 1):
        console.print(f"  [{i}] {task}")
    console.print("  [0] Type your own task")

    choice = input("\nPilih (0-3): ").strip()

    if choice in ("1", "2", "3"):
        task = DEMO_TASKS[int(choice) - 1]
    else:
        task = input("Task: ").strip()

    if not task:
        print_error("No task provided.")
        return

    print_info(f"Task: {task}")
    answer = run(task, model=model, verbose=True)

    console.rule()
    print_response(answer, title="JARVIS Final Answer")


if __name__ == "__main__":
    models = list_models()
    if not models:
        print_error("Ollama is not running or has no models.")
        print_info("Run: ollama pull llama3.2")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("--model", default=models[0], choices=models)
        args = parser.parse_args()
        main(args.model)
