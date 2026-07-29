from rich.console import Console

console = Console()

def show_banner(project_name: str, version: str, owner: str):
    console.rule(f"[cyan]{project_name} v{version}")
    console.print("[green]✓ Loading Configuration...")
    console.print("[green]✓ Initializing Brain...")
    console.print("[green]✓ System Ready")
    console.print(f"Welcome back, {owner}.", style="bold cyan")