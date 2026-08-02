from rich.console import Console

from core.startup import startup
from brain.router import Router
from voice.controller import VoiceController


console = Console()

startup()

router = Router()
voice = VoiceController()


while True:

    command = console.input(
        "\n[bold cyan]Chief (type / voice / exit) > [/bold cyan]"
    ).strip().lower()

    if command == "exit":
        console.print("[yellow]Goodbye, Chief.")
        break

    if command == "voice":

        spoken_command = voice.listen()

        if not spoken_command:
            console.print("[red]I couldn't hear you, Chief.")
            continue

        console.print(f"[cyan]Chief 🎤 >[/cyan] {spoken_command}")

        response = router.route(spoken_command)

        console.print(f"[green]KAI >[/green] {response}")

        voice.speak(response)

        continue

    response = router.route(command)

    console.print(f"[green]KAI >[/green] {response}")

    voice.speak(response)