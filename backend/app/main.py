from rich.console import Console
from dotenv import load_dotenv
import os

console = Console()

load_dotenv()

project_name = os.getenv("PROJECT_NAME")
owner = os.getenv("OWNER_NAME")
version = os.getenv("VERSION")

console.rule(f"[cyan]{project_name}v{version}")
console.print("[green]✓ Loading Configuration...")
console.print("[green]✓ System Ready")
console.print(f"Welcome back, {owner}.", style= "bold cyan")