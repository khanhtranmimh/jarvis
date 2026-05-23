"""Pretty console output using Rich."""

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()


def print_response(text: str, title: str = "JARVIS") -> None:
    console.print(Panel(Markdown(text), title=f"[bold cyan]{title}[/bold cyan]", border_style="cyan"))


def print_info(msg: str) -> None:
    console.print(f"[bold blue][i][/bold blue]  {msg}")


def print_success(msg: str) -> None:
    console.print(f"[bold green][ok][/bold green]  {msg}")


def print_error(msg: str) -> None:
    console.print(f"[bold red][!][/bold red]  {msg}")
