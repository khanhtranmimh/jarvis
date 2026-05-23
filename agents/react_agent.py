"""
ReAct Agent — Reason + Act loop.

The LLM alternates between:
  Thought:      what it's thinking
  Action:       tool_name
  Input:        argument for the tool
  Observation:  tool result (injected by us)
  ...repeat...
  Final Answer: the answer to the user

Works with any Ollama model (no function-calling required).
"""

from __future__ import annotations

import math
import re
from datetime import datetime
from pathlib import Path
from typing import Callable

from openai import OpenAI

# ── Tools ────────────────────────────────────────────────────────────────────

def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})  # noqa: S307
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def get_datetime(_: str = "") -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_file(path: str) -> str:
    try:
        content = Path(path).read_text(encoding="utf-8")
        return content[:2000]  # cap at 2000 chars
    except Exception as e:
        return f"Error: {e}"


def list_files(directory: str = ".") -> str:
    try:
        entries = list(Path(directory).iterdir())
        return "\n".join(e.name + ("/" if e.is_dir() else "") for e in sorted(entries))
    except Exception as e:
        return f"Error: {e}"


TOOLS: dict[str, tuple[Callable, str]] = {
    "calculator":   (calculator,  "Evaluate a math expression. Input: expression string e.g. '2 ** 10'"),
    "get_datetime": (get_datetime,"Return current date and time. Input: (leave empty)"),
    "read_file":    (read_file,   "Read contents of a file. Input: file path"),
    "list_files":   (list_files,  "List files in a directory. Input: directory path (default '.')"),
}

# ── Prompt ───────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are JARVIS, a helpful AI assistant that solves tasks step by step.

You have access to the following tools:
{tools}

Use this EXACT format for every response (no deviation):

Thought: <your reasoning about what to do next>
Action: <tool name — must be one of: {tool_names}>
Input: <input for the tool>

After seeing an Observation, continue with another Thought/Action/Input OR give the final answer:

Thought: I now know the answer.
Final Answer: <your answer here>

Rules:
- Always start with Thought:
- Never skip the Thought step
- Use Final Answer: only when you have enough information
- If no tool is needed, go straight to Final Answer after one Thought
""".strip()


def build_system_prompt() -> str:
    tool_descriptions = "\n".join(
        f"  - {name}: {desc}" for name, (_, desc) in TOOLS.items()
    )
    return SYSTEM_PROMPT.format(
        tools=tool_descriptions,
        tool_names=", ".join(TOOLS.keys()),
    )


# ── Agent loop ────────────────────────────────────────────────────────────────

def run(
    task: str,
    *,
    model: str = "llama3.2",
    max_steps: int = 8,
    verbose: bool = True,
) -> str:
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    messages = [
        {"role": "system", "content": build_system_prompt()},
        {"role": "user", "content": task},
    ]

    def log(text: str) -> None:
        if verbose:
            print(text)

    for step in range(1, max_steps + 1):
        log(f"\n{'─' * 50}  Step {step}")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=512,
            temperature=0,
        )
        reply = response.choices[0].message.content or ""
        log(reply)

        messages.append({"role": "assistant", "content": reply})

        # Check for Final Answer
        if "Final Answer:" in reply:
            match = re.search(r"Final Answer:\s*(.+)", reply, re.DOTALL)
            return match.group(1).strip() if match else reply

        # Parse Action + Input
        action_match = re.search(r"Action:\s*(\w+)", reply)
        input_match  = re.search(r"Input:\s*(.+?)(?:\n|$)", reply)

        if not action_match:
            log("[agent] No action found — stopping.")
            return reply

        tool_name = action_match.group(1).strip()
        tool_input = input_match.group(1).strip() if input_match else ""

        if tool_name not in TOOLS:
            observation = f"Unknown tool '{tool_name}'. Available: {', '.join(TOOLS)}"
        else:
            tool_fn, _ = TOOLS[tool_name]
            observation = tool_fn(tool_input)

        log(f"Observation: {observation}")
        messages.append({"role": "user", "content": f"Observation: {observation}"})

    return "Max steps reached without a final answer."
