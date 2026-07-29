from rich.console import Console

from core.startup import startup
from brain.router import Router

console = Console()

startup()

router = Router()

while True:

    command = console.input("\n[bold cyan]Chief > [/bold cyan]")

    if command.lower() in ["exit", "quit"]:
        console.print("[yellow]Goodbye, Chief.")
        break

    response = router.route(command)

    console.print(f"[green]KAI >[/green] {response}")